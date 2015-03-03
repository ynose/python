#coding:utf-8

import sys
import urllib
import json

def weather_api():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=120010'

    #print url + params
    response = urllib.urlopen(url)
    return response.read()
    
def do_json(s):
    item_list = json.loads(s)
    

    for  k, v in item_list.iteritems():
        if k == "title":
            print urllib.unquote(v.encode('utf8'))
        if k == "forecasts":
            print urllib.unquote(v[1]['dateLabel'].encode('utf8'))
            print urllib.unquote(v[1]['date'].encode('utf8'))
            print urllib.unquote(v[1]['telop'].encode('utf8'))
            print urllib.unquote(v[1]['temperature']['min']['celsius'].encode('utf8'))
            print urllib.unquote(v[1]['temperature']['max']['celsius'].encode('utf8'))


if __name__ == '__main__':
    json_str = weather_api()
    do_json(json_str)
