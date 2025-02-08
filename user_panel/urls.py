from django.urls import path
from . import views
urlpatterns = [
    path('', views.UserPanelView.as_view(), name="user_panel_page"),
    path('change-password/', views.ChangePasswordView.as_view(), name="change_password"),
    path('edit-profile/', views.EditUserPanelView.as_view(), name="edit_user_profile")

]