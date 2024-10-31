from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserCreateModelViewSet, Login, UpdatePasswordView, LogoutView

router = DefaultRouter()
router.register(r'users', UserCreateModelViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', Login.as_view(), name='login'),
    path('update-password/', UpdatePasswordView.as_view(), name='update_password'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
