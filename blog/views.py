from django.shortcuts import render
from django.views import generic
from .models import Post
import requests
from blog.views import *
import json
import requests
import time


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'



def get_currency(request):
# Import libraries

    # defining key/request url
    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    
    # requesting data from url

    data = requests.get(key)  
    data = data.json()
    def print_price():
        return data['price']

    price_prints = print_price()
    price_prints = float(price_prints)
    print_prints = round(price_prints,2)
    time.sleep(2)
    context = {'usd' : print_price}
    # print(context)
    # context = float(context)
    # context = round(context,2)
    return render(request , 'sidebar.html', context)