#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
from web_crawler import *
from web_crawler2 import *
from crawler import *
from config import *
from find_tld import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
from flask import Flask, request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from liffpy import LineFrontendFramework as LIFF, ErrorResponse

#======python的函數庫==========

liff_api = LIFF(CHANNEL_ACCESS_TOKEN)
#add_liff = liff_api.add(view_type="compact",view_url="https://pypi.org/project/liffpy/")

app = Flask(__name__,template_folder='templates')
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
# Channel Secret
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/share_vedio")
def share_vedio():
    return render_template("./share_vedio.html")



# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    print(body)
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
    msg = event.message.text
    if '最新合作廠商' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新活動訊息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '旋轉木馬' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    elif 'YT,' in msg:
        keyword = msg.split(',')[1]
        message = youtube_vedio_parser(keyword)
        line_bot_api.reply_message(event.reply_token, message)
    elif '測試' in msg:
        message = TextSendMessage(text=find_a_tag())
        line_bot_api.reply_message(event.reply_token, message)
    elif '系列文章' in msg:
        message = TextSendMessage(text=IT_helper())
        line_bot_api.reply_message(event.reply_token, message)
    elif '1' in msg:
        message = TextSendMessage(text="測試")
        line_bot_api.reply_message(event.reply_token, message)
    elif 'tld' in msg:
        url = "https://maplestory.beanfun.com/main"
        message = TextSendMessage(text=find_tld(url))
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)
    

@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
