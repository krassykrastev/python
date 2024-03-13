function solve(firstCharacter, secondCharacter) {
    let start = firstCharacter.charCodeAt(0);
    let end = secondCharacter.charCodeAt(0);

    if (start > end) {
        let temp = start;
        start = end;
        end = temp;
    }

    let charactersInRange = '';
    for (let i = start + 1; i < end; i++) {
        charactersInRange += String.fromCharCode(i) + ' ';
    }

    console.log(charactersInRange);
}

solve('a', 'd');
solve('#', ':');
solve('C', '#');