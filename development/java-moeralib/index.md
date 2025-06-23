---
layout: development
title: Java Library
---

# Java Library

`moeralib` ([GitHub][1]) is a library that allows Java applications to easily
interact with the Moera network.

The easiest way to install the library is from [Maven Central repository][2].
Add the following dependency to your `pom.xml`:

```
<dependency>
    <groupId>org.moera</groupId>
    <artifactId>moeralib</artifactId>
    <version>VERSION</version>
</dependency>
```

Or to your `build.gradle`:

```
implementation 'org.moera:moeralib:VERSION'
```

## Naming API

<code><a href="https://www.javadoc.io/doc/org.moera/moeralib/latest/org/moera/lib/naming/package-summary.html" target="_blank">org.moera.lib.naming</a></code>
package contains classes for interacting with Moera naming service. To access a naming server,
create `MoeraNaming` class and pass the naming server URL in the parameters. There are
constants for two well-known servers: `MoeraNaming.MAIN_NAMING_SERVER` and
`MoeraNaming.DEV_NAMING_SERVER`. The first one is used by default by `MoeraNaming`.

```java
import org.moera.lib.naming.MoeraNaming;
import org.moera.lib.naming.types.RegisteredNameInfo;

MoeraNaming naming = new MoeraNaming(MoeraNaming.DEV_NAMING_SERVER);
RegisteredNameInfo info = naming.getCurrent("balu-dev", 0);
System.out.println(info.nodeUri);
```

A static method `MoeraNaming.resolve()` is a shortcut that simplifies resolving of names.

```java
import org.moera.lib.naming.MoeraNaming;

System.out.println(MoeraNaming.resolve("balu-dev_0", MoeraNaming.DEV_NAMING_SERVER));
```

## Node API

<code><a href="https://www.javadoc.io/doc/org.moera/moeralib/latest/org/moera/lib/node/package-summary.html" target="_blank">org.moera.lib.node</a></code>
package contains classes for accessing Moera nodes. Just create `MoeraNode` class with the URL of
the node, and call the methods you need.

```java
import static org.moera.lib.naming.MoeraNaming.resolve;
import org.moera.lib.node.MoeraNode;

MoeraNode node = new MoeraNode(resolve("Alice"));
System.out.println(node.whoAmI().getFullName());
```

The library automatically parses JSON structures coming from the node and
converts them to Java objects. The corresponding types are defined in
`org.moera.lib.naming.types` and `org.moera.lib.node.types` subpackages.

```java
DomainAttributes attrs = new DomainAttributes();
attrs.setName("dave.moera.club");
attrs.setNodeId(DAVE_NODE_ID);
```

## Authentication

_[Read more about authentication][3] in the Node API reference._

To perform an authenticated request, you need to put the root secret, token, or carte
into `MoeraNode` and activate the corresponding authentication mode. Use
`rootSecret()`, `token()`, and `carte()` methods to set the root secret, token, and
carte correspondingly. The authentication mode is activated by generic
`authMethod()`, or by shortcut methods `noAuth()`, `auth()`, `authAdmin()`,
`authRootAdmin()`. After that, all API requests will be authenticated with
the selected method, if needed. You can switch to a different method at any time.

```java
import static org.moera.lib.naming.MoeraNaming.resolve;
import org.moera.lib.node.MoeraNode;

MoeraNode node = new MoeraNode(resolve("Alice"));
node.token("putthetokenhere");
node.authAdmin();
System.out.println(node.getProfile().getEmail());
```

## Managing cartes

<code><a href="https://www.javadoc.io/doc/org.moera/moeralib/latest/org/moera/lib/node/carte/MoeraCarteSource.html" target="_blank">MoeraCarteSource</a></code>
class simplifies managing authentication cartes. It obtains cartes from a home node,
caches them, supplies valid cartes for authentication, and requests new ones
when old ones expire.

```java
import static org.moera.lib.naming.MoeraNaming.resolve;
import org.moera.lib.node.MoeraNode;
import org.moera.lib.node.carte.MoeraCarteSource;
import org.moera.lib.node.types.FeedSliceInfo;
import org.moera.lib.node.types.StoryInfo;

MoeraNode home = new MoeraNode(resolve("Alice"));
home.token("putthetokenhere");
home.authAdmin();

MoeraNode node = new MoeraNode(resolve("Bob"));
node.carteSource(new MoeraCarteSource(home));
node.auth();
FeedSliceInfo slice = node.getFeedSlice("timeline");
for (StoryInfo story : slice.getStories()) {
    if (story.getPosting() != null) {
        System.out.println(story.getPosting().getOperations().getView(), story.getPosting().getHeading());
    }
}
```

## Generating cartes

<code><a href="https://www.javadoc.io/doc/org.moera/moeralib/latest/org/moera/lib/node/carte/Carte.html" target="_blank">Carte</a>.generate()</code>
static method generates a carte with the given parameters and signs it with
the provided private signing key.

