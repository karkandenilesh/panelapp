# serializers.py
from rest_framework import serializers
from .models import PanelInformation

class PanelInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PanelInformation
        fields = '__all__'
