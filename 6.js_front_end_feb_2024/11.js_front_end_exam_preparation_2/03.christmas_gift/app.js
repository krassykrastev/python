function solve() {
    const BASE_URL = 'http://localhost:3030/jsonstore/gifts/';

    let inputForm = document.getElementsByTagName('form')[0];
    let inputGift = document.getElementById('gift');
    let inputFor = document.getElementById('for');
    let inputPrice = document.getElementById('price');
    let addBtn = document.getElementById('add-present');
    addBtn.addEventListener('click', addRecord);
    let editBtn = document.getElementById('edit-present');
    editBtn.addEventListener('click', editRecord);
    let loadBtn = document.getElementById('load-presents');
    loadBtn.addEventListener('click', loadRecords);

    let giftsList = document.getElementById('gift-list');

    async function loadRecords() {
        giftsList.innerHTML = '';

        let response = await fetch(BASE_URL);
        let data = await response.json();

        for (let record of Object.values(data)) {
            let div = document.createElement('div');
            div.className = 'gift-sock';
            div.id = record._id;

            div.innerHTML +=
            `
            <div class="content">
                <p>${record.gift}</p>
                <p>${record.for}</p>
                <p>${record.price}</p>
            </div>
            `
            let buttonsContainer = document.createElement('div');
            buttonsContainer.className = 'buttons-container';
            let changeBtn = document.createElement('button');
            changeBtn.textContent = 'Change';
            changeBtn.id = record._id;
            changeBtn.className = 'change-btn';
            changeBtn.addEventListener('click', changeRecord);
            let deleteBtn = document.createElement('button');
            deleteBtn.textContent = 'Delete';
            deleteBtn.id = record._id;
            deleteBtn.className = 'delete-btn';
            deleteBtn.addEventListener('click', deleteRecord);

            buttonsContainer.appendChild(changeBtn);
            buttonsContainer.appendChild(deleteBtn);
            div.appendChild(buttonsContainer);
            giftsList.appendChild(div);
        }
    }

    async function addRecord() {
        let gift = inputGift.value;
        let price = inputPrice.value;
        let _for = inputFor.value;

        if (gift === '' || price === '' || _for === '') {
            return;
        }

        let message = {
            "gift": gift,
            "price": price,
            "for": _for
        }

        await fetch(BASE_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(message)
        })

        inputForm.reset();
        loadRecords();
    }

    function changeRecord(e) {
        let currentRecord = e.currentTarget.parentElement.parentElement;
        let currentRecordId = e.currentTarget.id;
        currentRecord.remove();
        let info = currentRecord.querySelectorAll('div > p');
        let present = info[0].textContent;
        let _for = info[1].textContent;
        let price = info[2].textContent

        inputGift.value = present;
        inputFor.value = _for;
        inputPrice.value = price;
        inputForm.id = currentRecordId;

        addBtn.disabled = true;
        editBtn.disabled = false;
        currentTaskId = currentRecordId;
    }

    async function editRecord() {
        let gift = inputGift.value;
        let price = inputPrice.value;
        let _for = inputFor.value;
        let _id = inputForm.id;

        if (gift === '' || price === '' || _for === '') {
            return;
        }

        let message = {
            "gift": gift,
            "price": price,
            "for": _for,
            "_id": _id
        }
        
        await fetch(BASE_URL + _id, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(message)
        });
        inputForm.reset();
        loadRecords();
        addBtn.disabled = false;
        editBtn.disabled = true;
    }

    async function deleteRecord(e) {
        let _id = e.currentTarget.id;
        await fetch(BASE_URL + _id, { method: 'DELETE' });
        loadRecords();
    }
}

solve();