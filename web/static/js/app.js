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
