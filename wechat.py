#!/usr/bin/env python
# coding:utf-8
###V1-2018-05-16###
#####################引入库#####################
import sys,time
import urllib2,urllib3,json,requests
###################初始配置#####################
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
reload(sys)
sys.setdefaultencoding('utf-8')
#####################配置参数#####################
#一、微信参数
#企业微信通知人
qy_wechart_user = 'liya'
#企业微信认证URL
authentiaction_URL = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={0}&corpsecret={1}'
#企业微信发送消息URL
send_URL = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}"
#企业微信ID
corpid = "wxe****************"
#企业微信应用密钥
corpsecret = "Vk*****************************************"

#######################获取微信接口认证密钥（Token)#####################
class Token(object):
    def __init__(self, corpid, corpsecret):
        self.baseurl = authentiaction_URL.format(corpid, corpsecret)
        self.expire_time = sys.maxint

    def get_token(self):
        if self.expire_time > time.time():
            request = urllib2.Request(self.baseurl)
            response = urllib2.urlopen(request)
            ret = response.read().strip()
            ret = json.loads(ret)
            if 'errcode'!= 0 in ret.keys():
                print >> ret['errmsg'], sys.stderr
                sys.exit(1)
            self.expire_time = time.time() + ret['expires_in']
            self.access_token = ret['access_token']
        return self.access_token

##########################发送微信消息########################
def send_msg(content):
    qs_token = Token(corpid=corpid, corpsecret=corpsecret).get_token()
    url = send_URL.format(
        qs_token)
    payload = {
        "touser": qy_wechart_user,
        "msgtype": "text",
        "agentid": "1",
        "text": {
                    "content": "{0}".format(content)
        },
        "safe": "0"
    }
    requests.post(url, data=json.dumps(payload, ensure_ascii=False) ,verify=False)