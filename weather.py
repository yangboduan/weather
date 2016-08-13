#-*-encoding:utf-8-*-
import urllib2 
import re 
import sys

mytype = sys.getfilesystemencoding()   

#从www.weather.com.cn获取html信息
response = urllib2.urlopen('http://m.weather.com.cn/mweather1d/101270101.shtml')  
weather_html = response.read().decode('utf-8').encode(mytype)

#从pm25.moji.com获取html信息
response = urllib2.urlopen('http://pm25.moji.com/53')  
moji_weather_html = response.read().decode("UTF-8").encode(mytype) 

#输出地理位置
moji_cityname=re.findall('<a href="javascript:;" id="cityname" class="btn">(.*?)</a>',moji_weather_html)
print u'地理位置 :'+moji_cityname[0].decode(mytype)

#输出车辆限行信息（分工作日和周末）
myItems_in_work_day = re.findall('<div class="wl">.*?<b>(.*?)</b>.*?<b>(.*?)</b>.*?<i class="lzy">(.*?)</i>',weather_html,re.S)

if ( myItems_in_work_day == [] ):
    #执行周末代码
    myItems_in_weekday = re.findall('<div class="wl">.*</span>\n(.*?)\n.*<i class="lzy">(.*?)</i>',weather_html,re.S)  
    if ( myItems_in_weekday[0][0].decode(mytype) == u'尾号限行不限行' ):
        print u'限行尾号 :不限行'.encode(mytype)
        print u'今日天气 :'+myItems_in_weekday[0][1].decode(mytype)
else:	
    #执行工作日的代码
    for myItems in myItems_in_work_day :
        print u'限行尾号 :'+myItems[0].decode(mytype)+u'和'+myItems[1]
        print u'今日天气 :'+myItems[2].decode(mytype)


#输出今日温度
moji_tep=re.findall('<div class="user-panel">.*?<div>.*?<span>(.*?)<span>.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?</div>',moji_weather_html,re.S)
for m in moji_tep:
	print u'今日温度 :'+m[2].decode(mytype)

#输出PM2.5指数和污染程度
moji_myItems = re.findall('<div class="map-air-temp">.*?<em>(.*?)</em><span>(.*?)</span>.*</div>',moji_weather_html,re.S)  
for n in moji_myItems:
	print u'PM2.5指数:'+n[0].decode(mytype)
	print u'污染程度 :'+n[1].decode(mytype).lstrip()

#输出温馨提示信息
moji_prompt=re.findall('<div class="map-air-time">.*?<p>.*?:(.*?)</p>',moji_weather_html,re.S)
print u'温馨提醒 :'+moji_prompt[0].lstrip().decode(mytype)

#输出发布时间
moji_air_time=re.findall('<div class="map-air-time">\n(.*?)\n.*?</div>',moji_weather_html,re.S)
print u'发布时间 :'+moji_air_time[0].decode(mytype).lstrip().replace(u'发布','')



#------------------------------------------------------------------------------------------------------------
#当地信息输出
response = urllib2.urlopen('http://pm25.moji.com')  
local_weather_html = response.read().decode("UTF-8").encode(mytype) 

local_cityname=re.findall('<div>.*?<span>(.*?)<span>',local_weather_html,re.S)
print '\n------------------------------------------------------------------------------------------\n'
print u'当地位置 :'+local_cityname[0].decode(mytype)

#输出今日温度
moji_tep=re.findall('<div class="user-panel">.*?<div>.*?<span>(.*?)<span>.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?</div>',local_weather_html,re.S)
for m in moji_tep:
	print u'今日温度 :'+m[2].decode(mytype)

#输出PM2.5指数和污染程度
moji_myItems = re.findall('<div class="map-air-temp">.*?<em>(.*?)</em><span>(.*?)</span>.*</div>',local_weather_html,re.S)  
for n in moji_myItems:
	print u'PM2.5指数:'+n[0].decode(mytype)
	print u'污染程度 :'+n[1].decode(mytype).lstrip()

#输出温馨提示信息
moji_prompt=re.findall('<div class="map-air-time">.*?<p>.*?:(.*?)</p>',local_weather_html,re.S)
print u'温馨提醒 :'+moji_prompt[0].lstrip().decode(mytype)

#输出发布时间
moji_air_time=re.findall('<div class="map-air-time">\n(.*?)\n.*?</div>',local_weather_html,re.S)
print u'发布时间 :'+moji_air_time[0].decode(mytype).lstrip().replace(u'发布','')