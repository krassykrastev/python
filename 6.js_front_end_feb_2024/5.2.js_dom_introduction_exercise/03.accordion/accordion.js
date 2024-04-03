function toggle() {
    const toggleButtonElement = document.querySelector('.head span.button');
    const extraInformationElement = document.getElementById('extra');

    const currentButtonText = toggleButtonElement.textContent;
    if (currentButtonText === 'More') {
        toggleButtonElement.textContent = 'Less';
        extraInformationElement.style.display = 'block';
    } else {
        toggleButtonElement.textContent = 'More';
        extraInformationElement.style.display = 'none';
    }
}