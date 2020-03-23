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
    get = TextSendMessage(text=event.message.text)
    
    if(get == 'd'):
        #print("Image Carousel")
        message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/IbbQ1xo.jpg',
                    action=MessageTemplateAction(
                        label='postback1',
                        text='postback text1'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/VQpvhMX.jpg',
                    action=MessageTemplateAction(
                        label='postback2',
                        text='postback text2'
                    )
                )
            ]
        )
        )
    if(get == 'Drama'):
        #print("Image Carousel")
        message = TemplateSendMessage(
        alt_text = 'Drama for mobile.(updated irregularly)',
        template = ImageCarouselTemplate(
            columns = [
                ImageCarouselColumn(
                    image_url = 'https://img.edwardmovieclub.com/uploads/20200117230248_9.jpg',
                    action = URITemplateAction(
                        label = '不完美的正義',
                        uri = 'http://www.777drama.com/vod/14/18320play.html?18320-1-3'
                    )
                ),
                ImageCarouselColumn(
                    image_url = 'https://pic.pimg.tw/q36genius/1571127285-4176158080_wn.jpg',
                    action = URITemplateAction(
                        label = '惡鄰布局',
                        uri = 'http://www.5goup.com/user/getmovie/show/5c078cc7d55812466c8887c7'
                    )
                ),
                ImageCarouselColumn(
                    image_url = 'https://img.17365i.com/Uploads/vod/2018-04-09/5acade40d1202.webp',
                    action = URITemplateAction(
                        label = '噤界',
                        uri = 'https://pttplay.com/vod-play-id-RjlB-src-1-num-6x.html'
                    )
                ),
                ImageCarouselColumn(
                    image_url = 'https://media.putyourself.in/pysiuploads/2019/10/event-the-garden-of-evening-mists-1118.jpg',
                    action = URITemplateAction(
                        label = '夕霧花園',
                        uri = 'http://www.777drama.com/vod/14/19322play.html?19322-1-4'
                    )
                )
            ]
        )
        )
    
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    app.run()
