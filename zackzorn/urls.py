from django.urls import path, include
from django.views.generic.base import RedirectView

from zackzorn import views

app_name = 'zackzorn'

urlpatterns = [
    # path('', RedirectView.as_view(pattern_name='zackzorn:screen_list'), name='index'),
    # path('screen/<str:slug>/', views.ScreenView.as_view(), name='view_screen'),
    # path('screens/', views.ScreenListView.as_view(), name='screen_list'),
]

