from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenRefreshView,
)

#urls from multiple modules
from api.urls import urlpatterns as api_urls
from myapp.urls import urlpatterns as app_urls
from auth_app.urls import urlpatterns as auth_app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += auth_app_urls
urlpatterns += app_urls
urlpatterns += api_urls