# -*- coding: utf8 -*-

#####----------------------------------------------------------------#####
#####                                                                #####
#####   Author:Tencent Cloud TAM Team                                #####
#####   Just for VIVO test on Jan.2020                               #####
#####                                                                #####
#####----------------------------------------------------------------#####

import logging
import requests, json
import sys

#控制log输出级别
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)

#定义测试目标地址
target_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=1e06913c-a2a3-44c6-8440-b33d8240d2fa"

def main_handler(event, context):
    logger.info("starting to send message to VIVO from main handler")

    #判断请求是否从API网管传递，并把body json赋值给告警内容
    if "body" in event.keys():
        AlarmContent = event['body']
        logger.info (str(len(AlarmContent.decode('utf-8'))))
        logger.info ('告警内容: '+ AlarmContent)
        send_msg(AlarmContent)

    else:
        return {
                "isBase64Encoded": False,"statusCode": 410,"headers": {"Content-Type": "text", "Access-Control-Allow-Origin": "*"},"body": "Error: AlarmContent is null"
            }

    return {"statusCode": 200,
        "headers": {"Content-Type": "text", "Access-Control-Allow-Origin": "*"
        }}#return

def send_msg(AlarmContent):
    #发送告警内容企业微信机器人测试

    data = json.dumps({"msgtype": "text", "text": {"content": AlarmContent}})
    r = requests.post(target_url, data, auth=('Content-Type', 'application/json'))
    print(r.json)

    #发送给vivo
    #定义VIVO告警地址
    vivo_url = "https://alarm.vivo.com.cn/api/alarms/save?appName=cdn&eventCode=001&secretKey= Hj7qq2UGbAv1wG99&content=" + AlarmContent
    response = requests.get(url=vivo_url).text

    print("vivo_reponse" + response)
    print("vivo_url" + vivo_url)
