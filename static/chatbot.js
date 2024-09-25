$(document).ready(function() {
    const msgerForm = $("#chatForm");
    const msgerInput = $("#textInput");
    const msgerChat = $(".msger-chat");

    const BOT_IMG = "https://image.flaticon.com/icons/svg/327/327779.svg";
    const PERSON_IMG = "https://image.flaticon.com/icons/svg/145/145867.svg";
    const BOT_NAME = "ChatBot";
    const PERSON_NAME = "You";

    let context = null;
    let info = {};
    let pattern = null;

    msgerForm.on("submit", function(event) {
        event.preventDefault();

        const msgText = msgerInput.val();
        if (!msgText) return;

        appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
        msgerInput.val("");
        botResponse(msgText);
    });

    function appendMessage(name, img, side, text) {
        const msgHTML = `
            <div class="msg ${side}-msg">
                <div class="msg-img" style="background-image: url(${img})"></div>
                <div class="msg-bubble">
                    <div class="msg-info">
                        <div class="msg-info-name">${name}</div>
                        <div class="msg-info-time">${formatDate(new Date())}</div>
                    </div>
                    <div class="msg-text">${text}</div>
                </div>
            </div>`;
        msgerChat.append(msgHTML);
        msgerChat.scrollTop(msgerChat[0].scrollHeight); // Scroll to the bottom
    }

    function botResponse(rawText) {
        console.log("Sending data to server:");
        console.log("Message:", rawText);
        console.log("Context:", context);
        console.log("Info:", info);
        console.log("Pattern:", pattern);

        $.ajax({
            type: "POST",
            url: "/chat",
            data: { 
                msg: rawText, 
                context: context, 
                info: JSON.stringify(info),  // Ensure it's serialized here too
                pattern: pattern 
            },
            success: function(data) {
                appendMessage(BOT_NAME, BOT_IMG, "left", data.response);
                context = data.context;  // Update the context
                info = data.info;        // Update the info
                pattern = data.pattern;   // Update the pattern

                console.log("Received data from server:");
                console.log("Response:", data.response);
                console.log("New Context:", context);
                console.log("New Info:", info);
                console.log("New Pattern:", pattern);

                // Update hidden inputs if they're present
                $('#context').val(context);
                $('#info').val(JSON.stringify(info)); // Use JSON.stringify if it's an object
                $('#pattern').val(pattern);
            },
            error: function() {
                appendMessage(BOT_NAME, BOT_IMG, "left", "Sorry, I couldn't process that.");
            }
        });
    }

    function formatDate(date) {
        const h = "0" + date.getHours();
        const m = "0" + date.getMinutes();
        return `${h.slice(-2)}:${m.slice(-2)}`;
    }
});
