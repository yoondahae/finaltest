from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', blog_views.signup, name='signup'),
]

# 미디어 파일을 서빙하는 URL 패턴을 추가합니다.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

