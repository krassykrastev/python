function solve(input) {
    const meetings = {};

    for (const line of input) {
        const [weekday, name] = line.split(' ');

        if (meetings[weekday]) {
            console.log(`Conflict on ${weekday}!`);
        } else {
            meetings[weekday] = name;
            console.log(`Scheduled for ${weekday}`);
        }
    }
    for (const weekday in meetings) {
        console.log(`${weekday} -> ${meetings[weekday]}`);
    }
}

solve(['Monday Peter',
'Wednesday Bill',
'Monday Tim',
'Friday Tim']);

solve(['Friday Bob',
'Saturday Ted',
'Monday Bill',
'Monday John',
'Wednesday George']
);