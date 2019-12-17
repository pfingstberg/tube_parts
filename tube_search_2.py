# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 09:26:31 2018

@author: User
"""

#api_key = '&key='+'AIzaSyA8lWG_8zM7R7ujsxTqMjft8ZunW3xV08o'
api_key = '&key='+'AIzaSyAfJGu_O13VGxcKjd90eL0A0ddAM72QEVc'
channelId = ''
videoId   = ''
channel_list = list()
video_list   = list()
url_base = 'https://www.googleapis.com/youtube/v3/search?'

#%%
part       = '&part='+'snippet'     # 'id,snippet' daje to samo co 'snippet'
#channelId  = '&channelId='+'UCQpBmjL9kJ768fty4tbqa6Q'   # Phil Konieczny
channelId  = '&channelId=' +'UCUj7z3B90RqN5g8ctpLeDkw'  # Eliza Michalik
maxResults = '&maxResults='+'8'
order      = '&order='     +'date'

url1 = url_base+part+channelId+maxResults+order+api_key
url2 = url_base+api_key+channelId+part+order+maxResults


#url4 = 'https://www.googleapis.com/youtube/v3/search?key=AIzaSyAfJGu_O13VGxcKjd90eL0A0ddAM72QEVc&channelId=UCQpBmjL9kJ768fty4tbqa6Q&part=snippet,id&order=date&maxResults=5'
url4 = 'https://www.googleapis.com/youtube/v3/search?key=AIzaSyAfJGu_O13VGxcKjd90eL0A0ddAM72QEVc&channelId=UCUj7z3B90RqN5g8ctpLeDkw&part=snippet,id&order=date&maxResults=5'

#%%
import certifi
import urllib3
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
r = http.request('GET', url2)
print(r.status,"\n"*5)
#%%
print(r.data)   
#   r.data jest byte stringiem, you need to decode if you want a string
#   rdd = r.data.decode('utf-8')
#   ale string można od razu załadować do struktury
import json
rdj = json.loads(r.data)
