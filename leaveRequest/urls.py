
from django.urls import path,include
from .views import LeaveRequestView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('',LeaveRequestView,basename='requestapproval'),
urlpatterns = [
    path('',include(router.urls))

]