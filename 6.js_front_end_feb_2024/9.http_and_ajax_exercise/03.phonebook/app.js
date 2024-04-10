function attachEvents() {
    const baseUrl ='http://localhost:3030/jsonstore/phonebook';

    const loadButtonElement = document.getElementById('btnLoad');
    const btnCreateButtonElement = document.getElementById('btnCreate');
    const phonebookElement = document.getElementById('phonebook');
    const personElement = document.getElementById('person');
    const phoneElement = document.getElementById('phone');

    loadButtonElement.addEventListener('click', () => {
        phonebookElement.innerHTML = '';
        fetch(baseUrl)
            .then(response => response.json())
            .then(data => {
                Object.values(data)
                .forEach(entry => {
                    const liElement = document.createElement('li');
                    liElement.textContent = `${entry.person}: ${entry.phone}`;

                    const deleteButton = document.createElement('button');
                    deleteButton.textContent = 'Delete';
                    
                    deleteButton.addEventListener('click', () => {
                        fetch(`${baseUrl}/${entry._id}`, {
                            method: 'DELETE'
                        })
                        .then(() => liElement.remove());
                    });

                    liElement.appendChild(deleteButton);
                    phonebookElement.appendChild(liElement);
                });
            })
    });

    btnCreateButtonElement.addEventListener('click', () => {
        const person = personElement.value;
        const phone = phoneElement.value;

        fetch(baseUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ person, phone })
        })
        .then(response => response.json())
        .then(data => {
            const liElement = document.createElement('li');
            liElement.textContent = `${person}: ${phone}`;

            const deleteButton = document.createElement('button');
            deleteButton.textContent = 'Delete';
            
            deleteButton.addEventListener('click', () => {
                fetch(`${baseUrl}/${data._id}`, {
                    method: 'DELETE'
                })
                .then(() => liElement.remove());
            });

            liElement.appendChild(deleteButton);
            phonebookElement.appendChild(liElement);
        });

        personElement.value = '';
        phoneElement.value = '';
    });
}

attachEvents();