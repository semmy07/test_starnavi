from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.models import User, Post
from .serializers import UserSerializer, RegistrationSerializer, PostSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user).data
    }


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostEndpoint(APIView):
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request):
        data = request.data
        user = User.objects.get(id=data.get('user_id'))

        fields = {
            'creator': user,
            'text': data.get('text', '')
        }

        Post.objects.create(**fields)
        return JsonResponse({"ok": True, "message": 'Post created successfully'},
                            status=200)

    def put(self, request):
        data = request.data

        user = User.objects.get(id=data.get('user_id'))
        post_id = data['post_id']

        current_post = Post.objects.get(id=post_id)
        all_likes = current_post.user_likes.all()

        if user in all_likes:
            current_post.user_likes.remove(user)
            message = 'Post liked'
        else:
            current_post.user_likes.add(user)
            message = 'Post unliked'

        return JsonResponse({"ok": True, "message": message}, status=200)

    def delete(self, request):
        data = request.data

        user = User.objects.get(id=data.get('user_id'))
        post_id = data['post_id']

        current_post = Post.objects.get(id=post_id)
        if current_post.creator == user:
            current_post.delete()
            return JsonResponse({"ok": True, "message": 'Post removed'}, status=200)

        return JsonResponse({"ok": False, "message": "You can't remove this post"}, status=403)
