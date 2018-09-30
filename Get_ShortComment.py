# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:24:45 2018

@author:Eugene
"""

import os
import re
import time
import requests
import codecs
from bs4 import BeautifulSoup
import matplotlib.pyplot
import jieba
from collections import Counter

Url="https://movie.douban.com/subject/1292052/comments"

def OpenUrl(url):
    req = requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}).content
    return req
def Get_Comment(html):
    Comment_list= list()
    soup = BeautifulSoup(html,'lxml')
    comment = soup.find_all('span','short')
    for each in comment:
        Comment_list.append(str(each.string))
    if soup.find('div',attrs={'id':'paginator','class':'center'}):
        find_page = soup.find('div',attrs={'id':'paginator','class':'center'})
        Page=find_page.find_all('a')
        p = r'<a class="next" data-page="" href="(.*)">'
        find_page_detail = re.findall(p,str(Page))
        #print(str(Page))
        if find_page_detail :
            for a in find_page_detail:
                return Comment_list,Url+a
    return Comment_list,None

def Write_Text():
    url=Url
    with codecs.open('E:/Pics/Test.txt','w',encoding='utf8') as fo:
        while url:
            html = OpenUrl(url)
            ShortComment,url = Get_Comment(html)
            for each_line in ShortComment:
                fo.write(each_line)
        fo.close()
def Parse(txt):
    seg=jieba.cut(txt)
    freq_dict=dict()
    c=Counter()
    for word in seg:
        if len(word)>1 and word!="\r\n":
            c[word]+=1
    for (k,v) in c.most_common(100):
        freq_dict[k]=freq_dict.get(k,0)+v
        print("%s%s  %d"%(k,'&'*int(v/2),v))
    return freq_dict
def Draw(datas):
    for key in datas:
        plt.bar(key,datas[key])
    plt.legend()
    plt.xlabel("words")
    plt.ylabel("frequency of words")
    plt.show()
def Main():
    Write_Text()
    with codecs.open('E:/Pics/Test.txt','r',encoding='utf-8') as fr:
        txt=fr.read()
        Fre=Parse(txt)
        Draw(Fre)
if __name__=='__main__':
    Main()
    
    
