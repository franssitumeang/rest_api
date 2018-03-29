from rest_framework import generics
from .models import Topic, News
from .serializers import TopicSerializers, NewsSerializers

class CreateNews(generics.CreateAPIView):
    serializer_class = NewsSerializers

class ListNews(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers

class ViewDetailNews(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers

class DeleteNews(generics.DestroyAPIView):
    queryset = News.objects.all()

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class UpdateNews(generics.RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers

class FilterNewsByStatus(generics.ListAPIView):
    serializer_class = NewsSerializers
    def get_queryset(self):
        status = self.kwargs['status']
        queryset = News.objects.filter(status=status)
        return queryset

class FilterNewsByTopic(generics.ListAPIView):
    serializer_class = NewsSerializers
    def get_queryset(self):
        pk = self.kwargs['pk']
        topic = Topic.objects.get(pk=pk)
        queryset = News.objects.filter(topic=topic)
        return queryset

class CreateTopic(generics.CreateAPIView):
    serializer_class = TopicSerializers

class ListTopic(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializers

class ViewDetailTopic(generics.RetrieveAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializers

class DeleteTopic(generics.DestroyAPIView):
    queryset = Topic.objects.all()

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class UpdateTopic(generics.RetrieveUpdateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializers