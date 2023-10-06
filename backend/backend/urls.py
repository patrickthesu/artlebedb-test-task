from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from libraries.views import LibraryViewSet

router = SimpleRouter()

router.register(r"library", LibraryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
