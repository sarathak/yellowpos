from django.urls import path

from users.views import *

# from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'users', UserViewSet)
# router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path(r'login', login, name='login'),
    path(r'register', register, name='register'),
]

# urlpatterns += router.urls
