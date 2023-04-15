from django.urls import path
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from .views import todo_list
# from . import settings
from django.contrib.staticfiles.urls import static
from django.views.generic import RedirectView



urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('pet/', views.perfis_pet, name='perfis_pet'),
    path('todo_list/', views.todo_list, name='todo_list'),
    path('pet/register/', views.register_pet),
    path('pet/register/submit', views.set_pet),
    path('', RedirectView.as_view(url='/pet'))
    #path('home/', views.home, name='home')
]

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)