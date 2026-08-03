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
function showMemory() {
    alert(
        "🧠 NovaCore Memory\n\n" +
        "No memories saved yet.\n\n" +
        "Soon NovaCore will remember your conversations, preferences, and projects."
    );
}

function showInfo() {
    alert(
        "🤖 NovaCore AI\n\n" +
        "Version: 1.0\n" +
        "Developer: Elvis\n\n" +
        "NovaCore is your intelligent AI assistant for learning, coding, research, and daily tasks."
    );
}
