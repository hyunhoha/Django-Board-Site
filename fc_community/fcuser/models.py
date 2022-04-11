from django.db import models

# Create your models here.

class Fcuser(models.Model):
    user_name = models.CharField(max_length=32, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registerdttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    user_email = models.EmailField(max_length=128, verbose_name='유저 이메일')
    
    def __str__(self) -> str:
        return self.user_name
    
    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자'