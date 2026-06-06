const token =
    localStorage.getItem(
        "token"
    );


async function loadExpenses() {

    try {

        const response =
            await fetch(
                `${API_BASE_URL}/expenses/`,
                {
                    method: "GET",
                    headers: {
                        "Authorization":
                            `Bearer ${token}`
                    }
                }
            );

        const expenses =
            await response.json();

        displayExpenses(
            expenses
        );

    } catch (error) {

        console.error(
            error
        );
    }
}


async function addExpense(
    event
) {

    event.preventDefault();

    const title =
        document.getElementById(
            "title"
        ).value;

    const amount =
        parseFloat(
            document.getElementById(
                "amount"
            ).value
        );

    const category =
        document.getElementById(
            "category"
        ).value;

    const description =
        document.getElementById(
            "description"
        ).value;

    const response =
        await fetch(
            `${API_BASE_URL}/expenses/`,
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json",

                    "Authorization":
                        `Bearer ${token}`
                },

                body: JSON.stringify({
                    title,
                    amount,
                    category,
                    description
                })
            }
        );

    if (response.ok) {

        document
            .getElementById(
                "expenseForm"
            )
            .reset();

        loadExpenses();
    }
}


function displayExpenses(
    expenses
) {

    const container =
        document.getElementById(
            "expensesContainer"
        );

    container.innerHTML = "";

    let total = 0;

    expenses.forEach(
        expense => {

            total +=
                expense.amount;

            const div =
                document.createElement(
                    "div"
                );

            div.classList.add(
                "expense-item"
            );

            div.innerHTML = `
                <div>
                    <h3>${expense.title}</h3>
                    <p>${expense.category}</p>
                    <small>${expense.description}</small>
                </div>

                <div>

                    ₹${expense.amount}

                    <button
                        class="delete-btn"
                        onclick="deleteExpense(${expense.id})">

                        Delete

                    </button>

                </div>
            `;

            container.appendChild(
                div
            );
        }
    );

    document.getElementById(
        "totalExpense"
    ).innerText =
        `₹${total}`;

    document.getElementById(
        "totalTransactions"
    ).innerText =
        expenses.length;
}


async function deleteExpense(
    id
) {

    await fetch(
        `${API_BASE_URL}/expenses/${id}`,
        {
            method: "DELETE",

            headers: {
                "Authorization":
                    `Bearer ${token}`
            }
        }
    );

    loadExpenses();
}


document
    .getElementById(
        "expenseForm"
    )
    .addEventListener(
        "submit",
        addExpense
    );