// Write a function that takes an integer number as an input and check if all the digits in a given number are the same or not.
// Print on the console true if all numbers are the same and false if not. On the next line print the sum of all digits.
// The input comes as an integer number.
// The output should be printed on the console.

function solve(number) {
    let numberText = number.toString();
    let currentDigit = numberText[0];
    let isSame = true;
    let sum = Number(currentDigit);

    for (let i = 1; i < numberText.length; i ++) {
        if (currentDigit !== numberText[i]) {
            isSame = false;
        }
        currentDigit = numberText[i];
        sum += Number(currentDigit);
    }
    console.log(isSame);
    console.log(sum);
}

solve(2222222);
solve(1234);