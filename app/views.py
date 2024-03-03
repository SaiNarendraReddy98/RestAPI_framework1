from django.shortcuts import render
from rest_framework.response import Response
from app.models import *
from app.serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser


# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated,IsAdminUser])
def jsonData_vizag(request):
    VDO = Vizag_places.objects.all()
    JSDO = VizagplacesModelSerializers(VDO,many=True)

    jsondata = JSDO.data

    return Response(jsondata)