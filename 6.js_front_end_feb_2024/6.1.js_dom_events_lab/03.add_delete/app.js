function addItem() {
    const inputItemElement = document.getElementById('newItemText');
    const itemsListElement = document.getElementById('items');

    //create new item element
    const newInputElement = document.createElement('li');
    newInputElement.textContent = inputItemElement.value;

    //create detele link element
    const deleteLinkElement = document.createElement('a');
    deleteLinkElement.textContent = '[Delete]';
    deleteLinkElement.href = '#';

    //add event to delete link element
    deleteLinkElement.addEventListener('click', () => {
        newInputElement.remove();
    });

    //append delete link element to new item element
    newInputElement.appendChild(deleteLinkElement);

    //append new item element to dom
    itemsListElement.appendChild(newInputElement);

    //clear input
    inputItemElement.value = '';

}