#!/usr/bin/env python
# coding:utf-8
###V2-2018-07-27###
#####################引入库#####################
import sys,time
import urllib2,json,requests
###################初始配置#####################
sys.setdefaultencoding('utf-8')
#####################配置参数#####################
authentiaction_URL = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={0}&corpsecret={1}'
send_URL = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}"
corpid = 'wx*************'
corpsecret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

class sendWechat():
    def __init__():
        self corpid = 'wx*************'
        self corpsecret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    def setting(self,corpid,corpsecret,aURL,sURL):
        pass

def get_token():
    corp_id = 'wxe3c6b2951a3ba8ce'
    corp_secret = 'Vks0za_0KyN3q2Ba8dRFv-WE5nhAdTwAHCeHCwpNBnyo'
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    carry ={'corpid':corp_id,'corpsecret':corp_secret}
    try:
        textmod = urllib.urlencode(carry)
        request = urllib2.Request(url+'?'+textmod)
        res = urllib2.urlopen(request).read()
        result = json.loads(res)
        if result.has_key('access_token'):
            return(result['access_token'])
        else:raise('获取Token错误：'+str(result['errmsg']))
    except Exception,e:print(e)

class Token(object):

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
