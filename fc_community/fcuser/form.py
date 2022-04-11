from django import forms

from .models import Fcuser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=32, label="사용자 이름",
                                error_messages={
                                    'required' : "이름을 입력해주세요"
                                })
    password = forms.CharField(max_length=32, label= "비밀번호", widget=forms.PasswordInput,
                               error_messages={
                                   'required' : "비밀번호를 입력해주세요"
                               })
    
    def clean(self):
        cleaned_data = super().clean()
        user_name = cleaned_data.get('user_name')
        password = cleaned_data.get('password')
        
        if user_name and password:
            try:
                fcuser = Fcuser.objects.get(user_name = user_name)
            except Fcuser.DoesNotExist:
                self.add_error('user_name', '아이디가 없습니다.')
                return
            
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호가 틀렸습니다')
            else:
                self.user_id = fcuser.id
        