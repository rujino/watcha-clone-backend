from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from videos.serializers import VideoCountSerializer
from .models import Video

class VideoViewCount(APIView):
    def get_video(self, request, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise status.NotFound
    
    def get(self, request, pk):
        video = self.get_video(self, pk)
        serializer = VideoCountSerializer(
            video,
        )
        return Response(serializer.data)

    def put(self, request, pk):
        video = self.get_video(self, pk)
        plus_count = video.play_count + 1
        serializer = VideoCountSerializer(
            video,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_video = serializer.save(play_count = plus_count)
            return Response(VideoCountSerializer(updated_video).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)