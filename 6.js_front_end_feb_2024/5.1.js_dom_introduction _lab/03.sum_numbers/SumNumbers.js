function calc() {
    const firstInputElement = document.getElementById('num1');
    const secondInputElement = document.getElementById('num2');
    const sumInputElemtn = document.getElementById('sum');

    const firstNumnber = Number(firstInputElement.value);
    const secondNumber = Number(secondInputElement.value);

    const sum = firstNumnber + secondNumber;
    sumInputElemtn.value = sum;
}
