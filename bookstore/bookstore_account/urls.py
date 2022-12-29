from django.urls import path
from django.contrib.auth import views
from .views import edit_my_book, log_out, login_page, myBooks, register,login_wave, user_account, remove_my_book
from .forms import MyPasswordChangeForm, MyResetPassForm, MySetPassForm


urlpatterns = [
    path('register',register),
    path('login',login_wave),
    path('logout',log_out),
    path('user',user_account),
    path('user/my-books',myBooks),
    path('remove-my-book/<detail_id>', remove_my_book), 
    path('edit-my-book/<detail_id>', edit_my_book), 
]


    # path("logout/", views.LogoutView.as_view(), name="logout"),
urlpatterns += [
    path(
        "password_change/", 
        views.PasswordChangeView.as_view(template_name='changePassword.html',
            form_class=MyPasswordChangeForm,
        ), 
        name="password_change",
    ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(template_name='passwordDone.html'),
        name="password_change_done",
        
    ),
    path("password_reset/", views.PasswordResetView.as_view(
        template_name='resetPassword.html',
        form_class=MyResetPassForm,
    ), name="password_reset"),

    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(
            template_name='resetPasswordDone.html'
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(
            template_name='resetPasswordConfirm.html',
            form_class=MySetPassForm,
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(
            template_name='resetPasswordComplete.html'
        ),
        name="password_reset_complete",
    ),
]
