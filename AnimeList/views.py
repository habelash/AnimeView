from django.shortcuts import render
from django.http import Http404
from .models import onepiece, naruto, haikyu, aot, onepunchman, bnha, afrosamurai, bleach, deathnote, kny, fairytail, \
    fmab, hxh, tokyoghoul, boruto

from list.models import animelist, topanime


# Create your views here.
def index(request):
    return render(request, 'index.html')


def watchanime(request):
    return render(request, 'watchanime.html')


def animes(request):
    details = animelist.objects.all().order_by('name')
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
        "link": 'onepiece',
        "topanime": topanime.objects.all()
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


def haikyuu(request, ep_no):
    try:
        display = haikyu.objects.get(Episode=ep_no)
    except haikyu.DoesNotExist:
        raise Http404("Episode Does Not Exist.")
    context = {
        'display': display,
        "anime": haikyu.objects.all().order_by('Episode'),
        "link": 'haikyu'
    }
    return render(request, 'watchanime.html', context)


def demon_slayer(request, ep_no):
    try:
        display = kny.objects.get(Episode=ep_no)
    except kny.DoesNotExist:
        raise Http404("Episode Does Not Exist.")
    context = {
        'display': display,
        "anime": kny.objects.all().order_by('Episode'),
        "link": 'demonslayer'
    }
    return render(request, 'watchanime.html', context)


def attackontitans(request, ep_no):
    try:
        display = aot.objects.get(Episode=ep_no)
    except aot.DoesNotExist:
        raise Http404("Episode Does Not Exist.")
    context = {
        'display': display,
        "anime": aot.objects.all().order_by('Episode'),
        "link": 'attackontitans'
    }
    return render(request, 'watchanime.html', context)


def onepunchmann(request, ep_no):
    try:
        display = onepunchman.objects.get(Episode=ep_no)
    except onepunchman.DoesNotExist:
        raise Http404("Episode Does Not Exist.")
    context = {
        'display': display,
        "anime": onepunchman.objects.all().order_by('Episode'),
        "link": 'onepunchman'
    }
    return render(request, 'watchanime.html', context)


def myheroaccademy(request, ep_no):
    try:
        display = bnha.objects.get(Episode=ep_no)
    except bnha.DoesNotExist:
        raise Http404("Episode Does Not Exist.")
    context = {
        'display': display,
        "anime": bnha.objects.all().order_by('Episode'),
        "link": 'myheroaccademy'
    }
    return render(request, 'watchanime.html', context)


def afro_samurai(request, ep_no):
    try:
        display = afrosamurai.objects.get(Episode=ep_no)
    except afrosamurai.DoesNotExist:
        raise Http404("Episode Does Not Exist.")
    context = {
        'display': display,
        "anime": afrosamurai.objects.all().order_by('Episode'),
        "link": 'afrosamurai'
    }
    return render(request, 'watchanime.html', context)


def blleach(request, ep_no):
    try:
        display = bleach.objects.get(Episode=ep_no)
    except bleach.DoesNotExist:
        raise Http404("Episode Does Not Exist.")
    context = {
        'display': display,
        "anime": bleach.objects.all().order_by('Episode'),
        "link": 'bleach'
    }
    return render(request, 'watchanime.html', context)


def death_note(request, ep_no):
    try:
        display = deathnote.objects.get(Episode=ep_no)
    except deathnote.DoesNotExist:
        raise Http404("Episode Does Not Exist.")
    context = {
        'display': display,
        "anime": deathnote.objects.all().order_by('Episode'),
        "link": 'deathnote'
    }
    return render(request, 'watchanime.html', context)


def fairy_tail(request, ep_no):
    try:
        display = fairytail.objects.get(Episode=ep_no)
    except fairytail.DoesNotExist:
        raise Http404("Episode Does Not Exist.")
    context = {
        'display': display,
        "anime": fairytail.objects.all().order_by('Episode'),
        "link": 'fairytail'
    }
    return render(request, 'watchanime.html', context)


def full_metal_alcamist(request, ep_no):
    try:
        display = fmab.objects.get(Episode=ep_no)
    except fmab.DoesNotExist:
        raise Http404("Episode Does Not Exist.")
    context = {
        'display': display,
        "anime": fmab.objects.all().order_by('Episode'),
        "link": 'fullmetalalcamist'
    }
    return render(request, 'watchanime.html', context)


def hunterxhunter(request, ep_no):
    try:
        display = hxh.objects.get(Episode=ep_no)
    except hxh.DoesNotExist:
        raise Http404("Episode Does Not Exist.")
    context = {
        'display': display,
        "anime": hxh.objects.all().order_by('Episode'),
        "link": 'hunterXhunter'
    }
    return render(request, 'watchanime.html', context)

def tokyo_ghoul(request, ep_no):
    try:
        display = tokyoghoul.objects.get(Episode=ep_no)
    except tokyoghoul.DoesNotExist:
        raise Http404("Episode Does Not Exist.")
    context = {
        'display': display,
        "anime": tokyoghoul.objects.all().order_by('Episode'),
        "link": 'tokyoghoul'
    }
    return render(request, 'watchanime.html', context)

def borutoo(request, ep_no):
    try:
        display = boruto.objects.get(Episode=ep_no)
    except boruto.DoesNotExist:
        raise Http404("Episode Does Not Exist.")
    context = {
        'display': display,
        "anime": boruto.objects.all().order_by('Episode'),
        "link": 'boruto'
    }
    return render(request, 'watchanime.html', context)