```java
import java.security.interfaces.ECPrivateKey;
import java.time.Instant;

import org.moera.lib.crypto.CryptoUtil;
import org.moera.lib.node.carte.Carte;
import org.moera.lib.node.types.Scope;

byte[] rawKey = new byte[] {
    (byte)0x72, (byte)0xd0, (byte)0x81, (byte)0x7b,
    (byte)0xea, (byte)0xf1, (byte)0x80, (byte)0x0c,
    (byte)0x54, (byte)0x48, (byte)0x84, (byte)0x1e,
    (byte)0x49, (byte)0x01, (byte)0x39, (byte)0xb6,
    (byte)0x80, (byte)0xf1, (byte)0x34, (byte)0xa5,
    (byte)0x6e, (byte)0x14, (byte)0x0b, (byte)0xdb,
    (byte)0x4f, (byte)0x33, (byte)0xae, (byte)0xb2,
    (byte)0xc4, (byte)0x3e, (byte)0x3c, (byte)0x48
};

ECPrivateKey signingKey = CryptoUtil.rawToPrivateKey(rawKey);
String carte = Carte.generate(
    "app0_0", null, Instant.now(), signingKey, "Alice", Scope.ALL.getMask(), Scope.NONE.getMask()
);
```

## Universal URLs

<code><a href="https://www.javadoc.io/doc/org.moera/moeralib/latest/org/moera/lib/UniversalLocation.html" target="_blank">org.moera.lib.UniversalLocation</a></code>
class represents a Moera universal URL.

To parse a universal URL, pass it to `UniversalLocation` constructor.
The constructed instance will contain the result of parsing.

```java
import java.net.URISyntaxException;

import org.moera.lib.UniversalLocation;

try {
    UniversalLocation uni = new UniversalLocation(
        "https://moera.page/@Alice/alice.moera.blog/post/69a403ef-b72d-43e0-967e-eab5e8dce9d3"
    );
    System.out.println(uni.getNodeName(), uni.getAuthority(), uni.getPath(), uni);
} catch (URISyntaxException e) {
    // error processing
}
```

To build a universal URL from parts, use `redirectTo()` static method.

```java
import org.moera.lib.UniversalLocation;

System.out.println(UniversalLocation.redirectTo(
    "Alice_0",
    "https://alice.moera.blog/",
    "/post/69a403ef-b72d-43e0-967e-eab5e8dce9d3",
    null,
    null
));
```

`redirectTo()` method with two parameters converts URL of a page on a node to
a corresponding universal URL.

```java
import org.moera.lib.UniversalLocation;

System.out.println(UniversalLocation.redirectTo(
    "Alice_0",
    "https://alice.moera.blog/moera/post/69a403ef-b72d-43e0-967e-eab5e8dce9d3"
));
```

## Cryptography

<code><a href="https://www.javadoc.io/doc/org.moera/moeralib/latest/org/moera/lib/crypto/CryptoUtil.html" target="_blank">org.moera.lib.crypto.CryptoUtil</a></code>
is a utility class for generation of cryptographic keys, signing
<a href="../cryptography/fingerprint.html">fingerprints</a> and validating
signatures. The class uses the <a href="../cryptography/algorithms.html">algorithms</a>
defined in the Moera protocol.

Static methods for building fingerprints for various objects are defined in
<code><a href="https://www.javadoc.io/doc/org.moera/moeralib/latest/org/moera/lib/naming/Fingerprints.html" target="_blank">org.moera.lib.naming.Fingerprints</a></code>
and <code><a href="https://www.javadoc.io/doc/org.moera/moeralib/latest/org/moera/lib/node/Fingerprints.html" target="_blank">org.moera.lib.node.Fingerprints</a></code>
classes. (The methods may have several versions for different versions of
the fingerprint.)

The following code changes a node URL on the naming server.
(The user should provide mnemonic of the updating key.)

```java
import java.security.interfaces.ECPrivateKey;

import org.moera.lib.crypto.CryptoUtil;
import org.moera.lib.naming.Fingerprints;
import org.moera.lib.naming.MoeraNaming;
import org.moera.lib.naming.types.RegisteredNameInfo;
import org.moera.lib.util.Util;

ECPrivateKey privateUpdatingKey = CryptoUtil.mnemonicToPrivateKey(mnemonic);

MoeraNaming srv = new MoeraNaming();
RegisteredNameInfo info = srv.getCurrent(name, generation);

byte[] fingerprint = Fingerprints.putCall(
    name, generation, info.getUpdatingKey(), newNodeUri, info.getSigningKey(),
    Util.toTimestamp(info.getValidFrom()), info.getDigest()
);
byte[] signature = CryptoUtil.sign(fingerprint, privateUpdatingKey);

srv.put(name, generation, null, newNodeUri, null, null, info.getDigest(), signature);
```

[1]: https://github.com/MoeraOrg/java-moeralib
[2]: https://central.sonatype.com/artifact/org.moera/moeralib
[3]: /development/node-api/authentication.html
