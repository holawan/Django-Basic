from django.shortcuts import render,redirect
from shortener.models import Users
# Create your views here.

def index(request) :
    #user중 이름이 admin인 것을 필터해서 그중 첫번째 것을 가져와라
    #없으면 none
    user = Users.objects.filter(username="admin").first()
    # user = Users.objects.get(username='admin')
    #email이 있으면 email에 email을 입력하고 아니면 anonymous User로 선언해라 
    email = user.email if user else "Anonymous User!"

    print(email)
    print(request.user.is_authenticated)
    #로그인이 되어있는지 확인 
    if request.user.is_authenticated is False :
        email = "Anonymous User!"

        print(email)
    return render(request,"base.html",{"welcome_msg" : f"Hello {email}!"})


def redirect_test(request):
    print("Go Redirect")
    #여기로 들어오면 index로 redirect하라 
    return redirect("index")



