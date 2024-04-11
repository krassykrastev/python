window.addEventListener("load", solve);

function solve() {
    const addButtonElement = document.getElementById("add-btn");
    const expenseInputElement = document.getElementById("expense");
    const amountInputElement = document.getElementById("amount");
    const dateInputElement = document.getElementById("date");
    const previewListElement = document.getElementById("preview-list");
    const expenseListElement = document.getElementById("expenses-list");
    const deleteButtonElement = document.querySelector(".btn.delete");

    addButtonElement.addEventListener('click', () => {
        //get input information
        const expense = expenseInputElement.value;
        const amount = amountInputElement.value;
        const date = dateInputElement.value;

        //check empty element
        if (!expense || !amount || !date) {
            return;
        }

        //add to preview list
        const expenseLiElement = createArticleElement(expense, amount, date);
        previewListElement.appendChild(expenseLiElement);

        //disable button
        addButtonElement.disabled = true;

        //clear inputs
        expenseInputElement.value = '';
        amountInputElement.value = '';
        dateInputElement.value = '';

        //get button elements
        const editButtonElement = expenseLiElement.querySelector('.btn.edit');
        const okButtonElement = expenseLiElement.querySelector('.btn.ok');

        //attach event listeners
        editButtonElement.addEventListener('click', () => {                 
            //send data to inputs
            expenseInputElement.value = expense;
            amountInputElement.value = amount;
            dateInputElement.value = date;

            //clear preview
            expenseLiElement.remove();

            //enable add button
            addButtonElement.disabled = false;


        });

        //attach ok event listener
        okButtonElement.addEventListener('click', () => {
            //remove buttons from expense item
            const expenseButtonsElement = expenseLiElement.querySelector('.buttons');
            expenseButtonsElement.remove();
            
            //move expense item to expense list
            expenseListElement.appendChild(expenseLiElement);

            //enable add button
            addButtonElement.disabled = false;
        });
    });

    deleteButtonElement.addEventListener('click', () => {
        expenseListElement.innerHTML = '';
    });

    function createArticleElement(expense, amount, date) {
        const pTypeElement = document.createElement("p");
        pTypeElement.textContent = `Type: ${expense}`;

        const pAmountElement = document.createElement("p");
        pAmountElement.textContent = `Amount: ${amount}$`;

        const pDateElement = document.createElement("p");
        pDateElement.textContent = `Date: ${date}`;

        const articleElement = document.createElement("article");
        articleElement.appendChild(pTypeElement);
        articleElement.appendChild(pAmountElement);
        articleElement.appendChild(pDateElement);

        const editButtonElement = document.createElement("button");
        editButtonElement.classList.add('btn', 'edit');
        editButtonElement.textContent = 'Edit';

        const okButtonElement = document.createElement("button");
        okButtonElement.classList.add('btn', 'ok');
        okButtonElement.textContent = 'ok';

        const buttonsDivElement = document.createElement("div");
        buttonsDivElement.classList.add('buttons');
        buttonsDivElement.appendChild(editButtonElement);
        buttonsDivElement.appendChild(okButtonElement);

        const liExpenseElement = document.createElement("li");
        liExpenseElement.classList.add('expense-item');
        liExpenseElement.appendChild(articleElement);
        liExpenseElement.appendChild(buttonsDivElement);

        return liExpenseElement;
    }
}