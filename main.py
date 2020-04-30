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
    MessageEvent, JoinEvent, TextMessage, TextSendMessage, ImageSendMessage, VideoSendMessage, TemplateSendMessage
)
from handout import handout
from table import timetable
import datetime
from wiki_search import wiki_api
import os

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


@handler.add(JoinEvent)
def handle_join(event):
    newcoming_text = "謝謝邀請我這個機器來至此群組！！我會盡力為大家服務的\n\n🆕🆕 目前功能:\n\n👉 講義:  小幫手顯示講義\n\n👉 查詢指定時間課表: 小幫手X月XX日課表 \n\n👉 明日課表:  小幫手明天的課表\n\n👉 昨日課表:  小幫手昨天的課表\n\n👉 維基百科:  小幫手wiki搜尋(keywords) \n\n👉 Help   :  \help"
    line_bot_api.reply_message(
        event.reply_token, TextMessage(text=newcoming_text))

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_text = event.message.text
    print(get_text[:6])
    if  get_text == '講義':

        #User_ID = event.source.user_id
        #line_bot_api.reply_message(event.reply_token, User_ID)
        line_bot_api.push_message(event.source.user_id, TemplateSendMessage(
            alt_text="課程講義", template=handout.handout()))
        print('Reply User ID =>' + event.source.user_id)

    elif get_text[:9] == '小幫手wiki搜尋':
        search_text = get_text[9:]
        url = wiki_api.wiki_search(search_text)
        line_bot_api.reply_message(
        event.reply_token, TextMessage(text='以下是小幫手幫您找到的網址:\n\n👉👉   '+str(url)))

    elif get_text == '小幫手顯示講義':
        #Group_ID = source.group_id
        #line_bot_api.reply_message(event.reply_token, Group_ID)
        line_bot_api.push_message(event.source.group_id, TemplateSendMessage(
            alt_text="課程講義", template=handout.handout()))
    
    elif get_text == '小幫手明天的課表' or get_text[:6] == '小幫手明天上':
        a = datetime.date.today() + datetime.timedelta(days=1)
        tmr_month = a.month
        tmr_day = a.day
        class_list = timetable.timetable(tmr_month, tmr_day)

        if len(class_list) == 3:

            content1 = class_list[0]
            content2 = class_list[1]
            content3 = class_list[2].strip('\n')

            timetable_text = "🆕 新消息:\n\n✏️ 明天課程:  {}\n\n✏️ 提醒事項:  {}\n\n✏️ 夜輔:      {}              ".format(
                content1, content2, content3)
            line_bot_api.push_message(
                event.source.group_id, TextMessage(text=timetable_text))

        elif len(class_list) == 2:
            content1 = class_list[0]
            content2 = class_list[1]
            timetable_text = "🆕 新消息:\n\n✏️ 明天課程:  {}\n\n✏️ 提醒事項:  {}\n\n✏️ 夜輔:         ❌".format(
                content1, content2)
            line_bot_api.push_message(
                event.source.group_id, TextMessage(text=timetable_text))
        elif len(class_list) == 1:
            content1 = class_list[0]

            timetable_text = "🆕 新消息:\n\n✏️ 明天課程:     ❌ \n\n✏️ 提醒事項:  {}\n\n✏️ 夜輔:     ❌              ".format(
                content1)
            line_bot_api.push_message(
                event.source.group_id, TextMessage(text=timetable_text))
    
    elif get_text == '小幫手昨天的課表' or get_text[:6]=='小幫手昨天上':
        a = datetime.date.today() + datetime.timedelta(days=-1)
        tmr_month = a.month
        tmr_day = a.day
        class_list = timetable.timetable(tmr_month, tmr_day)

        if len(class_list) == 3:

            content1 = class_list[0]
            content2 = class_list[1]
            content3 = class_list[2].strip('\n')

            timetable_text = "🆕 新消息:\n\n✏️ 昨天課程:  {}\n\n✏️ 提醒事項:  {}\n\n✏️ 夜輔:      {}              ".format(
                content1, content2, content3)
            line_bot_api.push_message(
                event.source.group_id, TextMessage(text=timetable_text))

        elif len(class_list) == 2:
            content1 = class_list[0]
            content2 = class_list[1]
            timetable_text = "🆕 新消息:\n\n✏️ 昨天課程:  {}\n\n✏️ 提醒事項:  {}\n\n✏️ 夜輔:         ❌".format(
                content1, content2)
            line_bot_api.push_message(
                event.source.group_id, TextMessage(text=timetable_text))
        elif len(class_list) == 1:
            content1 = class_list[0]

            timetable_text = "🆕 新消息:\n\n✏️ 昨天課程:     ❌ \n\n✏️ 提醒事項:  {}\n\n✏️ 夜輔:     ❌              ".format(
                content1)
            line_bot_api.push_message(
                event.source.group_id, TextMessage(text=timetable_text))
 

    elif get_text[:3] == '小幫手' and get_text[8:10]=='課表':
        month = int(get_text[3])
        day = int(get_text[5:7])
        print("get {} 月 {} 日".format(month,day))
        
        class_list = timetable.timetable(month,day)

        if len(class_list) == 3:

            content1 = class_list[0]
            content2 = class_list[1]
            content3 = class_list[2].strip('\n')

            timetable_text = "🆕 新消息: {} 月 {} 日\n\n✏️ 課程:  {}\n\n✏️ 提醒事項:  {}\n\n✏️ 夜輔:      {}              ".format(
                month, day, content1, content2, content3)
            line_bot_api.push_message(
                event.source.group_id, TextMessage(text=timetable_text))

        elif len(class_list) == 2:
            content1 = class_list[0]
            content2 = class_list[1]
            timetable_text = "🆕 新消息: {} 月 {} 日\n\n✏️ 課程:  {}\n\n✏️ 提醒事項:  {}\n\n✏️ 夜輔:         ❌             ".format(
                    month, day, content1, content2)
            line_bot_api.push_message(
                event.source.group_id, TextMessage(text=timetable_text))

        elif len(class_list) == 1:
                    content1 = class_list[0]

                    timetable_text = "🆕 新消息: {} 月 {} 日\n\n✏️ 課程:     ❌ \n\n✏️ 提醒事項:  {}\n\n✏️ 夜輔:     ❌              ".format(
                            month, day, content1)
                    line_bot_api.push_message(
                        event.source.group_id, TextMessage(text=timetable_text))












    elif  event.message.text == '/help':
        help_text = r"🆕🆕 目前功能:\n\n👉 講義:  小幫手顯示講義\n\n👉 查詢指定時間課表: 小幫手X月XX日課表\n\n👉明日課表:  小幫手明天的課表\n\n👉 昨日課表:  小幫手昨天的課表\n\n👉 維基百科:  小幫手wiki搜尋(keywords) \n\n👉 Help   :  \help"
        line_bot_api.reply_message(event.reply_token, TextMessage(text=help_text))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 88)))
