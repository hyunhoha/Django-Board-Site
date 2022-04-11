from django import forms
# from tag import Tag

class BoardForm(forms.Form):
    title = forms.CharField(error_messages={
        'required' : '제목을 입력하세요',
    },max_length=64, label="제목")
    contents = forms.CharField(error_messages={
        'required' : "내용을 입력하세요",
    },label='내용', widget=forms.Textarea)
    
    # tags = forms.cleaned_data('tags').split(',')
    tags = forms.CharField(required=False, label="태그")
    
    # def clean(self):
    #     if user_name and password:
    #         try:
                
    #         except Fcuser.DoesNotExist:
    #             self.add_error('username', '아이디가 없습니다.')
    #             return 
                