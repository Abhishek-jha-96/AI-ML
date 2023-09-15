from .views import ImageView
from rest_framework import routers
from django.urls import path, include

app_name = 'api-image'

router = routers.DefaultRouter()
router.register(r'image', ImageView)

urlpatterns = [
    path('', include(router.urls))
]
