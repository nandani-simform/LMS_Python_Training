from rest_framework import serializers
from .models import Students


# model serializers
class StudentSerializers(serializers.ModelSerializer):
    # name = serializers.CharField(read_only = True)

    class Meta:
        model = Students
        fields = ['id', 'name', 'roll', 'city']
        # read_only_fields = ['name', 'roll']



