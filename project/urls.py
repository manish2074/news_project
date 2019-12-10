"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from news.views import NewsTemplateView,contact_us,SearchResultsView
from accounts.views import contact
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', NewsTemplateView.as_view(), name='home'),
    path('account/',include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('news/',include('news.urls')),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name="password_reset"),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_done.html'), name="password_reset_done"),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name="password_reset_complete"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name="password_reset_confirm"),
    path('contact/',contact_us,name='contact'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('contact/mail/',contact,name='contact_mail')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)