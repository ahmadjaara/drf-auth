"""
allow data such data from queryset or models 
to be converted into python data types 
that can then be easily rendered into json 
"""
from rest_framework import serializers
from app.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=("id","title","author","excerpt","content")
        