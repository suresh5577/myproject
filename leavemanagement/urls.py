"""leavemanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from django.views.generic import TemplateView, ListView, CreateView, UpdateView,\
 DeleteView
from main.views import user_register, home_view, logout_view, LeaveCreateView
from main.models import Leave, LeaveType
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("api/",include("service.urls")),
    path("logout/",logout_view),
    path('admin/', admin.site.urls),
    path('', home_view),
    path('register/', user_register),
    path('index/', TemplateView.as_view(template_name="main/index.html")),
    path('leaves/', login_required(ListView.as_view(
        model=Leave,
        #template_name="main/leave_list.html"
        ))),
    path('leave_create/', login_required(LeaveCreateView.as_view())),
    re_path('leave_update/(?P<pk>[0-9]+)',login_required(UpdateView.as_view(
        model=Leave,
        fields=["desc","type","leavedate","user"],
        success_url="/leaves",
        template_name="main/leave_update_form.html"
        ))),
    re_path("leave_delete/(?P<pk>[0-9]+)",login_required(DeleteView.as_view(
            model=Leave,
            success_url="/leaves",
            #template_name="main/leave_confirm_delete.html"
        ))),
    path('leavetypes/', login_required(ListView.as_view(
        model=LeaveType,
        #template_name="main/leave_list.html"
        ))),
    path('leavetypes_create/', login_required(CreateView.as_view(
        model=LeaveType,
        fields="__all__",
        #fields=["desc","type","leavedate","user"],
        success_url="/leavetypes/",
        #template_name="main/leave_form.html"
        ))),
    re_path('leavetypes_update/(?P<pk>[0-9]+)',login_required(UpdateView.as_view(
        model=LeaveType,
        #fields=["desc","type","leavedate","user"],
        fields="__all__",
        success_url="/leavetypes",
        template_name="main/leavetype_update_form.html"
        ))),
    re_path("leavetypes_delete/(?P<pk>[0-9]+)",login_required(DeleteView.as_view(
            model=LeaveType,
            success_url="/leavetypes",
            #template_name="main/leave_confirm_delete.html"
        )))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
