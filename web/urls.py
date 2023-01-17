from django.urls import path
from .views import posts, PostView, homepage, sendEmail


urlpatterns = [
    path('', homepage, name='homepage'),
    path('posts/', posts, name='posts'),
    path('post/<slug:slug>/', PostView.as_view(), name='post'),
    # path('profile/', profile, name='profile'),
    path('send_mail/', sendEmail, name='send_email')
     
]