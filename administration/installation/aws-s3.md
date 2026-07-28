---
layout: administration
title: Installation
up: installation
subtitle: Amazon S3
---

# Amazon S3

Moera can move media files to a private Amazon S3 bucket and return presigned
URLs for direct access to them. The bucket must be created separately, and the
node must be given credentials that allow it to upload, download, and remove
objects.

The examples below use `media-moera-blog` as the bucket name,
`eu-central-1` as the AWS region, `moera-node` as the AWS profile, and
`moeranode` as the operating system user. Replace these values with your own.

## Create the bucket

In the [Amazon S3 console][1], create a general purpose bucket. See the
[AWS bucket creation guide][8] for detailed instructions.

1. Choose a globally unique bucket name. Prefer a name without dots, because
   dots may cause TLS certificate matching problems with virtual-hosted S3
   URLs.
2. Choose a region near the Moera node. The region used here must also be set
   in the node configuration.
3. Keep **Object Ownership** set to **Bucket owner enforced**.
4. Keep **Block all public access** enabled. Moera uses presigned URLs, so the
   bucket does not need to be public.

On the **Permissions** tab of the bucket, set this CORS configuration:

```json
[
  {
    "AllowedHeaders": ["*"],
    "AllowedMethods": ["GET", "HEAD"],
    "AllowedOrigins": ["*"],
    "ExposeHeaders": ["ETag"],
    "MaxAgeSeconds": 86400
  }
]
```

Moera uses multipart uploads for large files. On the **Management** tab, create
a lifecycle rule that applies to all objects and deletes incomplete multipart
uploads after seven days. This removes parts left behind by an interrupted
upload without deleting completed media objects. See the [AWS lifecycle rule
documentation][2] for details.

## Create an IAM policy and access keys

In the [IAM console][3], create a customer-managed policy with the following
JSON. Replace `media-moera-blog` with the bucket name:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "MoeraMediaObjects",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:DeleteObject",
        "s3:AbortMultipartUpload"
      ],
      "Resource": "arn:aws:s3:::media-moera-blog/*"
    }
  ]
}
```

This is an IAM identity policy, not a public bucket policy. Do not disable the
bucket's public-access block and do not grant public read access.

If the node runs outside AWS, create a dedicated IAM user, attach this policy
to it, and create an access key on the user's **Security credentials** tab.
Save the access key ID and secret access key immediately; AWS displays the
secret key only when the key is created.

When the node runs on AWS, an IAM role attached to the compute resource is
preferred to long-lived access keys. Attach the same policy to the role and
omit the `profile` setting from the node configuration. The AWS SDK will
obtain the role credentials automatically.

## Configure access keys

Do not put AWS access keys in the Moera node configuration file. Store them in
the standard shared AWS credentials file, readable only by the operating
system user that runs the node.

One way to create a named profile with the AWS CLI is:

```bash
# install -d -m 0700 -o moeranode -g moeranode /srv/moera-node/.aws
# sudo -u moeranode env \
    AWS_CONFIG_FILE=/srv/moera-node/.aws/config \
    AWS_SHARED_CREDENTIALS_FILE=/srv/moera-node/.aws/credentials \
    aws configure --profile moera-node
# chmod 0600 /srv/moera-node/.aws/config /srv/moera-node/.aws/credentials
```

Enter the access key ID, secret access key, and bucket region when prompted.
The profile name is `moera-node`. See the [AWS shared configuration and
credentials documentation][4] for the file format and profile naming rules.

Make the file locations available to the node process. For the systemd unit
shown in the [Running][5] section, add these lines to its `[Service]` section:

```ini
Environment="AWS_CONFIG_FILE=/srv/moera-node/.aws/config"
Environment="AWS_SHARED_CREDENTIALS_FILE=/srv/moera-node/.aws/credentials"
```

These explicit paths also work when the unit uses `ProtectHome=true`.

## Configure the node

Add the following to the Moera node [configuration file][6]:

```yaml
node:
  media:
    serve: accel
    cloud-accel-prefix: /cloudfile/
    direct-serve:
      source: aws-s3
      bucket: media-moera-blog
      region: eu-central-1
      profile: moera-node
```

The `profile` value selects the named profile created above. If credentials
are provided by an IAM role or by another source in the standard AWS
credentials provider chain, omit `profile`.

The `secret` setting used for [direct serving from the filesystem][7] is not
used with S3. S3 signs the URLs with the AWS credentials instead.

The node periodically uploads eligible media files to S3. The objects remain
private; clients access them through HTTPS presigned URLs with a limited
lifetime.

## Configure NGINX

With `node.media.serve` set to `accel`, the node uses an internal NGINX
location when an ordinary media API request needs an object that has already
been moved to S3. Add this location to the same `server` block that proxies the
node:

```nginx
server {
        # ...

        location /cloudfile/ {
                internal;
                proxy_pass https://media-moera-blog.s3.eu-central-1.amazonaws.com/;
                proxy_set_header Host media-moera-blog.s3.eu-central-1.amazonaws.com;
                proxy_ssl_server_name on;
                proxy_ssl_name media-moera-blog.s3.eu-central-1.amazonaws.com;
        }
}
```

Replace the bucket and region in all three hostnames. The hostname must be the
same S3 endpoint hostname that is used in the presigned URLs; the `Host` header
is part of the AWS signature. For a bucket in `us-east-1`, the endpoint may
use the shorter form:

```nginx
        location /cloudfile/ {
                internal;
                proxy_pass https://media-moera-blog.s3.amazonaws.com/;
                proxy_set_header Host media-moera-blog.s3.amazonaws.com;
                proxy_ssl_server_name on;
                proxy_ssl_name media-moera-blog.s3.amazonaws.com;
        }
```

The trailing slash on `proxy_pass` is important: it removes the internal
`/cloudfile/` prefix before sending the request to S3. NGINX forwards the
presigned query string, so it does not need AWS credentials of its own.

After changing the configuration, reload NGINX and restart `moera-node`. Check
the node log for S3 upload errors. New media becomes eligible for background
upload after it has been stored locally for at least 30 minutes.

[1]: https://console.aws.amazon.com/s3/
[2]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpu-abort-incomplete-mpu-lifecycle-config.html
[3]: https://console.aws.amazon.com/iam/
[4]: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html
[5]: running.html
[6]: config.html
[7]: direct-serving.html
[8]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html
