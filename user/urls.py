from django.urls import path
from . import views

urlpatterns = [
    path('',views.Bloghome, name='bloghome'),
    path('add_post/',views.add_post, name='add_post'),
    path('postpage/<int:post_id>/',views.postpage, name='postpage'),
    path('postComment/<int:post_id>/',views.postComment, name='postComment'),
    path('dashboard/',views.dashboard, name='dashboard'),

    path('signup',views.signup,name='signup'),
    path('login',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout'),

    path('changepass/', views.MyPasswordChangeView.as_view(), name='changepass'), 
    path('password_change_done/', views.MyPasswordChangeDoneView.as_view(), name='password_change_done'),
    
    path('password_reset/', views.MyPasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/', views.MyPasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/', views.MyPasswordResetCompleteView.as_view(),name='password_reset_complete'),

]