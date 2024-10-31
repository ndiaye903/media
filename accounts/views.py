from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer, UpdatePasswordSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .permissions import IsAdministrateur

class UserCreateModelViewSet(ModelViewSet):
    permission_classes = [IsAdministrateur]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        user_id = serializer.instance.id
        return Response({**serializer.data, 'id': user_id}, status=status.HTTP_201_CREATED, headers=headers)

class Login(APIView):
    permission_classes = [AllowAny] 
    @swagger_auto_schema(
        operation_description="Login with username and password",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            },
            required=['username', 'password'],
        ),
        responses={
            200: openapi.Response(
                description="Successful login",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
                        'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                        'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First Name'),
                        'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last Name'),
                        'is_guest': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is Guest'),
                        'is_administrateur': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is Administrator'),
                        'is_secretaire': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is Secretary'),
                        'token': openapi.Schema(type=openapi.TYPE_STRING, description='Auth Token'),
                    }
                )
            ),
            400: "Invalid credentials"
        }
    )
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            user_data = CustomUserSerializer(user).data
            return Response({**user_data, 'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
        

class UpdatePasswordView(APIView):
    @swagger_auto_schema(
        operation_description="Update password",
        request_body=UpdatePasswordSerializer,
        responses={
            200: "Password updated successfully",
            400: "Invalid data",
            401: "Unauthorized"
        }
    )
    def patch(self, request, *args, **kwargs):
        user = request.user
        serializer = UpdatePasswordSerializer(data=request.data)
        if serializer.is_valid():
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"detail": "Password updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)