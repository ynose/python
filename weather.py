#coding:utf-8

import sys
import urllib
import json

def livedoor_weather_api():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=120010'

    #print url + params
    response = urllib.urlopen(url)
    return response.read()
    
def livedoor_weather_json(s):
    item_list = json.loads(s)
    
    # 場所名
    print urllib.unquote(item_list["title"].encode('utf8'))
    # 今日[0]  明日は[1]  明後日は[2]
    forecasts_today = item_list["forecasts"][0]
    print urllib.unquote(forecasts_today['dateLabel'].encode('utf8'))
    print urllib.unquote(forecasts_today['date'].encode('utf8'))
    print urllib.unquote(forecasts_today['telop'].encode('utf8'))
    # 最低気温
    if forecasts_today['temperature']['min'] is not None:
        print "最低気温" + urllib.unquote(forecasts_today['temperature']['min']['celsius'].encode('utf8')) + "℃"
        
    if forecasts_today['temperature']['max'] is not None:
        print "最高気温" + urllib.unquote(forecasts_today['temperature']['max']['celsius'].encode('utf8')) + "℃"


if __name__ == '__main__':
    json_str = livedoor_weather_api()
    livedoor_weather_json(json_str)
