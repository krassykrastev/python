function solve(wordwordsInput, template) {
    let words = wordwordsInput.split(', ');
    let matches = template.matchAll(/\*+/g);
    for (let match of matches) {
        let word = words.find(w => w.length === match[0].length);
        template = template.replace(match[0], word);
    }
    console.log(template);
}

solve('great','softuni is ***** place for learning new programming languages')
solve('great, learning','softuni is ***** place for ******** new programming languages')