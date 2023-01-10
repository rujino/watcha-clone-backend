from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import status
from reviews.serializers import ReviewSerializer
from series.serializers import SeriesDetailSerializer, SeriesListSerializer
from .models import Series

# Create your views here.
class Series_s(APIView):
    def get(self, request):
        all_series = Series.objects.all()
        serializer = SeriesListSerializer(
            all_series,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)


class Series_sDetail(APIView):
    def get_object(self, pk):
        try:
            return Series.objects.get(pk=pk)
        except Series.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        series = self.get_object(pk)
        serializer = SeriesDetailSerializer(
            series,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        series = self.get_object(pk)
        serializer = SeriesListSerializer(
            series,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_series = serializer.save()
            return Response(SeriesListSerializer(updated_series).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Series_Genre_Drama(APIView):
    def get(self ,request):
        all_series = Series.objects.filter(genre=8)
        serializer = SeriesListSerializer(
            all_series,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)


class Series_sReviews(APIView):
    def get_object(self, pk):
        try:
            return Series.objects.get(pk=pk)
        except Series.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        series = self.get_object(pk)
        print(series)
        serializer = ReviewSerializer(series.review_set.all(), many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        series = self.get_object(pk)
        serializer = ReviewSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            review = serializer.save(
                user=request.user,
                series=series,
            )
            print(review)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
