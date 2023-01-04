from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
)
from .serializers import ListListSerializer, ListDetailSerializer
from .models import List

# Create your views here.


class ListList(APIView):
    def get(self, request):
        all_list = List.objects.all()
        serializer = ListListSerializer(all_list, many=True)
        return Response(serializer.data)


class ListDetail(APIView):
    def get_object(self, pk):
        try:
            return List.objects.get(pk=pk)
        except:
            raise NotFound

    def get(self, request, pk):
        list = self.get_object(pk)
        serializer = ListDetailSerializer(list)
        return Response(serializer.data)
