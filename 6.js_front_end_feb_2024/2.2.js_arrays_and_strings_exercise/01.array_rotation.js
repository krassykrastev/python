function solve(numbers, rotations) {
    for (let i = 0; i < rotations; i++) {
        let firstElement = numbers.shift()
        numbers.push(firstElement);
    }
    console.log(numbers.join(' '));
}

solve([51, 47, 32, 61, 21], 2)
solve([32, 21, 61, 1], 4)
solve([2, 4, 15, 31], 5)