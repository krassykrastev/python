function solve(employeeNames){
    const employees = {};
        for (const name of employeeNames) {
            employees[name] = name.length;
        }
        for (employee in employees) {
            console.log(`Name: ${employee} -- Personal Number: ${employees[employee]}`);
        }
    }

solve([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
    ]
    );
solve([
    'Samuel Jackson',
    'Will Smith',
    'Bruce Willis',
    'Tom Holland'
    ]
    );