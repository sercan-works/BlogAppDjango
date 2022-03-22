from unicodedata import category
from rest_framework import serializers
from .models import Category,Post,Comment,Like,PostView

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields=(
            "user",
            "post",
            "time_stamp",
            "content"
        )
    def get_user(self,obj):
        return obj.get_user_display()   

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Like
        fields=(
            "user",
            "post"
        )
    def get_user(self,obj):
        return obj.get_user_display()

class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True,read_only=True)
    like = LikeSerializer(many=True,read_only=True)
    category = serializers.SerializerMethodField() 
    author = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "image",
            "category",
            "publish_date",
            "last_updated",
            "comment",
            "like",
            "author",
            "status",
            "slug",
            "comment_count",
            "like_count",
            )
    def get_category(self,obj):
        return obj.get_category_display()    

    def get_author(self,obj):
        return obj.get_author_display()      
       
 
    