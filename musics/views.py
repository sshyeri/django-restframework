from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Music, Artist
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer

# Create your views here.

# Response를 통해 Serializer를 반환
# Serializer - 특정한 딕셔너리 혹은 쿼리셋 등의
# 파이썬 형식 데이터 타입을 반환해주도록 하는 아이

# music는 쿼리셋, 일종의 리스트인데 우리가 응답하려고 하는 것은 json
# Serializer가 해주는 것은 리스트를 하나 하나씩 json 타입으로 바꿔주는 고마운 도구
# 그리고 응답하는 함수는 Response이다.
# 결과로 보내줄 데이터는 .data로 가져온다.

@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicSerializer(music)
    return Response(serializer.data)
    
@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)
    
@api_view(['POST'])
def comment_create(request, music_pk):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music_pk)
        return Response(serializer.data)