from rest_framework.serializers import ModelSerializer, Serializer
from post.models import PostModel
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class SecureUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["name", "last_name", "address"]


class PostSerializer(ModelSerializer):
    create_at = SecureUserSerializer()

    class Meta:
        model = PostModel
        fields = "__all__"
        read_only = ["created_at", "created_by", "updated_by"]

    def get_extra_kwargs(self):
        pass
