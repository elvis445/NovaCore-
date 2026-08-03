async function sendMessage() {

    let input = document.getElementById("user-input");
    let message = input.value.trim();

    if (message === "") return;

    let formData = new FormData();
    formData.append("user", message);

    let response = await fetch("/ask", {
        method: "POST",
        body: formData
    });

    let data = await response.json();

    document.getElementById("chat-box").innerHTML +=
        "<div class='user-message'>" + message + "</div>" +
        "<div class='bot-message'>" + data.reply + "</div>";

    input.value = "";
}

// NovaCore Sidebar Toggle

function toggleMenu() {

    const sidebar = document.getElementById("sidebar");

    sidebar.classList.toggle("open");

}
// Register Service Worker

if ("serviceWorker" in navigator) {

    window.addEventListener("load", function () {

        navigator.serviceWorker.register("/static/sw.js")
            .then(function (registration) {
                console.log("Service Worker registered successfully!");
            })
            .catch(function (error) {
                console.log("Service Worker registration failed:", error);
            });

    });

}
