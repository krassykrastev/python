function solve(numbers) {
    let oddNumbers = numbers.filter(num => num % 2 !== 0);
    let eveNumbers = numbers.filter(num => num % 2 === 0);

    let oddSum = oddNumbers.reduce((a, b) => a + b, 0);
    let evenSum = eveNumbers.reduce((a, b) => a + b, 0);

    console.log(evenSum - oddSum);
}

solve([1, 2, 3, 4, 5, 6]);
solve([3, 5, 7, 9]);
solve([2, 4, 6, 8, 10]);