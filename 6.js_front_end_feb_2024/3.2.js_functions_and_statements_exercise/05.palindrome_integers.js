function solve(arr) {
    for (let i = 0; i < arr.length; i++) {
        const num = arr[i];
        const str = String(num);
        const reversedStr = str.split('').reverse().join('');
        const isPalindrome = str === reversedStr;
        console.log(isPalindrome);
    }
}

solve([123, 323, 421, 121]);
solve([32, 2, 232, 1010]);