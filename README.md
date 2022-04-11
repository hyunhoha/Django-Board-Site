# Django-Board-Site

### FastCampus Lecture Clone Coded

게시판을 만들어보았다. Login, Logout, Register, Board List, writing, See Detail (CRUD)

APPS : fcuser (유저 데이터), Board(게시판 글 관리), Tag(글 태그 관리)

# Models
 ### Fcuser :
- user_name : Char (사용자명)
- password : Char (비밀번호)
- registerdttm : DateTime (등록시간)
- user_email : Email (유저 이메일)
  
 ### Board :
- title : Char (제목)
- contents : Text (내용)
- writer : Foreign Key (Fcuser) (작성자)
- registereddttm : DateTime (작성시간)
- tag : ManyToMany (태그)
   
 ### Tag :
- name : Char (태그명)
- registeredttm : Datetime (등록시간)
   
## 기타사항
- 세션 사용 : view에서 request.session['attribute']
- admin에서 사용할 메타데이터 : model 아래에 Meta 클래스 작성, db_table, verbose_name, verbose_name_plural 설정하기.
- 게시글마다 주소에 글 번호 할당 : urlpatterns에 path(<int:pk>/) 형태로 타입과 받을 변수 타입명을 설정해주고 view 내 함수에서 pk 변수로 같이 받는다.
- view 함수에서 request.method == "POST, GET" 으로 GET, POST 요청별로 처리해줄 수 있다.
- form을 사용해보기 : 모델과 별개로, html에서 편하게 쓰기 위함. clean함수를 오버라이드 하여 데이터 유효성 검사를 할 수 있다.
- form으로 POST하기 : <form method="POST" action="."> -> form 변수를 입력받는 것이 가능.
- 모델 데이터 생성 : Model import 후 클래스 생성 후, save()함수를 사용하면 db에 바로 쉽게 저장된다.
   

   
   
