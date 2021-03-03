from rest_framework import serializers, viewsets
# breinfs in the User Model
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'is_active')

        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    # Overriding the default create model
    def create(self, validated_data):
        # is student is a custom field in the user model
        # so  this field needs to be saved AFTER the User is saved
        is_active = validated_data.pop('is_active')
        user = get_user_model().objects.create_user(**validated_data)
        user.is_active = is_active
        user.save()
        return user


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
