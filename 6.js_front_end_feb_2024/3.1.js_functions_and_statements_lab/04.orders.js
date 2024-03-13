function solve(product, quantity) {
    if (product === 'coffee') {
        return (quantity * 1.50).toFixed(2);
    }
    if (product === 'water') {
        return (quantity * 1.00).toFixed(2);
    }
    if (product === 'coke') {
        return (quantity * 1.40).toFixed(2);
    }
    if (product === 'snacks') {
        return (quantity * 2.00).toFixed(2);
    }
}

console.log(solve('water', 5)); // 5.00
console.log(solve('coffee', 2)); // 3.00