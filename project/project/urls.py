

from django.contrib import admin
from django.urls import path, include            # include doctor app url path




urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include("doctor.urls"))
]
