// JavaScript voor wachtwoordsterkte-indicator
const passwordInput = document.querySelector('input[name="password"]');
const passwordStrength = document.getElementById('password-strength');
const togglePasswordButton = document.getElementById('toggle-password');

togglePasswordButton.addEventListener('click', () => {
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
    } else {
        passwordInput.type = 'password';
    }
});

passwordInput.addEventListener('input', () => {
    const password = passwordInput.value;
    const strength = calculatePasswordStrength(password);
    updatePasswordStrengthIndicator(strength);
});

function calculatePasswordStrength(password) {
    if (password.length < 8 || !/[A-Z]/.test(password) || !/[a-z]/.test(password)) {
        return 'Weak';
    } else if (/[\W_]/.test(password)) {
        return 'Strong';
    } else {
        return 'Average';
    }
}

function updatePasswordStrengthIndicator(strength) {
    passwordStrength.textContent = `Password strength: ${strength}`;
    if (strength === 'Weak') {
        passwordStrength.style.color = 'red';
    } else if (strength === 'Strong') {
        passwordStrength.style.color = 'green';
    } else {
        passwordStrength.style.color = 'orange';
    }
}
