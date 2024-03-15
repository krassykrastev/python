function solve(input) {

    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }
    
        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }
    
    const cats = [];

    input.forEach(line => {
        const [name, age] = line.split(' ');

        cats.push(new Cat(name, age));
    });

    cats.forEach(cat => cat.meow());
}

solve(['Mellow 2', 'Tom 5']); // Mellow, age 2 says Meow Tom, age 5 says Meow
solve(['Candy 1', 'Poppy 3', 'Nyx 2']); // Mellow, age 2 says Meow
