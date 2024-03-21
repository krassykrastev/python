function colorize() {
    const evenRowElements = document.querySelectorAll('table tr:nth-child(2n)');

    for (const rowElement of evenRowElements) {
        rowElement.style.backgroundColor = 'Teal';   
    }
}