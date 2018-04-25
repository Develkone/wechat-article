import requests

URL = 'https://mp.weixin.qq.com/cgi-bin/appmsg'
headers = {
    'Cookie':'ua_id=XZzxBiEljKTrrv6EAAAAAFaP2vFbalSivaPnT-NZgtw=; mm_lang=zh_CN; pgv_pvi=3503939584; noticeLoginFlag=1; remember_acct=Dante805310424%40163.com; pgv_si=s8416270336; uuid=2e740d5bbb509d3dfbd97de6dae7c2a9; ticket=47158720a7155792ea51d84c015dd592b8201c94; ticket_id=gh_6629c2b945dd; cert=BFVPF0KFlC8MMDmLN95SN8upj5BJ9lZm; data_bizuin=3209823476; bizuin=3516043142; data_ticket=uqhR+mjpjL+3Ed/HIU7Ns+CGR/jekLGqjf2VPkIWilTA8kAJmQwi/gyI/wQaaSqP; slave_sid=ZGk0WEZTZVM3blhyTG91TlJTQXdBVWVfNUFhN1FfZWtBN3lTUVlvZWxxc0hXdWl0OVFGaXo1TXZNazBQX0dWbThydkw0U3VBM2hycXY0YWF5Z0ZOd2ZHQmt6VFhHY3Y1Wk5nUXR1MDhnbHZxRkdtMW03TjJhMVRvajNaVmJUdm1POFhNQTF4a0FhWXFMbFlT; slave_user=gh_6629c2b945dd; xid=a8456f559f0818239a9f56319b4256db; openid2ticket_o9ARSv5hvUybXhVuyTh22OG6ORNc=CDTkHUN/TQ/vVozX4li1+ZWKcdPNFmwG3mmdX7MmtOA=; webwx_data_ticket=gScF3coUJk0HWqcCfaN1aiPA; rewardsn=; wxtokenkey=777',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

def get_page(p):
    data = {
        'token':'1285266581',
        'lang':'zh_CN',
        'f':'json',
        'ajax':'1',
        'action':'list_ex',
        'begin':'{0}'.format(p*5),#  number表示从第number页开始爬取，为5的倍数，从0开始。如0、5、10……
        'count':'5',
        'query':'',
        'fakeid':'MzI5NTI4NTM0Nw==',#  fakeid是公众号独一无二的一个id，等同于后面的__biz
        'type':'9'
    }
    content_json = requests.get(URL, headers=headers, params=data).json()
    return content_json['app_msg_list']
