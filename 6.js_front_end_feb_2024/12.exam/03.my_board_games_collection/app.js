const baseUrl = 'http://localhost:3030/jsonstore/games'

const loadButton = document.getElementById('load-games');
const gameListDiv = document.getElementById('games-list');
const addGameButton = document.getElementById('add-game');
const editGameButton = document.getElementById('edit-game');

const nameInputField = document.getElementById('g-name');
const playersInputField = document.getElementById('players');
const typeInputField = document.getElementById('type');

loadButton.addEventListener('click', loadGames);
addGameButton.addEventListener('click', async () => {
    const name = nameInputField.value;
    const players = playersInputField.value;
    const type = typeInputField.value;

    await fetch(baseUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, players, type })
    });

    nameInputField.value = '';
    playersInputField.value = '';
    typeInputField.value = '';

    loadGames();
});

editGameButton.addEventListener('click', async (e) => {
    const game_id = e.currentTarget.parentElement.parentElement.getAttribute('data-id');
    const name = nameInputField.value;
    const players = playersInputField.value;
    const type = typeInputField.value;
    await fetch(`${baseUrl}/${game_id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, players, type, _id: game_id })
    });

    loadGames();

    editGameButton.setAttribute('disabled', 'disabled');
    addGameButton.removeAttribute('disabled');

    nameInputField.value = '';
    playersInputField.value = '';
    typeInputField.value = '';

});

async function loadGames() {
    const response = await fetch(baseUrl);
    const data = await response.json();
    gameListDiv.innerHTML = '';

    Object.values(data).forEach(game => {
        const gameDiv = document.createElement('div');
        gameDiv.classList.add('board-game');

        const contentDiv = document.createElement('div');
        contentDiv.classList.add('content');
        const nameParagraph = document.createElement('p');
        nameParagraph.textContent = `${game.name}`;
        const playersParagraph = document.createElement('p');
        playersParagraph.textContent = `${game.players}`;
        const typeParagraph = document.createElement('p');
        typeParagraph.textContent = `${game.type}`;

        contentDiv.appendChild(nameParagraph);
        contentDiv.appendChild(playersParagraph);
        contentDiv.appendChild(typeParagraph);

        const buttonsDiv = document.createElement('div');
        buttonsDiv.classList.add('buttons-container');
        const changeButton = document.createElement('button');
        changeButton.classList.add('change-btn');
        changeButton.textContent = 'Change';
        changeButton.addEventListener('click', () => {
            const formDivElement = document.getElementById('form');
            formDivElement.setAttribute('data-id', game._id);
            nameInputField.value = game.name;
            playersInputField.value = game.players;
            typeInputField.value = game.type;
            
            editGameButton.removeAttribute('disabled');
            addGameButton.setAttribute('disabled', 'disabled');
        });


        const deleteButton = document.createElement('button');
        deleteButton.classList.add('delete-btn');
        deleteButton.textContent = 'Delete';
        deleteButton.addEventListener('click', async () => {
            await fetch(`${baseUrl}/${game._id}`, {
                method: 'DELETE'
            });

            loadGames();
        });

        buttonsDiv.appendChild(changeButton);
        buttonsDiv.appendChild(deleteButton);

        gameDiv.appendChild(contentDiv);
        gameDiv.appendChild(buttonsDiv);
        gameListDiv.appendChild(gameDiv);
    });
}