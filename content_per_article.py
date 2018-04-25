import requests
from bs4 import BeautifulSoup
import content_per_page
import time
import pymysql
from database import Mysql

def get_url_title(p):
    global x #计算每一页有多少篇文章
    x = 0
    id = []
    title = []
    subtitle = []
    summary = []
    content = []
    picurl = []
    rid = ''
    author = []
    create_time = []
    public_time = []
    update_time = []
    isanonymous = ''
    content_imgs = []
    city = ''
    Page_con = content_per_page.get_page(p)
    connDB1 = Mysql.connDB()
    Mysql.exeSearch(connDB1[1])
    aids = connDB1[1].fetchall()
    for item in Page_con:
        res = requests.get(item['link'])
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'lxml')

        if (item['aid'],) in aids or soup.select('#post-user') == []: #判断要插入的数据是否已经存在数据库中或者要抓取的内容是否存在
            author.append('')
            time.sleep(1)
            continue
        else:
            id.append(item['aid'])

            title.append(item['title'].replace('"','”'))

            subtitle = title

            summary.append(item['digest'].replace('"','”'))

            content.append(pymysql.escape_string('\n'.join(str(s) for s in soup.select('p')[2:-6])))

            picurl.append(item['cover'])

            rid = '0'

            author.append(soup.select('#post-user')[0].text)

            if soup.select('#post-date') == []:
                create_time.append(soup.select('#publish_time')[0].text)
            else:
                create_time.append(soup.select('#post-date')[0].text)

            public_time = create_time

            update_time.append(item['update_time'])

            isanonymous = 'No'

            n = 0
            content_img = []
            while n < len(soup.select('img')):
                if soup.select('img')[n].has_attr("data-src"):
                    content_img.append(soup.select('img')[n]['data-src'])
                    n+=1
                else:
                    n+=1
            content_imgs.append(';'.join(content_img))

            city = 'Macheng'
            x+=1
            time.sleep(5)
    return id,title,subtitle,summary,content,picurl,rid,author,create_time,public_time,update_time,isanonymous,content_imgs,city
