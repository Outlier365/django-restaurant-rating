# 🍽️ Django Restaurant Rating Web App

一個使用 **Django** 開發的餐廳評論網站。  
使用者可以註冊帳號、登入、分享餐廳評論，並且系統會依照評分推薦最高分餐廳。

🔗 **Live Demo**  
https://django-restaurant-rating.onrender.com  

⚠️ 由於使用 Render 免費方案，網站在閒置後可能會進入休眠。  
第一次開啟可能需要 **30–60 秒**。

Demo Account:
```
username: Lilly
password: lll123456
```

## 📸 Screenshots
- 新增評論
<img width="764" height="440" alt="新增評價" src="https://github.com/user-attachments/assets/e6ad2589-1991-4883-bfef-490e065c36f6" />
- 若尚未登入自動跳轉至登入介面
<img width="211" height="199" alt="若尚未登入自動跳轉至登入介面" src="https://github.com/user-attachments/assets/cef4a12d-59a3-475b-94a7-9e750786e472" />
- 使用者只有權限刪除和更新自己上傳的評價
<img width="748" height="433" alt="使用者只有權限刪除和更新自己上傳的評價" src="https://github.com/user-attachments/assets/3810e6db-e75e-4886-ae4c-3b0d5b26bd05" />
- 輸入信箱點擊我要最佳推薦
<img width="554" height="428" alt="輸入信箱點擊我要最佳推薦" src="https://github.com/user-attachments/assets/ad5d5532-d200-4218-846d-00b36f39b5b8" />
- 收到推薦信
<img width="284" height="241" alt="收到推薦信" src="https://github.com/user-attachments/assets/e9128ec8-1d82-4c26-83c8-8d65b67b3d9c" />



## ✨ Features

### 使用者系統
- 使用者註冊 / 登入 / 登出
- Django Authentication System

### 餐廳評論系統
- 新增餐廳評論
- 編輯餐廳評論
- 刪除餐廳評論
- 顯示餐廳評分與評論內容

### 權限控制
- 只有 **建立該筆資料的使用者** 才能編輯或刪除
- 其他使用者只能瀏覽

### Email 推薦功能
- 使用 **Resend Email API**
- 輸入 Email 即可收到 **最高評分餐廳推薦**

---

## 🧠 技術重點

### Django Class-Based Views
使用 CBV 管理 CRUD 操作：

- `Home`
- `Add_Restaurant`
- `Edit_Restaurant`
- `Delete_Restaurant`

### 權限控制設計


Restaurant model 綁定 owner：
```python
owner = models.ForeignKey(User, on_delete=models.CASCADE)
```

在 view 中進行權限檢查：
```python
if data.owner != request.user:
    return HttpResponseForbidden("你沒有權限編輯此筆資料")
```
Template 只顯示自己的編輯按鈕：

```django
{% if user.is_authenticated and rst.owner_id == user.id %}
```
## 🛠️ Tech Stack
### Backend
- Django
- Python
### Database
- SQLite (development)
### Authentication
- Django Authentication System
### Email Service
- Resend API
### Deployment
- Render
- Gunicorn
### Version Control
- Git
- GitHub

## 🚀 Deployment
專案部署在 Render Web Service
Start Command
```
gunicorn myproject_restaurant_rating.wsgi:application
```
Build Command
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput


## 📂 Project Structure

```
myproject_restaurant_rating
│
├─ manage.py
├─ requirements.txt
├─ Procfile
│
├─ rating
│   ├─ models.py
│   ├─ views.py
│   ├─ forms.py
│   ├─ urls.py
│
├─ templates
│   ├─ home.html
│   ├─ add-restaurant.html
│   ├─ edit-restaurant.html
│   ├─ login.html
│   └─ signup.html
```
## ⭐ Key Highlights
- Django authentication system
- Owner-based permission control
- Email recommendation system
- Full CRUD restaurant review system
- Deployed on Render

## 👨‍💻 Author
Jerry Shen

GitHub
https://github.com/Outlier365
