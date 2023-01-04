from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from series.models import Series
from .serializers import WishlistsSerializer
from .models import Wishlist


class Wishlists(APIView):
    def get(self, request):
        if Wishlist.objects.filter(user=request.user):
            print("!!")
            all_wishlists = Wishlist.objects.filter(user=request.user)
            serializer = WishlistsSerializer(
                all_wishlists,
                many=True,
                context={"request": request},
            )
        else:
            Wishlist.objects.create(user=request.user)
            all_wishlists = Wishlist.objects.filter(user=request.user)
            serializer = WishlistsSerializer(
                all_wishlists,
                many=True,
                context={"request": request},
            )
        return Response(serializer.data)

    def post(self, request):
        serializer = WishlistsSerializer(data=request.data)
        if serializer.is_valid():
            wishlist = serializer.save(
                user=request.user,
            )
            serializer = WishlistsSerializer(wishlist)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WishlistToggle(APIView):
    def get_list(self, pk, user):
        try:
            return Wishlist.objects.get(pk=pk, user=user)
        except Wishlist.DoesNotExist:
            raise NotFound

    def get_series(self, pk):
        try:
            return Series.objects.get(pk=pk)
        except Series.DoesNotExist:
            raise NotFound

    def put(self, request, pk, series_pk):
        wishlist = self.get_list(pk, request.user)
        series = self.get_series(series_pk)
        if wishlist.series.filter(pk=series.pk).exists():
            wishlist.series.remove(series)
        else:
            wishlist.series.add(series)

        return Response(status=status.HTTP_200_OK)
