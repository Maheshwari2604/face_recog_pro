from rest_framework import serializers
from .models import Users
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import exceptions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


# class QuestionSerializer(serializers.ModelSerializer):
#     choices = ChoiceSerializer(many=True)
#     tags = TagSerializer(many=True)

#     class Meta:
#         model = Question
#         fields = [
#             "id",
#             "title",
#             "status",
#             "created_by",
#             "choices",
#             "tags"
#         ]
# read_only_fields = ["tags"]



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data

