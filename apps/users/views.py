from rest_framework import serializers, viewsets
# breinfs in the User Model
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # returns User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    # Overriding the default create model
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
