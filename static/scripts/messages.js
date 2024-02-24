document.addEventListener('DOMContentLoaded', (event) => {
    const messages = document.querySelectorAll('.alert');
    if (messages) {
        setTimeout(() => {
            messages.forEach(message => {
                message.style.opacity = '0';
            });
            setTimeout(() => {
                messages.forEach(message => message.remove());
            }, 600); // Wait for the fade out to finish
        }, 5000); // 3 seconds
    }
});