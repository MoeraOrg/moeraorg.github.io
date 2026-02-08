(function() {
    'use strict';

    function init() {
        const form = document.getElementById('feedback-form');
        if (!form) {
            return;
        }

        const nameField = form.querySelector('[name="name"]');
        const emailField = form.querySelector('[name="email"]');
        const messageField = form.querySelector('[name="message"]');

        function setupFieldValidation(field) {
            field.addEventListener('input', function () {
                field.classList.remove('is-invalid');
            });
        }

        setupFieldValidation(nameField);
        setupFieldValidation(emailField);
        setupFieldValidation(messageField);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();

function onFeedbackSubmit(token) {
    const form = document.getElementById('feedback-form');
    const nameField = form.querySelector('[name="name"]');
    const emailField = form.querySelector('[name="email"]');
    const messageField = form.querySelector('[name="message"]');
    const bottomElement = form.querySelector('.bottom');

    const name = nameField.value.trim();
    const email = emailField.value.trim();
    const message = messageField.value.trim();

    let isValid = true;

    if (!name) {
        nameField.classList.add('is-invalid');
        isValid = false;
    }

    if (!email) {
        emailField.classList.add('is-invalid');
        isValid = false;
    }

    if (!message) {
        messageField.classList.add('is-invalid');
        isValid = false;
    }

    if (!isValid) {
        return;
    }

    function htmlEncode(str) {
        return str
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    }

    const body = `${htmlEncode(name)} &lt;<a href="mailto:${htmlEncode(email)}">${htmlEncode(email)}</a>&gt; writes:<br><br>${htmlEncode(message)}`;

    const formData = new URLSearchParams();
    formData.append('subject', name);
    formData.append('body', body);
    formData.append('g-recaptcha-response', token);

    fetch('https://feedback.moera.org/feedback', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData.toString()
    })
        .then(function (response) {
            if (response.status === 200) {
                const messageContainer = document.createElement('div');
                messageContainer.className = 'alert alert-success mt-3';
                messageContainer.textContent = 'Thank you for your feedback! We will get back to you soon.';
                bottomElement.parentNode.appendChild(messageContainer);

                form.reset();

                setTimeout(function () {
                    messageContainer.remove();
                }, 5000);
            } else {
                throw new Error('Request failed');
            }
        })
        .catch(function () {
            const errorContainer = document.createElement('div');
            errorContainer.className = 'alert alert-danger mt-3';
            errorContainer.textContent = 'Your feedback could not be submitted. Please try again later.';
            bottomElement.parentNode.appendChild(errorContainer);

            setTimeout(function () {
                errorContainer.remove();
            }, 5000);
        });
}
