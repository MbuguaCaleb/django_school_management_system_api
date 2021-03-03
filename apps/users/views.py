from rest_framework import serializers, viewsets
# breinfs in the User Model
from django.contrib.auth import get_user_model
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # returns User
        # i must add all the fields i wish to see under the fields
        # all fields which i wish returned must be declared here
        fields = ('id', 'email', 'password', 'is_student')
        # write only means that the password will not be returned in the response
        # these are the validations
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    # Overriding the default create model
    def create(self, validated_data):
        # is student is a custom field in the user model
        # so  this field needs to be saved AFTER the User is saved
        is_student = validated_data.pop('is_student')
        user = get_user_model().objects.create_user(**validated_data)
        user.is_student = is_student
        user.save()
        return user


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
