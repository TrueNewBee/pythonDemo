#!/usr/bin/env python
#!--*--coding:utf-8 --*--
#!@Time    :2018/7/6 12:13
#!@Author   TrueNewBee
#爬取并批量下载网易云歌单
#根据URL下载音乐  https://music.163.com/#/playlist?id=2269661190

import requests
import time
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


#1.获取页面源代码
def get_page():
    """获取网页源代码(选择自己喜欢的网易云歌单连接)"""
    # 去掉原链接里面的   #/
    url ="https://music.163.com/playlist?id=2269661190"
    #请求头
    headers ={
        'Host':'music.163.com',
        'Referer':'https://music.163.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    #获取网页源代码
    res = requests.get(url,headers=headers).text
    #url ="https://music.163.com/playlist?id=2269661190"
    #创建对象  解析网页
    r = BeautifulSoup(res,"html.parser")
#2.获取ID
    music_dict = {}
    #找源代码中的a标签
    result = r.find("ul",{'class':'f-hide'}).find_all('a')
    for music in result:
        music_id = music.get('href').strip("/song?id=")#去掉/song?id
        music_name = music.text #获取其中的文字
        music_dict[music_id] = music_name
    return music_dict


#3.下载歌曲
def download_song(music_dict):
    """下载音乐"""
    for song_id in music_dict:
        song_url = "http://music.163.com/song/media/outer/url?id=%s.mp3"%song_id
        #下载地址(地址填写自己的地址)
        path="C:\\Users\Administrator\Desktop\网易云音乐\\%s.mp3"%music_dict[song_id]#通过键值对来查找歌曲名字
        #下载音乐  urlretriver (地址  路径)
        time.sleep(1)
        urlretrieve(song_url,path)
        print("正在下载%s"%music_dict[song_id])


def  main():
    music_dict =get_page()
    download_song(music_dict)

if __name__ == '__main__':
    main()


