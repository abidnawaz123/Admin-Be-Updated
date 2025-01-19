from django.contrib import admin
from django.urls import path
from myapp.urls import urlpatterns as app_urls
from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenRefreshView,
)
from api.urls import urlpatterns as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += app_urls
urlpatterns += api_urls