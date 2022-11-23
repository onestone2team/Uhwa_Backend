from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.models import Users
from .validators import (
                            emailvaildator,
                            passwordvaildator,
                        )
import re

class UserSerializer(serializers.ModelSerializer):
    password_check = serializers.CharField(max_length=50, write_only=True)
    class Meta:
        model = Users
        fields = '__all__'
    def validate(self, attrs):
        is_password = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@!%*#?&])[A-Za-z\d@!%*#?&]{8,}$')
        if not is_password.fullmatch(attrs['password']):
             raise serializers.ValidationError("비밀번호는 최소 8자이상, 숫자, 문자 특수문자를 하나이상 포함해야합니다.")
        password_valid = passwordvaildator(
            attrs['password'], attrs["password_check"])
        if password_valid == False:
            raise serializers.ValidationError("비밀번호가 일치하지 않습니다.")
        attrs.pop('password_check', None)    
        email_valid = emailvaildator(attrs['email'])
        if email_valid == False:
            raise serializers.ValidationError("유효하지 않은 이메일입니다.")
        return super().validate(attrs)

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def update(self, validated_data):
        user = super().update(validated_data)
        password = user.password
        user.set_password(password)
        user.is_active = False
        user.save()
        return user


class CustomedUserSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_admin'] = user.is_admin
        token['address'] = user.address
        return token
