from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from decouple import config
from flask import Flask, request, abort

# 找機會部屬到GOOGLE測試一下LINE

line_bot_api = LineBotApi(config('LINE_KEY'))

def handle_message(event):
    user_message = event.message.text
    if user_message == "!HI":
        reply_message = "HI"
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_message))

app = Flask(__name__)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    app.run()