function solve(grade) {
    let formatttedGrade = ''
    if (grade < 3) {
        formatttedGrade = `Fail (${grade})`
    } else if (grade < 3.5) {
        formatttedGrade = `Poor (${grade.toFixed(2)})`
    } else if (grade < 4.5) {
        formatttedGrade = `Good (${grade.toFixed(2)})`
    } else if (grade < 5.5) {
        formatttedGrade = `Very good (${grade.toFixed(2)})`
    } else {
        formatttedGrade = `Excellent (${grade.toFixed(2)})`
    }

    console.log(formatttedGrade)
}

solve(3.33)
solve(4.50)
solve(2.99)