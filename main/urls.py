from django.urls import path
from .views import (index, add_savol, category, Login,
                    profile, check,
                    savol, savollar, signup, add_javob, 
                    qidirish, Logout, edit_profile, delete_javob, delete_savol)




urlpatterns = [
    path("", index, name="index"),
    path("add_savol/", add_savol, name="add_savol"),
    path("category/", category, name="category"),
    path("login/", Login, name="login"),
    path("profile/", profile, name="profile"),
    path("profile/<str:username>/", profile, name="profile"),
    path("savol/<int:id>/", savol, name="savol"),
    path("savollar/", savollar, name="savollar"),
    path("savollar/<int:id>/", savollar, name="savollar"),
    path("savollar/<str:username>/", savollar, name="savollar"),
    path("signup/", signup, name="signup"),
    path("add_javob/<int:id>", add_javob, name="add_javob"),
    path("qidirish/", qidirish, name="qidirish"),
    path("logout/", Logout, name="logout"),
    path("check/<int:savol_id>/<int:javob_id>/", check, name="check"),
    path("edit_profile/", edit_profile, name="edit_profile"),
    path("delete/<int:savol_id>/<int:javob_id>/", delete_javob, name="delete_javob"),
    path("delete/<int:savol_id>/", delete_savol, name="delete_savol")
]

