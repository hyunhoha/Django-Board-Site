from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .form import LoginForm

# Create your views here.

def home(request):
    user_id = request.session.get('user')
    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        
    return render(request, 'home.html')

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/fcusers/home/')

def login(request):
    # return render(request, 'login.html', {'form' : form})

    if request.method == 'GET':
        form = LoginForm()
    elif request.method =='POST':
        form = LoginForm(request.POST)
        # form.user_name = request.POST.get('user_name')
        # form.password = request.POST.get('password')
        if form.is_valid():
            request.session['user'] = form.user_id
            # return redirect('/')
            # return redirect('/board/list')
            return redirect('/fcusers/home')
            # return render(request, 'login.html', {'form' : form})
        else:
            pass
            # return render(request, 'login.html', {'form' : form})
            
            # return HttpResponse("Not Valid")
        
    return render(request, 'login.html', {'form' : form})

# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     elif request.method == 'POST':
#         user_name = request.POST.get('user_name', None)
#         password = request.POST.get('password', None)
        
#         res_data = {}
        
#         if not (user_name and password):
#             res_data['error'] = '모든 값을 입력해야 합니다.'
#         else:
#             fcuser = Fcuser.objects.get(user_name=user_name)
#             if check_password(password, fcuser.password):
#                 # 비밀번호 동일
#                 pass
#             else:
#                 res_data['error'] = '비밀번호가 다릅니다.'
    
#         return render(request, 'login.html', res_data)
                
        
def register(request):
    
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        
        user_name = request.POST.get('user_name',None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re-password',None)
        user_email = request.POST.get('user_email', None)
        
        res_data = {}
                
        if not (user_name and password and re_password and user_email):
            res_data['error'] = "모든 값을 입력해야 합니다."
        elif password != re_password:
            res_data['error'] = "비밀번호가 다릅니다!"

        else:
            fcuser = Fcuser(
                user_name = user_name,
                password = make_password(password),
                user_email = user_email,
            )
            
            fcuser.save()
        
        return render(request, 'register.html', res_data)
    
    # return render(request, 'register.html')