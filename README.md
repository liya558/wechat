#更新于2018-07-25

#Wechat通知脚本说明。
#Python依赖库urllib2,urllib3,json,requests,sys,time
#脚本编码utf-8
#此脚本发送消息类型为文本。

#关键参数

#企业ID
#corpid = "wxe****************"

#企业微信应用密钥。
#corpsecret = "Vk*****************************************"

#企业收件用户，可使用用户名或者组名，多个收信人以“|”符号隔开。
#qy_wechart_user = '企业用户名'

#企业微信认证URL，如微信不更新及不用更改，后面携带的二个参数分别为企业微信ID和企业应用密钥。
#authentiaction_URL = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={0}&corpsecret={1}'

#企业微信发送消息URL，后面携带一个通过认证获取的Token密钥。
#send_URL = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={0}"

#发送内容格式参见企业微信开发者文档。  https://work.weixin.qq.com/api/doc#10012

#zabbix中使用方法。
#在zabbix报警媒介类型的脚本参数中定义，默认在此全部接收
#（下面是以1为收件人，2为通知信息处理方法，其它也全部发出。信息中有特殊符号时注意转义）。

#def parameter():
#        par = sys.argv[1:]
#        if not sys.stdin.isatty():
#                par.append(sys.stdin.read())
#        return(par)
#notify = parameter()
#try:
#    qy_wechart_user = notify[0]
#    content = str(notify[1])
#    for i in range(2,len(notify)):
#        content += '\n'+notify[i]
#    if __name__ == '__main__':
#        send_msg(content)
#except Exception,e:print(e)