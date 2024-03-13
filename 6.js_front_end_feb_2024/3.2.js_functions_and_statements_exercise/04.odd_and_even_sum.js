function solve(number) {
    let oddSum = 0;
    let evenSum = 0;
    let digits = number.toString().split('');

    for (let digit of digits) {
        if (digit % 2 === 0) {
            evenSum += Number(digit);
        } else {
            oddSum += Number(digit);
        }
    }

    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`);
}

solve(1000435);
solve(3495892137259234);
