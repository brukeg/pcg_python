from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import URL
from random import choice, shuffle


def index(request):
    url = URL.objects.all()
    return render(request, 'url_shorten/index.html')


def shorten(request):
    if request.method == 'POST':
        url_input = request.POST['url']  # <input name in index.html name=''
        url = URL.objects.filter(long_url=url_input).first()

        if not url:
            url = URL(long_url=url_input, short=randomize(url_input))  # url_input
            url.save()
        return render(request, 'url_shorten/index.html', {'short': url.short})  # app name from urls.py


def redirectr(request, short_url):  # short_url
    url = get_object_or_404(URL, short=short_url)  # short_url
    print(url.long_url)
    return redirect(url.long_url)


def randomize(long_url):
    address = ''
    characters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '1234567890'
    n_char = 4
    n_num = 4
    while n_char > 0:
        char = choice(characters)
        address += char
        n_char -= 1
    while n_num > 0:
        num = choice(numbers)
        address += num
        n_num -= 1

    address = list(address)
    shuffle(address)
    short = ''.join(address)
    return short
