// Write a function, which will be given a single number. Your task is to find the sum of its digits and print it on the console.

function solve(number) {
    let sum = 0;
    while (number > 0) {
        sum += number % 10;
        number = Math.floor(number / 10);
    }
    console.log(sum);
}

solve(245678);
solve(97561);
solve(543);