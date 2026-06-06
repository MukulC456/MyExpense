async function registerUser() {

    const username =
        document.getElementById("username").value;

    const email =
        document.getElementById("email").value;

    const password =
        document.getElementById("password").value;

    try {

        const response = await fetch(
            `${API_BASE_URL}/auth/register`,
            {
                method: "POST",
                headers: {
                    "Content-Type":
                        "application/json"
                },
                body: JSON.stringify({
                    username,
                    email,
                    password
                })
            }
        );

        const data =
            await response.json();

        console.log(
            "Register Response:",
            data
        );

        if (response.ok) {

            alert(
                "Registration Successful!"
            );

            window.location.href =
                "login.html";

        } else {

            alert(
                data.detail ||
                "Registration Failed"
            );
        }

    } catch (error) {

        console.error(
            "Register Error:",
            error
        );

        alert(
            "Cannot connect to backend."
        );
    }
}


async function loginUser() {

    const email =
        document.getElementById("email").value;

    const password =
        document.getElementById("password").value;

    const formData =
        new URLSearchParams();

    formData.append(
        "username",
        email
    );

    formData.append(
        "password",
        password
    );

    try {

        const response = await fetch(
            `${API_BASE_URL}/auth/login`,
            {
                method: "POST",
                headers: {
                    "Content-Type":
                        "application/x-www-form-urlencoded"
                },
                body: formData
            }
        );

        console.log(
            "Status:",
            response.status
        );

        const data =
            await response.json();

        console.log(
            "Login Response:",
            data
        );

        if (data.access_token) {

            localStorage.setItem(
                "token",
                data.access_token
            );

            console.log(
                "Saved Token:",
                localStorage.getItem(
                    "token"
                )
            );

            alert(
                "Login Successful!"
            );

            window.location.href =
                "dashboard.html";

        } else {

            alert(
                "Invalid Email or Password"
            );
        }

    } catch (error) {

        console.error(
            "Login Error:",
            error
        );

        alert(
            "Cannot connect to backend."
        );
    }
}