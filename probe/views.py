from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from probe.models import TwoIntegers
from probe.serializers import TwoIntegersSerializer
from probe.tasks import sum_task


class SomeView(ModelViewSet):

    queryset = TwoIntegers.objects.all()
    serializer_class = TwoIntegersSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        ser = TwoIntegersSerializer(data=request.data)
        ser.is_valid()
        first = ser.validated_data.get('first')
        second = ser.validated_data.get('second')
        sum_task.delay(first,  second)
        return Response('OK')
