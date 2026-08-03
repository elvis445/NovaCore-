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

function showMemory(){

    document.getElementById("page-content").style.display="block";
    document.getElementById("page-title").innerHTML="🧠 NovaCore Memory";

    document.getElementById("page-body").innerHTML=`
        <p>No memories have been saved yet.</p>
        <p>Future versions will remember conversations, projects, and preferences.</p>
    `;

}

function showInfo(){

    document.getElementById("page-content").style.display="block";
    document.getElementById("page-title").innerHTML="🤖 About NovaCore";

    document.getElementById("page-body").innerHTML=`
        <h3>NovaCore AI</h3>
        <p><b>Version:</b> 1.0</p>
        <p><b>Developer:</b> Elvis</p>
        <p>NovaCore is an intelligent AI assistant built to help with coding, learning, research, and everyday tasks.</p>
    `;

}
