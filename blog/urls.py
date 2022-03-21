from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import  PostList,PostDetail


urlpatterns = [
   path("post/",PostList.as_view(), name="post"),
   path("post/<int:pk>/",PostDetail.as_view(), name="post_detail")

  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)