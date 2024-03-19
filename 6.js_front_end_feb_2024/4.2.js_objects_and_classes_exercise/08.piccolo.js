function solve(input) {
    const parking = new Set();

    for (const row of input) { 
        const [direction, carNumber] = row.split(', ');

        if (direction === 'IN') {
            parking.add(carNumber);
        } else {
            parking.delete(carNumber);
        }
    }

    if (parking.size === 0) {
        return console.log('Parking Lot is Empty');
    }

    Array.from(parking.values())
        .sort((a, b) => a.localeCompare(b))
        .forEach(carNumber => console.log(carNumber));
}

solve(['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'IN, CA9999TT',
'IN, CA2866HI',
'OUT, CA1234TA',
'IN, CA2844AA',
'OUT, CA2866HI',
'IN, CA9876HH',
'IN, CA2822UU']
);
solve(['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'OUT, CA1234TA']
);