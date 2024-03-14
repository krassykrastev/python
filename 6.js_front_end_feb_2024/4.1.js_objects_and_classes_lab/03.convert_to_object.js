function solve (json) {
    let obj = JSON.parse(json);
    
    Object
    .keys(obj)
    .forEach(key => console.log(`${key}: ${obj[key]}`));
}

solve('{"name": "George", "age": 40, "town": "Sofia"}');
solve('{"name": "Peter", "age": 35, "town": "Plovdiv"}');