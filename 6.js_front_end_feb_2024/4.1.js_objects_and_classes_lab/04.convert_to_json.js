function solve(firstName, lastName, hairColor) {
    let obj = {
        name: firstName,
        lastName,
        hairColor,
    };

    console.log(JSON.stringify(obj));

}

solve('George', 'Jones', 'Brown');
solve('Peter', 'Smith', 'Blond');