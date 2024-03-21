function sumTable() {
    const tdCostElements = document.querySelectorAll('table tr td:last-of-type:not(#sum)');
    const tdSumElement = document.getElementById('sum');

    const sum = Array
    .from(tdCostElements)
    .reduce((sum, element) => sum + Number(element.textContent), 0); 
    
    tdSumElement.textContent = sum;
}