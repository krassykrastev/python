function deleteByEmail() {
    const inputEmailElement = document.querySelector('input[name=email]');
    const resultElement = document.getElementById('result');
    const trElements = document.querySelectorAll('table#customers tbody tr');

    //search for tr element
    const resultTrElement = Array
        .from(trElements)
        .find(trElement => trElement.children[1].textContent.includes(inputEmailElement.value));

    if (resultTrElement) {
    //delete table row
    resultTrElement.remove();

    //show deleted textContent
    resultElement.textContent = 'Deleted.';

    } else {
    //show not found textContent
    resultElement.textContent = 'Not found.';
    }

    //clear input
    inputEmailElement.value = '';
}