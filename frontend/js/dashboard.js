window.onload = () => {

    const token =
        localStorage.getItem("token");

    if (!token) {

        window.location.href =
            "login.html";
    }

    loadExpenses();
};


function logout() {

    localStorage.removeItem(
        "token"
    );

    window.location.href =
        "login.html";
}