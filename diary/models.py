from functools import update_wrapper
from os import truncate
from django.db import models
from accounts.models import CustomUser



# Create your models here.
class Diary(models.Model):
    user = models.ForeignKey(CustomUser,verbose_name='ユーザー' ,on_delete=models.PROTECT)
    title = models.TextField(verbose_name='タイトル',max_length=40)
    content =models.TextField(verbose_name='本文',blank=True,null=True)
    photol = models.ImageField(verbose_name='写真2',blank=True,null=True)
    photol = models.ImageField(verbose_name='写真1',blank=True,null=True)
    photol = models.ImageField(verbose_name='写真3',blank=True,null=True)
    created_at= models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    update_at= models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    class Meta:
        verbose_name_plural='Diary'
        
    def __str__(self):
        return self.title
    
