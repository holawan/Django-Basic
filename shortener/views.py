from django.shortcuts import render,redirect
from shortener.forms import RegisterForm
from shortener.models import Users
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.contrib.auth import login, authenticate

def index(request) :
    #user중 이름이 admin인 것을 필터해서 그중 첫번째 것을 가져와라
    #없으면 none'
    # print(request.user.pay_plan)
    user = Users.objects.filter(id=request.user.id).first()
    # print(request.user.pay_plan.name)
    # user = Users.objects.get(username='admin')
    #email이 있으면 email에 email을 입력하고 아니면 anonymous User로 선언해라 
    email = user.email if user else "Anonymous User!"
    # print(email)
    print("Logged In?", request.user.is_authenticated)
    #로그인이 되어있는지 확인 
    if request.user.is_authenticated is False :
        email = "Anonymous User!"
    print(email)
    return render(request,"base.html",{"welcome_msg" : f"Hello {email}!"})


@csrf_exempt
def get_user(request, user_id):
    print(user_id)
    if request.method == "GET":
        #쿼리셋 형태로 받은 abc에 들어있는 값과 xyz에 들어있는 값을 리턴한다.
        # eX) http://127.0.0.1:8000/get_user/1?abc=123&xyz=안녕
        abc = request.GET.get("abc")
        xyz = request.GET.get("xyz")
        user = Users.objects.filter(pk=user_id).first()
        #리스트 형태로 데이터를 넘겨주면 Django HTML에서 for문으로 출력 가능 
        return render(request, "base.html", {"user": user, "params": [abc, xyz]})
    elif request.method == "POST":
        username = request.GET.get("username")
        #username을 방금 요청받은 이름으로 변경한다. 
        if username:
            user = Users.objects.filter(pk=user_id).update(username=username)

        return JsonResponse(dict(msg="You just reached with Post Method!"))

def register(request) :

    if request.method=='POST' :
        form = RegisterForm(request.POST) 
        msg = "올바르지 않은 데이터입니다."

        if form.is_valid() :
            form.save()
            username= form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            msg="회원가입 완료"
        return render(request,"register.html",{"form":form,"msg":msg})
    else :
        form = RegisterForm()
    return render(request, "register.html",{"form" : form})