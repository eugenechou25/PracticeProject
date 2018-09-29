# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 08:33:06 2018
"""
import os
import urllib.request
from bs4 import BeautifulSoup
import matplotlib.pyplot
import jieba

def OpenUrl(url):

    response = urllib.request.Request(url)
    
    #发送请求
    
    response.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
    print("Opening url")
    
    page = urllib.request.urlopen(response)
    
    #获取并解码
    
    html = page.read().decode("utf-8")
    
    print("Html got....")
    
    return html
    
    
def Parse_Word(html):
    #beautifulsoup进行处理
    
    soup = BeautifulSoup(html,'lxml')
    
    detail = soup.find('div',attrs={'id':'content'}) 
    
    #空列表用来存储爬取的内容
    
    DetailList = []
    
    for each in detail.find_all('p'):
    
        #返回的each是bs的一个对象，无法直接写入，进行字符串转换
        
        txtt = str(each.string)
        
        DetailList.append(txtt)
        
    print("begin to writing into file.....")
    
    for each_one in DetailList:
    
        with open('E:/Pics/Fir.txt','a') as fw:
        
            fw.write(each_one)
            
    print("done")
    
    
def Parse_Text(txt):

    #空字典存储词语及其词频
    
    frequency=dict()
    
    seg=jieba.cut(txt)
    
    c=Counter()
    
    for word in seg:
    
        if len(word)>1 and word!="\r\n"
        :
            c[word] +=1
            
    for (k,v) in c.most_common(100):
    
        frequency[k]=frequency.get(k,0)+v
        
        print("%s    %d"%(k,v))
    return frequency
    
    
    
def draw(datas):

    for key in datas.keys():
    
        plt.bar(key,datas[key])
        
    #画图函数
    
    plt.legend()
    
    plt.xlabel("word")
    
    plt.ylabel("frequency")
    
    plt.title("frequency of words")
    
    plt.show()
    
    
def main():

    url="http://www.xinhuanet.com/politics/19cpcnc/2017-10/27/c_1121867529.htm"
    
    Parse_Word(OpenUrl(url))
    
    with open('E:/Pics/Fir.txt','r') as fo:
    
        txt=fo.read()
        
        Parse_Text(txt)
        
        draw(Parse_Text(txt))
        
        
if __name__ == '__main__' :
    main()
    
    
    
