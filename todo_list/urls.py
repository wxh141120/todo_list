"""todo_list URL Configuration

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
# import todo.urls
# import todo.views as todo
import todo.views as todo

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('todo/', include(todo.urls)),
    path('get/', todo.get, name='get'),
    path('add/', todo.add, name='add'),
    path('delete/', todo.delete, name='delete'),
    path('edit/', todo.edit, name='edit'),
]
