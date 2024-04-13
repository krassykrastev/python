function solve(input) {
    let n = Number(input.shift());
    let heroes = {};
    for (let i = 0; i < n; i++) {      
        let [name, hp, bullets] = input.shift().split(' ');
        heroes[name] = {hp: Number(hp), bullets: Number(bullets)};
    }
    let line = input.shift();
    while (line !== 'Ride Off Into Sunset') {
        let [command, firstArgument, secondArgument, thirdArgument] = line.split(' - ');
        if (command === 'FireShot') {
            let hero = heroes[firstArgument];
            
            if (hero.bullets > 0) {
                hero.bullets--;
                console.log(`${firstArgument} has successfully hit ${secondArgument} and now has ${hero.bullets} bullets!`);
            } else {
                console.log(`${firstArgument} doesn't have enough bullets to shoot at ${secondArgument}!`)
            }
        } else if (command === 'TakeHit') {
            let hero = heroes[firstArgument];
            hero.hp -= Number(secondArgument);
            if (hero.hp > 0) {
                console.log(`${firstArgument} took a hit for ${secondArgument} HP from ${thirdArgument} and now has ${hero.hp} HP!`);
            } else {
                console.log(`${firstArgument} was gunned down by ${thirdArgument}!`);
                delete heroes[firstArgument];
            }
        } else if (command === 'Reload') {
            let hero = heroes[firstArgument];
            if (hero.bullets < 6) {
                let reloadedBullets = 6 - hero.bullets;
                hero.bullets = 6;
                console.log(`${firstArgument} reloaded ${reloadedBullets} bullets!`)
            } else {
                console.log(`${firstArgument}'s pistol is fully loaded!`)
            }
        } else if (command === 'PatchUp') {
            let hero = heroes[firstArgument];
            if (hero.hp < 100) {
                if (hero.hp + Number(secondArgument) > 100) {
                    console.log(`${firstArgument} patched up and recovered ${100 - hero.hp} HP!`)
                    hero.hp = 100;
                } else {
                    hero.hp += Number(secondArgument);
                    console.log(`${firstArgument} patched up and recovered ${secondArgument} HP!`)
                }
            } else {
                console.log(`${firstArgument} is in full health!`);
            }
        }
        line = input.shift();
    }
    for (const hero in heroes) {
        console.log(`${hero}\n HP: ${heroes[hero].hp}\n Bullets: ${heroes[hero].bullets}`);
    }
}

solve((["2",
"Gus 100 0",
"Walt 100 6",
"FireShot - Gus - Bandit",
"TakeHit - Gus - 100 - Bandit",
"Reload - Walt",
"Ride Off Into Sunset"])
);

solve((["2",
"Jesse 100 4",
"Walt 100 5",
"FireShot - Jesse - Bandit",
 "TakeHit - Walt - 30 - Bandit",
 "PatchUp - Walt - 20" ,
 "Reload - Jesse",
 "Ride Off Into Sunset"])
);

solve((["2",
"Gus 100 4",
"Walt 100 5",
"FireShot - Gus - Bandit",
"TakeHit - Walt - 100 - Bandit",
"Reload - Gus",
"Ride Off Into Sunset"])
);