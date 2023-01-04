from rest_framework import serializers
from .models import Rider,Requester,RegisterRider
class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = ["id","Name", "From_location", "To_location","Timestamp","number_of_assets","Medium"]


class RequesterSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Requester
        fields = ["id", "Name", "From_location", "To_location", "Timestamp", "Type_of_assets","Phone","Sensitivities","Status"]

class RequestFromRequesterSerializer(serializers.ModelSerializer) :
    class Meta :
        model = RegisterRider
        fields = ["id", "Requester", "Rider", "Timestamp"]
