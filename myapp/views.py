from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .custom_permissions import IsAdmin
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

class UserListCreateView(APIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        users = User.objects.all().values('id','username','email', 'role')
        return Response(users,status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            role=data['role'],
        )
        return Response({"message": "User created successfully", "user_id": user.id}, status=status.HTTP_201_CREATED)

class UserDetailUpdateDeleteView(APIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            return Response({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role,
            },status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, user_id):
        try:
            data = request.data
            user = User.objects.get(id=user_id)
            user.username = data['username']
            user.email = data['email']
            user.role = data['role']
            user.save()
            return Response({"message": "User updated successfully"}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
