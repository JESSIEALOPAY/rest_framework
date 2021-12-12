from django.db.models import fields
from rest_framework import serializers
from news.models import News ,Reporter

from datetime import datetime,date
from django.utils.timesince import timesince


class  NewsSerializer(serializers.ModelSerializer):
    time_since_publish= serializers.SerializerMethodField()
    # author=serializers.StringRelatedField()# postta hata veriyor

    class Meta:
        model= News
        fields="__all__"
        # exclude=["active"]
        # fields= ["title","explanation","text"]
        read_only_fields= ["id","created_date","update_date"]
    
    def get_time_since_publish(self, object):
        now= datetime.now()
        publishDate= object.release_date
        if object.active:
            time_delta= timesince(publishDate,now)
            return time_delta
        return "we can't calculate since publish time because your active status is false"

    def validate_release_date(self,value):
        today= date.today()
        if value> today:
            raise serializers.ValidationError("Release date bugünden ileri olamaz")
        return value


class ReporterSerializer(serializers.ModelSerializer):
    # news = NewsSerializer(many=True, read_only=True)
    # news = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,           # HyperlinkedrelatedField yapamadım.
    #     view_name='api:detail',
    # )
    news = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    class Meta:
        model= Reporter
        fields= "__all__"













###   Standart Serializer 
class NewsDefaultSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only= True)
    author = serializers.CharField()
    title = serializers.CharField()
    explanation = serializers.CharField()
    text = serializers.CharField()
    city = serializers.CharField()
    release_date = serializers.DateField()
    active = serializers.BooleanField()
    created_date =serializers.DateTimeField(read_only=True)
    update_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author= validated_data.get("author", instance.author)
        instance.title =validated_data.get("title",instance.title)
        instance.explanation =validated_data.get("explanation",instance.explanation)
        instance.text =validated_data.get("text",instance.text)
        instance.city =validated_data.get("city",instance.city)
        instance.release_date =validated_data.get("release_date",instance.release_date)
        instance.active =validated_data.get("active",instance.active)
        instance.save()
        return instance

    def validate(self,data):
        if data["title"]== data["explanation"]:
            raise serializers.ValidationError("title and explanation fields can not be same")
        return data

    def validate_author(self,value):
        if len(value)<4:
            raise serializers.ValidationError(f"auhtor has to be least 4 character. You typed {len(value)} character")
        return value



