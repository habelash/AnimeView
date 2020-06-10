from django.shortcuts import render
from django.http import Http404
from .models import onepiece


# Create your views here.
def index(request):
    return render(request, 'index.html')


def watchanime(request):
    return render(request, 'watchanime.html')


def animelist(request):
    details = onepiece.objects.all().order_by('Episode')
    return render(request, 'animelist.html', {'details': details})


def searchanime(request):
    return render(request, 'searchanime.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def one_piece(request, ep_no):
    try:
        display = onepiece.objects.get(Episode=ep_no)
    except onepiece.DoesNotExist:
        raise Http404("Episode Does Not Exist.")
    context = {
        'display': display,
        "anime": onepiece.objects.all().order_by('Episode')
    }
    return render(request, 'watchanime.html', context)
