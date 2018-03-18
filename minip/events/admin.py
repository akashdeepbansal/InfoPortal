from django.contrib import admin
from .models import event_details
from .models import news_details
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('title','date', 'details')
    list_filter = ('id','title','status')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'details')
    list_filter = ('id', 'title', 'status')

admin.site.register(event_details, EventAdmin)
admin.site.register(news_details, NewsAdmin)
