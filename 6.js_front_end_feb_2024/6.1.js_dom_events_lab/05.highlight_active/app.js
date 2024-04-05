function focused() {
    const inputElements = document.querySelectorAll('input');
 
    Array.from(inputElements).forEach(input => {
        input.addEventListener('focus', event => {
            event.target.parentElement.classList.add('focused');
        });

        input.addEventListener('blur', event => {
            event.target.parentElement.classList.remove('focused');
        });
    });
}