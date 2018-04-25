import content_per_article
import time
from database import Mysql

connDB1 = Mysql.connDB()
Mysql.exeSearch(connDB1[1])
ids = connDB1[1].fetchall()
p = 0
n = 0
while p<=8:  #循环抓取每一页的内容，实际页数为篇p+1
    s = 0
    a = content_per_article.get_url_title(p)
    if a[0]!=[]:  #判断是否此页的所有文章都在数据库中
        while s<content_per_article.x:  #循环抓取一页中每篇文章的内容
            if (a[0][s],) in ids or a[7][s] == '':  #判断是否有文章已经存在数据库中或者要抓取的文章是否有内容
                s += 1
                continue
            else:
                sql = "INSERT INTO xungen(id,title,subtitle,summary,content,picurl,rid,author,create_time,public_time,update_time,isanonymous,content_imgs,city)VALUES"
                sql1 = sql + '("' + str(a[0][s]) + '","' + str(a[1][s]) + '","' + str(a[2][s]) + '","' + str(a[3][s]) + '","' + str(a[4][s]) + '","' + str(a[5][s]) + '","' + str(a[6]) + '","' + str(a[7][s]) + '","' + str(a[8][s]) + '","' + str(a[9][s]) + '","' + str(a[10][s]) + '","' + str(a[11]) + '","' + str(a[12][s]) + '","' + str(a[13]) + '")'
                Mysql.exeUpdate(connDB1[0],connDB1[1],sql1)
                s+=1
                n+=1
                print('Already upload {0} articles'.format(n))
        p+=1
        time.sleep(5)
    else:
        time.sleep(5)
        p+=1
Mysql.connClose(connDB1[0],connDB1[1])
