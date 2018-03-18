from django.contrib import admin
from users.models import user_details
from events.models import event_details
from events.models import news_details

# Register your models here.
# admin.site.register(user_details)


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'password')

# class EventAdmin(admin.ModelAdmin):
#     list_display = ('title', 'details')

# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'details')



admin.site.register(user_details, UserAdmin)
# admin.site.register(event_details, EventAdmin)
# admin.site.register(news_details, NewsAdmin)
