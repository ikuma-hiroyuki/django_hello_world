from django.contrib import admin
from django.urls import path, include

from hello import views

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
    path('hello2/', views.HelloView.as_view(), name='hello_class'),
]
