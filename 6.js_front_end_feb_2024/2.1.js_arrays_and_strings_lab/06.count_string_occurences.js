function solve(text, word) {
    let result = text
    .split(' ')
    .filter(element => element === word)
    .length;
    console.log(result);
}

solve('This is a word and it also is a sentence','is')
solve('softuni is great place for learning new programming languages','softuni')