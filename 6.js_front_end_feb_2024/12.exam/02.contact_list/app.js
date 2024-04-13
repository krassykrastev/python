window.addEventListener("load", solve);

function solve() {
    // get the input fields
    const nameInputField = document.getElementById('name');
    const phoneInputField = document.getElementById('phone');
    const categoryInputField = document.getElementById('category');
    const checkList = document.getElementById('check-list');
    const addButton = document.getElementById('add-btn');

    addButton.addEventListener('click', () => {
        // add to ul
        const name = nameInputField.value; 
        const phone = phoneInputField.value;
        const category = categoryInputField.value;
        const nameParagraph = document.createElement('p');
        nameParagraph.textContent = `name:${name}`;
        const phoneParagraph = document.createElement('p');
        phoneParagraph.textContent = `phone:${phone}`;
        const categoryParagraph = document.createElement('p');
        categoryParagraph.textContent = `category:${category}`;
    
        const article = document.createElement('article');
        article.appendChild(nameParagraph);
        article.appendChild(phoneParagraph);
        article.appendChild(categoryParagraph);
    
        const editButton = document.createElement('button');
        editButton.classList.add('edit-btn');
        const saveButton = document.createElement('button');
        saveButton.classList.add('save-btn');
    
        const divButtonsElement = document.createElement('div');
        divButtonsElement.classList.add('buttons');
        divButtonsElement.appendChild(editButton); 
        divButtonsElement.appendChild(saveButton);
    
        const liElement = document.createElement('li');
        liElement.appendChild(article);
        liElement.appendChild(divButtonsElement);
    
        editButton.addEventListener('click' , () => {
            nameInputField.value = name;
            phoneInputField.value = phone;
            categoryInputField.value = category;
            liElement.remove();
          }
        )

        saveButton.addEventListener('click' , () => {
            const contactList = document.getElementById('contact-list');
            saveButton.remove();
            editButton.remove();
            const deleteButton = document.createElement('button');
            deleteButton.classList.add('del-btn');
            deleteButton.addEventListener('click' , () => {
                liElement.remove();
              }
            )
            liElement.appendChild(deleteButton);
            contactList.appendChild(liElement);
          }
        )

        checkList.appendChild(liElement);

        // clear input
        nameInputField.value = '';
        phoneInputField.value = '';
        categoryInputField.value = '';
    });
}  