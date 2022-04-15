from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError



class UserRegistartionSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError('Password is too short')
        elif len(value) > 20:
            raise ValidationError('Password is too long')
        else: 
            return value

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']

        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return user