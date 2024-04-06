function addItem() {
    const inputTextElement = document.getElementById('newItemText');
    const inputValueElement = document.getElementById('newItemValue');
    const selectElement = document.getElementById('menu');

    const optionElement = document.createElement('option');
    optionElement.textContent = inputTextElement.value;
    optionElement.value = inputValueElement.value;

    selectElement.appendChild(optionElement);

    inputTextElement.value = '';
    inputValueElement.value = '';
}