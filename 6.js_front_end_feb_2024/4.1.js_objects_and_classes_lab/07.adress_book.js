function solve(input) {
    const addressBook = {};

    input.forEach(line => {
        const[name, address] = line.split(':');
        addressBook[name] = address;
    })

    Object
    .entries(addressBook)
    .sort((a, b) => a[0].localeCompare(b[0]))
    .forEach(entry => {
        console.log(`${entry[0]} -> ${entry[1]}`);
    });
}

solve(['Tim:Doe Crossing',
'Bill:Nelson Place',
'Peter:Carlyle Ave',
'Bill:Ornery Rd']
);

solve(['Bob:Huxley Rd',
'John:Milwaukee Crossing',
'Peter:Fordem Ave',
'Bob:Redwing Ave',
'George:Mesta Crossing',
'Ted:Gateway Way',
'Bill:Gateway Way',
'John:Grover Rd',
'Peter:Huxley Rd',
'Jeff:Gateway Way',
'Jeff:Huxley Rd']
);