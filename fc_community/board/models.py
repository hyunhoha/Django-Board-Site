from django.db import models
# from fc_community import fcuser
# from fc_community import fcuser


# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    writer = models.ForeignKey('fcuser.Fcuser', verbose_name="작성자", on_delete=models.CASCADE)
    registered_dttm = models.DateTimeField(verbose_name="작성시간", auto_now_add=True)
    tag = models.ManyToManyField('tag.Tag', verbose_name='태그')
    
    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = '패스트캠퍼스 게시글'
        verbose_name_plural = '패스트캠퍼스 게시글'
