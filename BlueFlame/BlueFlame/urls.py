# urlpatterns 필수 사항
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from FestivalApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),

    path('timeline', views.timeTable, name='timeTable'),

    path('list/<int:day>', views.booth, name="booth"),

    path('pub/<int:pub_id>', views.pubDetail, name="pubDetail"),
    path('club/<int:club_id>', views.clubDetail, name="clubDetail"),

    path('aboutUs', views.aboutUs, name="aboutUs" ),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)