function solve(number) {
    let result = '';
    for (let i = 0; i < number; i++) {
        result += `${number} `.repeat(number).trim() + '\n';
    }
    console.log(result);
}

solve(3);
solve(7);
solve(2);