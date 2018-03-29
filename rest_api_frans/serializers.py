from rest_framework import serializers
from .models import Topic,News

class TopicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'