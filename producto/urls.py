from rest_framework import routers 
from .api import ProductoviewSet

router = routers.DefaultRouter()
router.register('api/producto', ProductoviewSet, 'producto')

urlpatterns=router.urls