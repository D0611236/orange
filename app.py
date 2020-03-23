from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('zE1MsJwQJlGNJKDKJ5wO8wgjOS+9YP0DXQp2jHQp2wS0ii+MuGhSJdQjdypF8qJPsRdGpQGvrwxQ483M/PZXLq0RFCvzKGadfxAbE+I+EQb2kFR39YRanwCyKqlDG+CfvV1y66GY+MBMeR/pFKuDkgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('2093c6299585fbbc306fc82570e55755')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    app.run()
