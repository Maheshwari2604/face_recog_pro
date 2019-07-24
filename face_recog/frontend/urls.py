from django.conf.urls import url ,include
from .views import userviewset , register , PollListView
#from rest_framework import routers
from rest_framework.routers import DefaultRouter, SimpleRouter
#from .api import UserViewSet

routers = DefaultRouter()
routers.register('employee',userviewset)


# router = DefaultRouter()
# router.register('poll', PollViewSet)



urlpatterns = [
    url(r'^employee/', include(routers.urls)),
    url(r'^poll/', PollListView.as_view()),
    url(r'^poll/<int:id>/', PollListView.as_view()),

    #url(r'aa/', views.PostList.as_view()),
    #url(r'^<int:pk>/', views.PostDetail.as_view()),
    url(r'^$', register , name='register'),
    #url(r'^user/', userview.as_view()),
]





# urlpatterns += router.urls 