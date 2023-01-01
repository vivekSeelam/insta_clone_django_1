from django.urls import path
from . import views

# localhost:8000/users/index
# localhost:8000/users/
# localhost:8000/

urlpatterns = [
    path('signup/', views.signup, name="users_main_view"),
    path('index/', views.index, name="users_sign_up"),
    path('add/', views.create_user, name="create_user_api")
]