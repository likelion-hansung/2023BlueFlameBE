from django.shortcuts import get_object_or_404, render
from .models import Pub, Club

def home(request):
    return render(request, 'home.html')

def timeTable(request):
    return render(request, 'timeTable.html')

def booth(request, day):
    pubs = Pub.objects.filter(date = day)
    clubs = Club.objects.filter(date = day)
    return render(request, 'index.html', {'pubs':pubs, 'clubs':clubs})

def foodBooth(request, day):
    pubs = Pub.objects.filter(date = day)
    return render(request, 'index.html', {'pubs':pubs})

def eventBooth(request, day):
    clubs = Club.objects.filter(date = day)
    return render(request, 'index.html', {'clubs':clubs})

def pubDetail(request, pub_id):
    pub = get_object_or_404(Pub, pk = pub_id)
    return render(request, 'pub.html', {'pub':pub})

def clubDetail(request, club_id):
    club = get_object_or_404(Club, pk = club_id)
    return render(request, 'club.html', {'club':club})

def aboutUs(request):
    return render(request, 'aboutus.html')

