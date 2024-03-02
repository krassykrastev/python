// Write a function that displays numbers from given start to given end and their sum. The input comes as two number parameters.

function printAndSum(start, end) {
    let sum = 0;
    let result = '';
    for (let i = start; i <= end; i++) {
        sum += i;
        result += i + ' ';
    }
    console.log(result.trim());
    console.log(`Sum: ${sum}`);
}

printAndSum(5, 10);
printAndSum(0, 26);