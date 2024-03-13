function solve(numOne, numTwo, numThree) {
    if ((numOne < 0 && numTwo >= 0 && numThree >= 0) ||
                         (numTwo < 0 && numOne >= 0 && numThree >= 0) ||
                         (numThree < 0 && numTwo >= 0 && numOne >= 0) ||
                         (numOne < 0 && numTwo < 0 && numThree < 0)){
         return "Negative";
    } 
    else {
         return "Positive";
    }
}

console.log(solve(5, 12, -15))
console.log(solve(-6, -12, 14))
console.log(solve(-1, -2, -3))