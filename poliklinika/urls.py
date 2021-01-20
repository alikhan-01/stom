"""poliklinika URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from poliklinika import settings
from main.views import indexHandler,aboutHandler,serviceHandler, page404Handler,blogHandler,doctorsHandler,contactsHandler
from main.views import doctorsItemHandler,usefulHandler

urlpatterns = [
    path('about/', aboutHandler),
    path('service/', serviceHandler),
    path('blog/', blogHandler),
    path('doctors/', doctorsHandler),
    path('doctors/<int:item_id>/', doctorsItemHandler),
    path('useful/', usefulHandler),
    path('contacts/', contactsHandler),


    url(r'^media/(?P<path>.*)$', serve,{
        'document_root': settings.MEDIA_ROOT
    }),
    path('admin/', admin.site.urls),
    path('', indexHandler),

    path('404', page404Handler),
]
