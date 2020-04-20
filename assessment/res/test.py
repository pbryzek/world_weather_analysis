import json
import os

filepath = os.path.join("youtube_response.json")
with open(filepath) as jsonfile:
    video_json = json.load(jsonfile)
    
    tmp = video_json['data']['items'][0]['thumbnail']['default']
    print(tmp)

"""
{'apiVersion': '2.0', 
'data': {'updated': '2010-01-07T19:58:42.949Z', 'totalItems': 800, 'startIndex': 1, 'itemsPerPage': 1, 
'items': [{'id': 'hYB0mn5zh2c', 'uploaded': '2007-06-05T22:07:03.000Z', 'updated': '2010-01-07T13:26:50.000Z', 
'uploader': 'GoogleDeveloperDay', 'category': 'News', 'title': 'Google Developers Day US - Maps API Introduction', 
'description': 'Google Maps API Introduction ...', 'tags': ['GDD07', 'GDD07US', 'Maps'], 
'thumbnail': {'default': 'http://i.ytimg.com/vi/hYB0mn5zh2c/default.jpg', 
'hqDefault': 'http://i.ytimg.com/vi/hYB0mn5zh2c/hqdefault.jpg'}, 
'player': {'default': 'http://www.youtube.com/watch?vu003dhYB0mn5zh2c'}, 
'content': {'1': 'rtsp://v5.cache3.c.youtube.com/CiILENy.../0/0/0/video.3gp', '5': 'http://www.youtube.com/v/hYB0mn5zh2c?f...', '6': 'rtsp://v1.cache1.c.youtube.com/CiILENy.../0/0/0/video.3gp'}, 'duration': 2840, 'aspectRatio': 'widescreen', 'rating': 4.63, 'ratingCount': 68, 'viewCount': 220101, 'favoriteCount': 201, 'commentCount': 22, 'status': {'value': 'restricted', 'reason': 'limitedSyndication'}, 'accessControl': {'syndicate': 'allowed', 'commentVote': 'allowed', 'rate': 'allowed', 'list': 'allowed', 'comment': 'allowed', 'embed': 'allowed', 'videoRespond': 'moderated'}}]}}
"""