# urls.py

from django.contrib import admin
from django.urls import path, include
from . import views  # Import views from the current directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Include accounts app URLs
    path('', views.home, name='home'),  # Home page URL
]
