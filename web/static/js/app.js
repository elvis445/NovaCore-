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
    console.log("NovaCore reply:", data.reply);
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


// Open a NovaCore page/panel

function openPage(title, content) {

    document.getElementById("page-content").style.display = "block";

    document.getElementById("page-title").innerText = title;

    document.getElementById("page-body").innerHTML = `
        <div style="text-align: right; margin-bottom: 20px;">
            <button
                onclick="document.getElementById('page-content').style.display='none'"
                style="background:#1f2937;color:white;border:none;padding:10px 20px;border-radius:8px;cursor:pointer;font-size:16px;">
                Close
            </button>
        </div>

        <div style="font-size:18px;line-height:1.6;">
            ${content}
        </div>
    `;
}


// Memory page

function showMemory() {

    openPage(
        "🧠 NovaCore Memory",
        "<p>Your saved memories will appear here.</p>"
    );

}


// About page

function showInfo() {

    openPage(
        "ℹ About NovaCore",
        "<p><b>NovaCore AI</b><br>Developer: Elvis<br>Version: 1.0</p>"
    );

}
