function addItem() {
    const inputElement = document.getElementById('newItemText');
    const itemListElement = document.getElementById('items');

    //create new item
    const newItemElement = document.createElement('li');

    //add text content
    newItemElement.textContent = inputElement.value;

    //append to dom
    itemListElement.appendChild(newItemElement);

    //clear input element
    inputElement.value = '';
}