from django.urls import path

from products.views import CategoryViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'categories', CategoryViewSet)
# router.register(r'accounts', AccountViewSet)

urlpatterns = [
]

urlpatterns += router.urls
