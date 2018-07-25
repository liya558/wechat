#!/usr/bin/env python
# coding:utf-8
###V1-2018-05-16###
#####################引入库#####################
import sys,time
import urllib2,json,requests
###################初始配置#####################
sys.setdefaultencoding('utf-8')
#####################配置参数#####################
#一、微信参数
#企业微信通知人
#qy_wechart_user = 'user'
#企业微信认证URL
authentiaction_URL = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={0}&corpsecret={1}'
#企业微信发送消息URL
send_URL = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}"
#企业微信ID
corpid = 'wx*************'
#企业微信应用密钥
corpsecret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

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
    url = send_URL.format(qs_token)
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



#zabbix中使用方法。
#在zabbix报警媒介类型的脚本参数中定义，默认在此全部接收
#（下面是以1为收件人，2为通知信息处理方法，其它也全部发出。信息中有特殊符号时注意转义）。
def parameter():
        par = sys.argv[1:]
        if not sys.stdin.isatty():
                par.append(sys.stdin.read())
        return(par)
notify = parameter()
try:
    qy_wechart_user = notify[0]
    content = str(notify[1])
    for i in range(2,len(notify)):
        content += '\n'+notify[i]
    if __name__ == '__main__':
        send_msg(content)
except Exception as e:print(e)
