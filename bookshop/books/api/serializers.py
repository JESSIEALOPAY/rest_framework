from django.db.models import fields
from rest_framework import serializers
from books.models import Book , Comment



class CommentSerializer(serializers.ModelSerializer):
    commenter= serializers.StringRelatedField(read_only=True)
    class Meta:
        model= Comment
        # fields= "__all__"
        exclude= ["book"]


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Book
        fields = "__all__"

    comments= CommentSerializer(many=True,read_only=True)
