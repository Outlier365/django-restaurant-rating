from django.urls import path,include
from .views import Home,Add_Restaurant,Delete_Restaurant,Edit_Restaurant,send_top_score_email,SignUp
urlpatterns = [

    path("",Home.as_view(),name='Home'),
    path('add-restaurant/',Add_Restaurant.as_view(),name='add-restaurant'),
    path('delete-restaurant/',Delete_Restaurant.as_view(),name="delete-restaurant"),
    path('edit-restaurant/<int:id>/',Edit_Restaurant.as_view(),name="edit-restaurant"),
    path('send-email-route/',send_top_score_email, name='send_email'),
    path('signup/', SignUp.as_view(), name='signup'),
]
