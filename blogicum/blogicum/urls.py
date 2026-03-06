from django.contrib import admin
from django.urls import include, path

app_name = 'blogicum'

urlpatterns = [
    path("", include('blog.urls', namespace='index')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('pages/', include('pages.urls', namespace='pages')),
    path('admin/', admin.site.urls),
]
