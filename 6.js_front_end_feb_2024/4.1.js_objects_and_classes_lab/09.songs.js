function solve(input) {

    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
    }
    
    let n = input.shift();
    let songs = [];

    for (let i = 0; i < n; i++) {
        let [typeList, name, time] = input[i].split('_');
        let song = new Song(typeList, name, time);
        songs.push(song);
    }

    let type = input.pop();

    if (type === 'all') {
        songs.forEach(song => console.log(song.name));
    } else {
        let filtered = songs.filter(song => song.typeList === type);
        filtered.forEach(song => console.log(song.name));
    }
}

solve([3,
    'favourite_DownTown_3:14',
    'favourite_Kiss_4:16',
    'favourite_Smooth Criminal_4:01',
    'favourite']
    );

solve([4,
    'favourite_DownTown_3:14',
    'listenLater_Andalouse_3:24',
    'favourite_In To The Night_3:58',
    'favourite_Live It Up_3:48',
    'listenLater']
    );

solve([2,
    'like_Replay_3:15',
    'ban_Photoshop_3:48',
    'all']
    );