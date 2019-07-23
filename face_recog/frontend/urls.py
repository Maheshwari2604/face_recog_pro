from django.conf.urls import url ,include
from .views import userviewset , register
from rest_framework import routers
#from .api import UserViewSet

routers = routers.DefaultRouter()
routers.register('employee',userviewset)

urlpatterns = [
    url(r'^employee/', include(routers.urls)),

    #url(r'aa/', views.PostList.as_view()),
    #url(r'^<int:pk>/', views.PostDetail.as_view()),
    url(r'^$', register , name='register'),
    #url(r'^user/', userview.as_view()),
]





# urlpatterns += router.urls 