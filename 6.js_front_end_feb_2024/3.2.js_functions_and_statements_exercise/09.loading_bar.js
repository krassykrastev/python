function solve(progress) {
    let result = '';
    for (let i = 0; i < 10; i++) {
        if (i < progress / 10) {
            result += '%';
        } else {
            result += '.';
        }
    }

    if (progress === 100) {
        console.log('100% Complete!');
        console.log('[' + result + ']');
        
    } else {
        console.log(progress + '% [' + result + ']');
        console.log('Still loading...');
    }   
}

solve(30);
solve(50);
solve(100);