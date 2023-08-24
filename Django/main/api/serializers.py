from rest_framework import serializers
from .models import Students


# def starts_with_n(value):
#     if value[0].lower() != 'n':
#         raise serializers.ValidationError('Name should start with N')
    

# class StudentSerializers(serializers.Serializer):
#     name = serializers.CharField (max_length = 20, validators= [starts_with_n])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length = 30)

#     def create(self, validate_data):
#         return Students.objects.create(**validate_data)
    
#     def update(self, instance, validated_data):
#         print(instance.name)
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()

#         return instance

#     def validate_roll(self, value):
#         if value > 250:
#             raise serializers.ValidationError('Seats full')

#         return value
    
#     def validate(self, data):
#         nm = data.get('name')
#         ct = data.get('city')

#         if nm == 'daksh' and ct != 'jaipur':
#             raise serializers.ValidationError('City must be Jaipur')
#         return data
    


# model serializers
class StudentSerializers(serializers.ModelSerializer):
    # name = serializers.CharField(read_only = True)

    class Meta:
        model = Students
        fields = ['id', 'name', 'roll', 'city']
        read_only_fields = ['name', 'roll']



