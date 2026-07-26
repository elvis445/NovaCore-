function sendMessage() {

    let input = document.getElementById("user-input");

    let chat = document.getElementById("chat-box");

    let message = input.value.trim();

    if(message === "") return;

    chat.innerHTML += `
        <div class="user-message">${message}</div>
    `;

    input.value = "";

    setTimeout(function(){

        chat.innerHTML += `
            <div class="bot-message">
                NovaCore is still learning...
            </div>
        `;

        chat.scrollTop = chat.scrollHeight;

    },1000);

}
