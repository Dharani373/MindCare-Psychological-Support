from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_view,name = 'login'),
    path('signup/',views.signup_view,name = 'signup'),
    path('home/',views.home_view,name = 'home'),
    path('logout/', views.logout_view, name='logout'),
    path("stress-check/", views.stress_check_view, name="stress_check"),
    path("stress-result/", views.stress_result_view, name="stress_result"),
    path("stress-history/", views.stress_history_view, name="stress_history"),
    path("ai-support/", views.ai_support_view, name="ai_support"),
    path("resources/", views.resources_view, name="resources"),
    path("find-help/", views.find_doctors_view, name="find_doctors"),
    path("profile/", views.profile_view, name="profile"),
]
