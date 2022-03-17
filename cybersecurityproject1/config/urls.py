from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('messages/', include('messageboard.urls')),
    path('', 
         TemplateView.as_view(template_name='home.html',
                              extra_context={'next': 'messages/'}),
         name='home')
]
