from django.shortcuts import render
from django.http import Http404
from .models import onepiece, naruto
from list.models import animelist, topanime


# Create your views here.
def index(request):
    return render(request, 'index.html')


def watchanime(request):
    return render(request, 'watchanime.html')


def animes(request):
    details = animelist.objects.all()
    return render(request, 'animelist.html', {'details': details})


def searchanime(request):
    details = animelist.objects.all()
    return render(request, 'searchanime.html', {'details': details})


def aboutus(request):
    return render(request, 'aboutus.html')


def top_anime(request):
    details = topanime.objects.all()
    return render(request, 'topanime.html', {'details': details})


def one_piece(request, ep_no):
    try:
        display = onepiece.objects.get(Episode=ep_no)
    except onepiece.DoesNotExist:
        raise Http404("Episode Does Not Exist.")
    context = {
        'display': display,
        "anime": onepiece.objects.all().order_by('Episode'),
        "link": 'onepiece'
    }
    return render(request, 'watchanime.html', context)


def naruto_(request, ep_no):
    try:
        display = naruto.objects.get(Episode=ep_no)
    except naruto.DoesNotExist:
        raise Http404("Episode Does Not Exist.")
    context = {
        'display': display,
        "anime": naruto.objects.all().order_by('Episode'),
        "link": 'naruto'
    }
    return render(request, 'watchanime.html', context)
