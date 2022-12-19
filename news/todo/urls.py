"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from homepage.views import HomepageView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("django.contrib.auth.urls")),
    path('', HomepageView.as_view(), name='home'),
    path('todo-list/', HomepageView.todo_list, name='todo-list'),
    path('todo-create/', HomepageView.todo_create, name='todo-create'),
    path('todo-edit/', HomepageView.todo_edit, name='todo-edit'),
    path('todo-delete/', HomepageView.todo_delete, name='todo-delete'), 
    path('', csrf_exempt(HomepageView.as_view()), name='home'),
]
