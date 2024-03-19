function solve(input) {
    const movies = [];

    for (const row of input) {
        if (row.includes('addMovie')) {
            const movieName = row.split('addMovie ')[1];
            movies.push({ name: movieName });
        } else if (row.includes('directedBy')) {
            const [movieName, director] = row.split(' directedBy ');
            const movie = movies.find(m => m.name === movieName);
            if (movie) {
                movie.director = director;
            }
        } else if (row.includes('onDate')) {
            const [movieName, date] = row.split(' onDate ');
            const movie = movies.find(m => m.name === movieName);
            if (movie) {
                movie.date = date;
            }
        }
    }
    movies
        .filter(m => m.name && m.director && m.date)
        .forEach(movie => console.log(JSON.stringify(movie)));
}

solve([
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen'
    ]
    );
solve([
    'addMovie The Avengers',
    'addMovie Superman',
    'The Avengers directedBy Anthony Russo',
    'The Avengers onDate 30.07.2010',
    'Captain America onDate 30.07.2010',
    'Captain America directedBy Joe Russo'
    ]
    );
