<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <style>
        /* Add additional styling as needed */
        .chat {
            margin-top: 50px;
        }
        .msg_card_body {
            height: 400px;
            overflow-y: auto;
        }
    </style>
</head>
<body>
    <div class="container-fluid h-100">
        <div class="row justify-content-center h-100">		
            <div class="col-md-8 col-xl-6 chat">
                <div class="card">
                    <div class="card-header msg_head">
                        <div class="d-flex bd-highlight">
                            <div class="img_cont">
                                <img src="https://cdn-icons-png.flaticon.com/512/387/387569.png" 
                                     class="rounded-circle user_img" 
                                     alt="Chatbot Icon">
                                <span class="online_icon"></span>
                            </div>
                            <div class="user_info">
                                <span>Medical Chatbot</span>
                                <p>Ask me anything!</p>
                            </div>
                        </div>
                    </div>
                    <div id="messageBody" class="card-body msg_card_body">
                        <!-- Messages will appear here -->
                    </div>
                    <div class="card-footer">
                        <form id="messageArea" class="input-group">
                            <input type="text" id="text" name="msg" placeholder="Type your message..." autocomplete="off" class="form-control type_msg" required>
                            <div class="input-group-append">
                                <button type="submit" id="send" class="input-group-text send_btn">
                                    <i class="fas fa-location-arrow"></i>
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        $(document).ready(function() {
            function scrollToBottom() {
                $("#messageBody").scrollTop($("#messageBody")[0].scrollHeight);
            }

            $("#messageArea").on("submit", function(event) {
                const date = new Date();
                const hour = date.getHours();
                const minute = date.getMinutes();
                const str_time = hour + ":" + (minute < 10 ? "0" : "") + minute;

                var rawText = $("#text").val().trim();
                if (!rawText) {
                    alert("Please enter a message!");
                    return false;
                }

                var userHtml = `<div class="d-flex justify-content-end mb-4">
                    <div class="msg_cotainer_send">${rawText}<span class="msg_time_send">${str_time}</span></div>
                    <div class="img_cont_msg">
                        <img src="https://i.ibb.co/d5b84Xw/Untitled-design.png" 
                             class="rounded-circle user_img_msg" 
                             alt="User Avatar">
                    </div>
                </div>`;

                $("#text").val("");
                $("#messageBody").append(userHtml);
                scrollToBottom();

                $.ajax({
                    data: { msg: rawText },
                    type: "POST",
                    url: "/get",
                }).done(function(data) {
                    var botHtml = `<div class="d-flex justify-content-start mb-4">
                        <div class="img_cont_msg">
                            <img src="https://cdn-icons-png.flaticon.com/512/387/387569.png" 
                                 class="rounded-circle user_img_msg" 
                                 alt="Chatbot Icon">
                        </div>
                        <div class="msg_cotainer">${data}<span class="msg_time">${str_time}</span></div>
                    </div>`;
                    $("#messageBody").append(botHtml);
                    scrollToBottom();
                });

                event.preventDefault();
            });
        });
    </script>
</body>
</html>
