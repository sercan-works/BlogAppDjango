
from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance,filename):
    return 'blog/{0}/{1}'.format(instance.author.id,filename)

class Category(models.Model):
    name = models.CharField(max_length=100)  

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name



class Post(models.Model):
    OPTIONS = (
        ('d','Draft'),
        ('p','Published')
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.CharField(max_length=255)     #models.ImageField(upload_to=user_directory_path,default='blog.png') # local directory için
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    #comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices=OPTIONS,default='d')
    slug = models.SlugField(blank=True, unique=False) #Uniqe değiştirildi

    def __str__(self):
        return self.title

    
    def comment_count(self):
        return self.comment.count()

    def like_count(self):
        return self.like.count()

    def get_category_display(self):
        return self.category.name
    
    def get_author_display(self):
        return self.author.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="comment")
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username 

    def get_user_display(self):
        return self.user.username
     
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="like")

    def __str__(self):
        return self.user.username

    def get_user_display(self):
        return self.user.username    

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username     