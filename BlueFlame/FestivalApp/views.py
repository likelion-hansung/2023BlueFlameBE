from django.shortcuts import get_object_or_404, render
from .models import Pub, Club

def home(request):
    return render(request, 'main.html')

def timeLine(request):
    return render(request, 'timeline2.html')

def booth2(request):
    return render(request, 'booth(Day1).html')

def booth(request, day):
    if day == 0:
        template ="booth(Day1).html"
    elif day == 1:
        template ="booth(Day2).html"
    else:
        template="booth(Day3).html"
        day = 1
    pubs = Pub.objects.filter(date = day)
    clubs = Club.objects.filter(date = day)
    return render(request, template, {'pubs':pubs, 'clubs':clubs})

def pubDetail(request, pub_id):
    pub = get_object_or_404(Pub, pk = pub_id)
    return render(request, 'pub.html', {'pub':pub})

def clubDetail(request, club_id):
    club = get_object_or_404(Club, pk = club_id)
    return render(request, 'club.html', {'club':club})

def aboutUs(request):
    return render(request, 'aboutus.html')

