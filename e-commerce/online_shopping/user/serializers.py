from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','username', 'email', 'phone_number', 'date_of_birth', 'city', 'country', 'role') 

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields = ('username','password', 'email', 'role', 'first_name', 'last_name', 'phone_number') 
        extra_kwargs = {
                'first_name': {'required': True},
                'last_name': {'required': True},
                'role': {'required': True},
                'phone_number': {'required': False}
            }

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'], 
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role=validated_data['role'],
            phone_number=validated_data['phone_number']
            
            )
        user.set_password(validated_data['password'])
        user.save()

        return user
    
class UserLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

