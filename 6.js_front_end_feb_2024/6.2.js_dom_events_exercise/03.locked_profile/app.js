function lockedProfile() {
    const profileElements = document.querySelectorAll('.profile');
    for (const profileElement of profileElements) {
        const showButtonElement = profileElement.querySelector('button');
        const lockRadioElement = profileElement.querySelector('input[type=radio][value=lock]');

        showButtonElement.addEventListener('click', (e) => {
            if (lockRadioElement.checked) {
                return;
            }

            const additionInfoElement = showButtonElement.previousElementSibling;

            if (showButtonElement.textContent === 'Show more') {
                additionInfoElement.style.display = 'block';
                showButtonElement.textContent = "Hide it";
            } else {
                additionInfoElement.style.display = 'none';
                showButtonElement.textContent = "Show more";
            }
        });
    }
}