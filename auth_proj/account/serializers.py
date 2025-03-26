from rest_framework import serializers
from account.models import MyUser

class UserRegistrationSerialier(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model= MyUser
        fields= '__all__'
        extra_kwargs={
            'password':{'write_only': True}
        }

    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError('Password & Conf Password Doesnt match')
        return attrs
    
    def create(self, validate_data):
        return MyUser.objects.create_user(**validate_data)
    
class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model = MyUser
        fields= ['email','password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'email','name']