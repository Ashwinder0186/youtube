import requests
from .models import City
from isodate import parse_duration
from .forms import CityForm

from django.conf import settings
from django.shortcuts import render, redirect

def index(request):
    videos = []

    if request.method == 'POST':
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        search_params = {
            'part' : 'snippet',
            'q' : request.POST['search'],
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'maxResults' : 9,
            'type' : 'video'
        }

        r = requests.get(search_url, params=search_params)
  


        results = r.json()['items']
    

        video_ids = []
        for result in results:
            video_ids.append(result['id']['videoId'])

        if request.POST['submit'] == 'lucky':
            return redirect(f'https://www.youtube.com/watch?v={ video_ids[0] }')

        video_params = {
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'part' : 'snippet,contentDetails',
            'id' : ','.join(video_ids),
            'maxResults' : 9
        }

        r = requests.get(video_url, params=video_params)

        results = r.json()['items']

        
        for result in results:
            video_data = {
                'title' : result['snippet']['title'],
                'id' : result['id'],
                'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                'url2' : f'https://www.youtubepp.com/watch?v={ result["id"] }',
                'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'thumbnail' : result['snippet']['thumbnails']['high']['url']
            }

            videos.append(video_data)

    context = {
        'videos' : videos
    }
    
    return render(request, 'search/index.html', context)








def index1(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=ad3bc86040cf57b155df5fbe2d8c1ca1'
    #url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c3346984e18cb7358c27c387e3a0dfc2'

    if request.method == 'POST':
        
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    try:
        for city in cities:
            r = requests.get(url.format(city)).json()
            temp=(r['main']['temp']-32)*0.55555555555
            temp1 = "{:.2f}".format(temp)
            print(temp1)

            city_weather = {
            'city' : city.name,
            'temperature' : temp1,
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            }

            weather_data.append(city_weather)
    except KeyError:
        pass
    except Exception as e:
        pass





    context = {'weather_data' : weather_data, 'form' : form}
    try:
        p=City.objects.all()
        r=list(reversed(p))[0].delete()
    except Exception as e:
        pass

    return render(request, 'search/index1.html', context)