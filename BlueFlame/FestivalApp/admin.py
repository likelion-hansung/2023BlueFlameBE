from django.contrib import admin
from .models import Club, Pub, Menu

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'belong')
    list_display_links = ['name']
    list_filter = ['location']

    # def short_content(self):
    #     return self.content[:10]
    
    # def short_information(self):
    #     return self.information[:10]

@admin.register(Pub)
class PubAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'location', 'belong')

    # def short_content(self):
        # return self.content[:10]
    

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
