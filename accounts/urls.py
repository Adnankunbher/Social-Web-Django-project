from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.signup,name='signup_page'),
    path('login/',views.login_view,name='login_page'),
]
urlpatterns= urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
