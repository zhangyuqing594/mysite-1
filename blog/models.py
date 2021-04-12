from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from read_statistics.models import ReadNumExpandMethod,ReadDetail
from django.urls import reverse

# Create your models here.


class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    
    def __str__(self):
        return self.type_name

class Blog(models.Model,ReadNumExpandMethod):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType,on_delete=models.CASCADE)
    #一篇博客对应一种博客类型
    content = RichTextUploadingField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    read_details= GenericRelation(ReadDetail)
    created_time= models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def get_url(self):
        return  reverse('blog_detail',kwargs={'blog_pk': self.pk})
    def get_email(self):
        return self.author.email
  
    def __str__(self):
        return "<Blog:%s>"% self.title

    class Meta:
        ordering=['-created_time']
            