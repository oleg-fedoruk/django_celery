from rest_framework.serializers import Serializer, ModelSerializer

from probe.models import TwoIntegers


class TwoIntegersSerializer(ModelSerializer):
    class Meta:
        model = TwoIntegers
        fields = '__all__'
