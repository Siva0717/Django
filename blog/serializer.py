
from rest_framework import serializers
from.models import hotel, university, inventory


class hotelSerializer(serializers.ModelSerializer):
    class Meta:
        model=hotel
        fields= '__all__'
        extra_Kwargs={
            'password':{'write_only':True}
        }

    def valid(self, validated_data):
        password=validated_data.pop('password', None)
        instance= self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance
        
class universitySerializer(serializers.ModelSerializer):
    class Meta:
        model=university
        fields='__all__'

class inventorySerializer(serializers.ModelSerializer):
     class Meta:
         model=inventory
         fields= '__all__'

        