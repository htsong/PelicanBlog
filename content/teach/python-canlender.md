Title: 用 Python （无模块）打印当月日历
Date: 2020-09-22 08:10
Category: 教学

## 公元之由来

公元，即公历纪年法，是一种源自于西方社会的纪年方法。原称基督纪元，又称西历或西元，是由意大利医生兼
哲学家阿洛伊修斯·李箓时 (Aloysius Lilius) 对儒略历加以改革而制成的一种历法 —— 格里高利历，或简称
格里历。1582年，时任罗马教皇的格列高利十三世 (Gregory XIII) 予以批准颁行。

<div align=center>
  <img src="https://sh556.oss-cn-shanghai.aliyuncs.com/images/aw_wm/69/Eo3jSd634412e22.jpg" 
    width = "300" height = "400" />
  <p align="center">Pope Gregory XV (not XIII),1591-1666</p>
</div>

公历纪年以耶稣诞生之年作为纪年的开始。在儒略历与格里高利历中，在耶稣诞生之后的日期，称为主的年份 (Anno 
Domini, A.D.)（拉丁）。而在耶稣诞生之前，称为主前 (Before Christ, B.C.)。但是现代学者为了淡化其宗
教色彩以及避免非基督徒的反感而多半改称用“公元” (Common Era, C.E.) 与“公元前” (Before the 
Common Era, B.C.E.) 的说法。

辛亥革命爆发后次年（1912年），当时的中华民国政府采用公历作为国历，纪年方面，公元纪年法与民国纪年法并
行。1949年9月27日，经过中国人民政治协商会议第一届全体会议通过，新成立的中华人民共和国使用国际社会上
大多数国家通用的公历和公元作为历法与纪年。

## 格里历介绍

格里历 [参考文献2] 的历年平均长度为365.2425日，接近平均回归年的365.242199074日，即每3300年误差一日，也
更接近春分点回归年的365.24237日，即每8000年误差一日；而儒略历的历年为365.25日，每128年就误差一日。到 
1582 年时，儒略历的春分日（3月21日）与地球公转到春分点的实际时间已相差10天，令到所算出的复活节日期与实际的
春分的间隔逐渐增大，

因此，格里历开始实行时，将儒略历1582年10月4日星期四的次日，为格里历1582年10月15日星期五，即有10天被删除，
但原星期的周期保持不变。格里历的纪年沿用儒略历，当年定历以耶稣诞生年开始起算（但考证是公元前4年出生，但
此记数法沿用至今），称为“公元”。

## 蔡勒公式 (Zeller's congruence)

蔡勒公式（Zeller's congruence），是一种计算任何一日属一星期中哪一日的算法，由德国数学家克里斯提安·蔡勒推算出来。

![Zeller's congruence 1](https://wikimedia.org/api/rest_v1/media/math/render/svg/c65e11cd656b95b753e220dbec1d7441d572aa7e)

or 

![Zeller's congruence 2](https://wikimedia.org/api/rest_v1/media/math/render/svg/b671ee256387a51343ba0c42524286a25ece7a41)

公式都是基于公历的置闰规则来考虑，公式中的符号含义如下：

* w：星期（计算所得的数值对应的星期：0-星期日；1-星期一；2-星期二；3-星期三；4-星期四；5-星期五；6-星期六）；
* c：年份前两位数；
* y：年份后两位数；
* m：月（m的取值范围为3至14，即在蔡勒公式中，某年的1、2月要看作上一年的13、14月来计算，比如2003年1月1日要看作2002年的13月1日来计算）；
* d：日；
* [　]：称作高斯符号，代表向下取整，即，取不大于原数的最大整数；
* mod：取余（这里代表括号里的答案除以7后的余数）。

如果对此公式的由来充满好奇，请看[参考文献4]，了解[蔡勒公式及其推导](https://zhuanlan.zhihu.com/p/79290515)。

## 代码实现 (Python3)

```python3
# 输出日历， 其关键是当月首日星期几
# 参考： 
# 计算任何一天是星期几的几种算法， https://blog.csdn.net/luoyayun361/article/details/54881835
# Zeller’s Congruence | Find the Day for a Date, https://www.geeksforgeeks.org/zellers-congruence-find-day-date/

def Zellercongruence(year, month, day) : 
    if (month <= 2) : month += 12; year -= 1
    w = (day + 13*(month+1)// 5 + year%100 + year%100//4 + year//100//4 + year//100*5) % 7
    return (w+5)%7, {0:"Sat", 1:"Sun", 2:"Mon", 3:"Tue", 4:"Wed", 5:"Thu", 6:"Fri"}[w]

print(Zellercongruence(2020, 9, 1))
# (1, 'Tue')
```

## 小结

有了上述函数，再打印月历就比较简便的了，这次先说到这里。

**（续）@20200930**

2020秋的《应用数据科学》课上庞耀彬（18级市场营销班）用Python3写的月历程序，附上代码：

```python3

def Zellercongruence(year, month) : 
    if (month <= 2) : month += 12; year -= 1
    w = (1 + 13*(month+1)// 5 + year%100 + year%100//4 + year//100//4 + year//100*5) % 7
    return w

is_leap_year = lambda year:year % 4 ==0 and year % 100 != 0 or year % 400 ==0
days = lambda year, month: 31 if month in (1,3,5,7,8,10,12) else 30 if month in (4,6,9,11) else 29 if month == 2 and is_leap_year(year) else 28

year = int(input('输入年份：')) 
month = int(input('输入月份'))
print('  周六 周日 周一 周二 周三 周四 周五\n' + '     '* Zellercongruence(year,month), end='')
for num in range(1, days(year,month)+1):
    print('%5d' % num, end ='')
    if (Zellercongruence(year,month)+num) % 7 ==0:print('\n')
```


----------
[参考文献]

1. 公元，[EB/OL] https://baike.baidu.com/item/%E5%85%AC%E5%85%83/17855?fromtitle=格里高利历，20200922

2. 格里历，[EB/OL] https://zh.wikipedia.org/wiki/，20200922

3. 蔡勒公式，[EB/OL] https://zh.wikipedia.org/wiki/蔡勒公式，20200922

4. 蔡勒(Zeller)公式及其推导，https://zhuanlan.zhihu.com/p/79290515，20190822

5. 怎样计算某一天是星期几与历法中的陷阱，[DB/OL] https://www.bilibili.com/video/BV1JV411f7fM，20200401

6. 历法的故事，[DB/OL] https://www.bilibili.com/video/BV15b41147Ao, 20190324

7. 五分钟图解公元纪年历史，[EB/OL] https://www.bilibili.com/video/BV1NJ411a779, 20191229

8. 时间法则：历法的历史进程，回到2049，[DB/OL] https://www.bilibili.com/video/BV1Qx411U7hh, 20170428

9. Pope Gregory XV - Guercino (Giovanni Francesco Barbieri) (Italian (Bolognese), 1591 - 1666),世之歌， https://www.shizhige.com/artwork/4155/pope-gregory-xv, 20200922
