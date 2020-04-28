import configparser
import json
from flask import Flask, request, abort
import logging
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
from linebot.models import (
    MessageEvent, JoinEvent,LeaveEvent, TextMessage, TextSendMessage, ImageSendMessage, VideoSendMessage, LocationSendMessage, StickerSendMessage, TemplateSendMessage
)
import handout
from linebot.models import TemplateSendMessage, CarouselTemplate, CarouselColumn, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction
app = Flask(__name__)
config = configparser.ConfigParser()
config.read('config.ini')
token = config.get('LINE', 'CHANNEL_TOKEN')
secret = config.get('LINE', 'CHANNEL_SECRET')



line_bot_api = LineBotApi(token)
handler = WebhookHandler(secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.setLevel(logging.INFO)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


#line_bot_api.push_message('C52d8081df27ed6ed322409634f4933db', TemplateSendMessage(alt_text="課程講義電子檔", template=handout.handout_carouse()))            
#line_bot_api.push_message('C52d8081df27ed6ed322409634f4933db', TemplateSendMessage(alt_text="課程講義1", template=handout.handout1()))
#line_bot_api.push_message('C52d8081df27ed6ed322409634f4933db', TemplateSendMessage(alt_text="課程講義2", template=handout.handout2()))


#C52d8081df27ed6ed322409634f4933db
#https://docs.google.com/spreadsheets/d/1qTkccFsNRy8IJLFEDK2ty-GB24Np1cu7avLoB0uZZUs/edit#gid=1865763997

handout_icon1 = "https://image.flaticon.com/icons/svg/1061/1061447.svg"
handout_icon2 = 'https://upload.wikimedia.org/wikipedia/commons/f/f1/Books_Flat_Icon_Vector.svg'
handout_icon3 = 'https://banner2.cleanpng.com/20180407/jpq/kisspng-book-flat-design-books-5ac984c5e9ef33.3004996215231561659582.jpg'
book_icon = "https://i.pinimg.com/236x/2c/fc/93/2cfc93d7665f5d7728782700e50596e3--icons.jpg"
timetable_url = "https://docs.google.com/spreadsheets/d/1qTkccFsNRy8IJLFEDK2ty-GB24Np1cu7avLoB0uZZUs/edit#gid=1865763997"
html_url = "https://drive.google.com/open?id=1bXnZtE9LyhTV80IPttCYJ0Ro5jOmIaaJ"
python_basic_url = 'https://drive.google.com/open?id=1tcBxB6_5h5nLIu40cKuBvtzviGKjOw0M'
linux_url = 'https://drive.google.com/open?id=1N1GmA9-tYUSTK8AWCERfplyBQoKCe0BD'
pyetl_url = 'https://drive.google.com/open?id=1HyBsyshzSuBQtKZYrH09vuloWmlLv-v0'
pyai_url = 'https://drive.google.com/open?id=1Xp-i_7ltQBo2r-luiF4Rp-4vfnLgck52'
data_mining_url = 'https://drive.google.com/open?id=1r45ik4uD2TYr7xrNp5c9VfrkXEAVMSLX'
nosql_url = 'https://drive.google.com/open?id=1VeDkM1g3MYNaFUDQ8O_m4lF43HT-w_1R'
text_mining_nlu_url = 'https://drive.google.com/open?id=1puNXOTh1DoArz_20eV748D1OpvmdXvNR'
hadoop_url = 'https://drive.google.com/open?id=10mZ5iis0aCI7S4AzbFOAlEXW4FOdr5dW'
kafka_url = 'https://drive.google.com/open?id=1ZfRDO713xLXHSVrMXUWOYXlep4kYXRW1'

handout_carouse = CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=handout_icon1,
                    title='課程講義 page 1',
                    text='請選擇您要的講義',
                    actions=[
                    URITemplateAction(
                        label='網頁概論',
                        uri=html_url
                    ),
                    URITemplateAction(
                        label='Python 基礎',
                        uri=python_basic_url
                    ),
                    URITemplateAction(
                        label='Linux',
                        uri=linux_url
                    ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=handout_icon2,
                    title='課程講義 page 2',
                    text=' ',
                    actions=[
                    URITemplateAction(
                        label='PyETL',
                        uri=pyetl_url
                    ),
                    URITemplateAction(
                        label='PyAI',
                        uri=pyai_url
                    ),
                    URITemplateAction(
                        label='Data Mining(含R語言)',
                        uri=data_mining_url
                    ),


                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=handout_icon3,
                    title='課程講義 page 3',
                    text=' ',
                    actions=[
                    
                    URITemplateAction(
                        label='NoSQL',
                        uri=nosql_url
                    ),
                    
                    URITemplateAction(
                        label='Text Mining + NLU',
                        uri=text_mining_nlu_url
                    ),
                    
                    URITemplateAction(
                            label='Kafka',
                            uri=kafka_url
                    ),


                    ]
                )
                
                ]
            )


group_id_list = []

@handler.add(JoinEvent)
def handle_join(event):
    newcoming_text = "謝謝邀請我這個機器來至此群組！！我會盡力為大家服務的～"
    group_id = event.source.group_id
    group_id_list.append(group_id)
    line_bot_api.reply_message(
            event.reply_token,
            TextMessage(text=newcoming_text)
        )
    line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(alt_text="Template Example", template=button_template_message)
        )
    line_bot_api.push_message('C52d8081df27ed6ed322409634f4933db', TemplateSendMessage(alt_text="Template Example", template=button_template_message))
    print("JoinEvent =", JoinEvent)
    print(group_id_list,'\n\n', group_id)
    

@handler.add(LeaveEvent)
def handle_leave(event):
    group_id = event.source.group_id
    
    try:
        group_id_list.remove(group_id)
        print("leave Event =", event)
        print("我被踢掉了QQ 相關資訊", event.source)
    except:
        pass

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event.message.text)
    if event.message.text == 'ID?' or event.message.text == 'id?':

        User_ID = TextMessage(text=event.source.user_id)

        line_bot_api.reply_message(event.reply_token, User_ID)
        line_bot_api.push_message('C52d8081df27ed6ed322409634f4933db', TemplateSendMessage(alt_text="Template Example", template=handout.handout_carouse()))
        print ('Reply User ID =>' + event.source.user_id)
        
    elif event.message.text == 'GroupID?':
        Group_ID = TextMessage(text=event.source.group_id)
        line_bot_api.reply_message(event.reply_token, Group_ID)
        line_bot_api.push_message('C52d8081df27ed6ed322409634f4933db', TemplateSendMessage(alt_text="Template Example", template=handout.handout_carouse()))
        print ('Reply Group ID =>' + event.source.group_id)
    else:
        pass
#line_bot_api.push_message( 'C52d8081df27ed6ed322409634f4933db',TextSendMessage(text="Hello world"))
    
    


if __name__ == "__main__":
    app.run(port='8000', debug=True)