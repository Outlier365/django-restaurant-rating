import os
import resend
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import  Restaurant
from .forms import RestaurantForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



resend.api_key = os.environ.get("RESEND_API_KEY")
# Create your views here.
class Home(View):
    def get(self,request):
        restaurant_data=Restaurant.objects.all()
        return render(request,'home.html',{'rstdata':restaurant_data})

class Add_Restaurant(LoginRequiredMixin,View):
    login_url = "/accounts/login/" 

    def get(self, request):
        fm = RestaurantForm()
        return render(request, 'add-restaurant.html', {'form': fm})

    def post(self, request):
        fm = RestaurantForm(request.POST)
        if fm.is_valid():
            obj = fm.save(commit=False)   # 先不要存
            obj.owner = request.user      # ✅ 綁定建立者
            obj.save()
            return redirect('/')
        return render(request, 'add-restaurant.html', {'form': fm})

class Delete_Restaurant(LoginRequiredMixin, View):
    login_url = "/accounts/login/"

    def post(self, request):
        id = request.POST.get('id')
        data = get_object_or_404(Restaurant, id=id)

        # ✅ 權限檢查：不是 owner 就不給刪
        if data.owner != request.user:
            return HttpResponseForbidden("你沒有權限刪除此筆資料")

        data.delete()
        return redirect('/')

class Edit_Restaurant(LoginRequiredMixin, View):
    login_url = "/accounts/login/"

    def get(self, request, id):
        data = get_object_or_404(Restaurant, id=id)

        if data.owner != request.user:
            return HttpResponseForbidden("你沒有權限編輯此筆資料")

        fm = RestaurantForm(instance=data)
        return render(request, 'edit-restaurant.html', {'form': fm})

    def post(self, request, id):
        data = get_object_or_404(Restaurant, id=id)

        if data.owner != request.user:
            return HttpResponseForbidden("你沒有權限編輯此筆資料")

        fm = RestaurantForm(request.POST, instance=data)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        return render(request, 'edit-restaurant.html', {'form': fm})

def send_top_score_email(request):
    if request.method == "POST":
        # 1. 取得使用者在網頁輸入框填寫的信箱
        receiver_email = request.POST.get('user_email')
        
        # 2. 查詢 Restaurant 資料中 score 最高的那一筆
        # order_by('-score') 表示由高到低排序，.first() 取第一筆
        top_restaurant = Restaurant.objects.order_by('-score').first()
        
        if top_restaurant and receiver_email:
            try:
                # 3. 準備郵件內容並透過 Resend 寄出
                params = {
                    "from": "Restaurant App <onboarding@resend.dev>", # 測試期請用 resend 預設寄件者
                    "to": [receiver_email],
                    "subject": f"推薦餐廳：{top_restaurant.name} ",
                    "html": f"""
                        <h1><strong>{top_restaurant.name}</strong></h1>
                        <p>是目前最高分的餐廳</p>
                        <p>分數：<strong>{top_restaurant.score}</strong> 分</p>
                        <p>評價：<strong>{top_restaurant.review}</strong></p>
                        <p>感謝您的查詢</p>
                    """,
                }
                resend.Emails.send(params)
                print("郵件已成功發送！")
            except Exception as e:
                print(f"發送失敗: {e}")
            
        # 寄完後看你要跳轉回原頁面還是成功頁面
        return render(request, 'success.html') 

    return redirect('Home') # 如果不是 POST 請求就回到首頁

class SignUp(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, "registration/signup.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # 註冊完直接登入
            return redirect('/')
        return render(request, "registration/signup.html", {"form": form})