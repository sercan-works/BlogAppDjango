from rest_framework import serializers
from .models import Category,Post,Comment,Like,PostView

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields=(
            "user",
            "post",
            "time_stamp",
            "content"
        )
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields=(
            "user",
            "post"
        )

class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True,read_only=True)
    like = LikeSerializer(many=True,read_only=True)
     

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
        
       
 
    