from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout_page,name='logout_page'),
    path('<int:pk>/',views.delete_post),
    path('<str:username>/',views.profile_info), 
    path('post',views.Post_id),  
    path('',views.index,name='home'),  
]
urlpatterns= urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)