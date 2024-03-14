function solve(number) {
    let result = '';
    for (let i = 1; i < number; i++) {
        if (number % i === 0) {
            result += i + ' ';
        }
    }
    if (result.split(' ').map(Number).reduce((a, b) => a + b) === number) {
        console.log('We have a perfect number!');
    } else {
        console.log("It's not so perfect.");
    }
}

solve(6);
solve(28);
solve(1236498);