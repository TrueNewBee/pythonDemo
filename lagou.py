# /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/9/23 20:22 
# @Author : TrueNewBee

import requests
import json
import time

# 网站
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%88%90%E9%83%BD&needAddtionalResult=false&isSchoolJob=1'

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'WEBTJ-ID=20180918181741-165ec2f83d743-0ee41db9c69e0e-6e1f147a-2073600-165ec2f83d95d1; _ga=GA1.2.1559975793.1537265862; user_trace_token=20180918181742-13d9fe9b-bb2c-11e8-baf2-5254005c3644; LGUID=20180918181742-13da0831-bb2c-11e8-baf2-5254005c3644; JSESSIONID=ABAAABAAAFCAAEG0FCA6542C1D06F1F470B0A7189B8AD06; index_location_city=%E6%88%90%E9%83%BD; TG-TRACK-CODE=index_search; _gid=GA1.2.1437892044.1537705170; LGSID=20180923201929-eb4f9cfb-bf2a-11e8-bb56-5254005c3644; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DXpamso_IxFbfBezXbGYWv8-vI3sYyGf67_89jrtjXQK%26wd%3D%26eqid%3Da27f010200061c48000000025ba784cc; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1537265862,1537265872,1537354446,1537705170; LGRID=20180923201940-f1eea38b-bf2a-11e8-bb56-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1537705181; SEARCH_ID=baf28c394763403c8afc3fc36dce76a4',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_python?isSchoolJob=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
}

for i in range(1, 5):
    data = {
        'first': 'true',
        'pn': i,
        'kd': 'python',
    }
    html = requests.post(url, data=data, headers=headers)
    jsonData = html.json()['content']['positionResult']['result']
    for item in jsonData:
        time.sleep(1)
        print('*'*80)
        print(item['companyFullName'])
        print(item['workYear'])
        print(item['positionName'])
        print(item['salary'])
        print(item['secondType'])
