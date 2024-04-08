function attachEvents() {
    const titleInputElement = document.querySelector('input[type=text][name=title]');
    const authorInputElement = document.querySelector('input[type=text][name=author]');
    const submitButtonElement = document.querySelector('#form button');
    const bookTableBodyElement = document.querySelector('#books tbody');

    submitButtonElement.addEventListener('click', (e) => {
        const bookTrElement = createBookElement(titleInputElement.value, authorInputElement.value);

        bookTableBodyElement.appendChild(bookTrElement);

        titleInputElement.value = '';
        authorInputElement.value = '';
    });

}

function createBookElement(title, author) {
    const editButtonElement = document.createElement('button');
    editButtonElement.textContent = 'Edit';
    const deleteButtonElement = document.createElement('button');
    deleteButtonElement.textContent = 'Delete';

    const buttonsTdElement = document.createElement('td');
    buttonsTdElement.appendChild(editButtonElement);
    buttonsTdElement.appendChild(deleteButtonElement);

    const titleTdElement = document.createElement('td');
    titleTdElement.textContent = title;

    const authorTdElement = document.createElement('td');
    authorTdElement.textContent = author;

    const bookTrElement = document.createElement('tr');
    bookTrElement.appendChild(titleTdElement);
    bookTrElement.appendChild(authorTdElement);
    bookTrElement.appendChild(buttonsTdElement);

    return bookTrElement;
}

attachEvents();
