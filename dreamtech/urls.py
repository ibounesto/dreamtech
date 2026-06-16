from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
import shop.views 
from django.conf import settings
from django.conf.urls.static import static
import authentication.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', authentication.views.register_user, name='signup'),
    path('', shop.views.HomeView.as_view(), name='home'),
    path('register/article/', shop.views.register_article, name='register_article'),
    path('article/<int:pk>/', shop.views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/update/<int:pk>/', shop.views.ArticleUpdateView.as_view(), name='update_article'),
    path('article/delete/<int:pk>/', shop.views.ArticleDeleteView.as_view(), name='delete_article'),
    path('user/<int:pk>/', authentication.views.UserDetailView.as_view(), name='user_detail'),
    path('user/update/<int:pk>/', authentication.views.UserUpdateView.as_view(), name='update_user'),
    path('user/articles/', shop.views.user_articles, name='user_articles'),
    path('user/delete/<int:pk>/', authentication.views.UserDeleteView.as_view(), name='delete_user'),
    path('add_to_cart/<int:pk>/', shop.views.add_to_cart, name='add_to_cart'),
    path('cart/', shop.views.cart, name='cart'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)