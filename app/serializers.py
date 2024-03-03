from rest_framework import serializers
from app.models import *

class VizagplacesModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vizag_places
        fields = '__all__'
        