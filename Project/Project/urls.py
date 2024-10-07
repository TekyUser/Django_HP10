from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.urls')),
    path('blog/', include('Blog.urls')),
]

handler404 = 'App.views.error'
