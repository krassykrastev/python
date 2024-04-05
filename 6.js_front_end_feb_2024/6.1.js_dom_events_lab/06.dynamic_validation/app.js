function validate() {
    const emailInputElement = document.getElementById('email');
    const pattern = /^[a-z]+@[a-z]+\.[a-z]+$/;

    emailInputElement.addEventListener('change', (event) => {
        const email = emailInputElement.value;
        if (pattern.test(email)) {
            emailInputElement.classList.remove('error');
        } else {
            emailInputElement.classList.add('error');
        }    
    });       
}