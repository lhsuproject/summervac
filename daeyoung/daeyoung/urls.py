from django.contrib import admin
from django.urls import path
from shop import views
from account import views as account_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('shop',views.shop,name='shop'),
    path('ItemCreate',views.ItemCreate,name='ItemCreate'),
    path('goodsRegist',views.goodsRegist, name='goodsRegist'),
    path('detail/<int:item_id>',views.detail,name='detail'),
    path('my/',views.my,name='myPage'),
    
    
    path('login',account_views.login, name='login'),
    path('logout/', account_views.logout, name='logout'),
    path('regist',account_views.regist, name='regist'),
    path('create',account_views.create, name='create'),
    path('myPage', account_views.myPage, name='myPage'),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
