function solve(num1, num2) {
    function factorial(num) {
        let result = 1;
        for (let i = 1; i <= num; i++) {
            result *= i;
        }
        return result;
    }

    let factorialNum1 = factorial(num1);
    let factorialNum2 = factorial(num2);

    let result = factorialNum1 / factorialNum2;
    console.log(result.toFixed(2));
}

solve(5, 2); // 60.00
solve(6, 2); // 360.00