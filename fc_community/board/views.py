from django.shortcuts import render, redirect

from board.form import BoardForm
from .models import Board
from fcuser.models import Fcuser
from django.http import Http404
from django.core.paginator import Paginator
from tag.models import Tag

# Create your views here.

def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')
    return render(request, 'board_detail.html', {'board':board})

def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 2) # 페이지당 2개씩 나오게 설정
    boards = paginator.get_page(page)
    return render(request, 'board.html', {'boards':boards})

def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcusers/login/')
    form = BoardForm()
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = Board()
            user_id = request.session.get('user') 
            fcuser = Fcuser.objects.get(pk=user_id)
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()
            
            tags = form.cleaned_data['tags'].split(',')
            for tag in tags:
                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tag.add(_tag)
                
            return redirect('/board/list')
    
    else:
        form = BoardForm()
        
    return render(request, 'board_write.html', {'form' : form})
    
        
    # else:
        
    
