function solve(input) {
    const words = input.split(' ');
    const wordOccurences = {};

    for (const word of words) {
        if (!wordOccurences.hasOwnProperty(word.toLowerCase())) {
            wordOccurences[word.toLowerCase()] = 0;
        }
        wordOccurences[word.toLowerCase()] += 1;
    }

    const result = [];
    for (const word in wordOccurences) {
        if (wordOccurences[word] % 2 !== 0) {
            result.push(word);
        }
    }
    console.log(result.join(' '));
}

solve('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');
solve('Cake IS SWEET is Soft CAKE sweet Food');