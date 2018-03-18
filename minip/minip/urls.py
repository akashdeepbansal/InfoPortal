"""minip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from material.frontend import urls as frontend_urls
from rest_framework.urlpatterns import format_suffix_patterns
from users import views as users_view
from events import views as events_view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', users_view.userList.as_view()),
    # url(r'^events/', include('events.urls')),
    url(r'events/', events_view.eventList.as_view()),
    url(r'news/', events_view.newsList.as_view()),
    # url(r'user/', views.userList.as_view()),
    # url(r'', include(frontend_urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
