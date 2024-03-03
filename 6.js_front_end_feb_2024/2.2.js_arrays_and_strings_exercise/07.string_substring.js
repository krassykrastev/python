function checkWord(word, text) {
    const words = text.toLowerCase().split(' ');
    const isIncluded = words.includes(word.toLowerCase());

    if (isIncluded) {
        return word;
    } 
        return `${word} not found!`;
}

const word = 'javascript';
const text = 'JavaScript is the best programming language';

console.log(checkWord('javascript','JavaScript is the best programming language'));
console.log(checkWord('python','JavaScript is the best programming language'));

