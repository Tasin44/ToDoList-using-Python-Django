from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('',views.index,name="todo"), #maps to the index view, displaying the list of to-do items.
    path('del/<str:item_id>/', views.remove, name="del"),#handles the deletion of a to-do item.
    path('admin/', admin.site.urls),#gives access to Django’s admin interface for managing data.
]
'''
from django.contrib import admin:
This line imports Django's built-in admin module, 
which allows for managing your application’s models via an automatically generated admin interface.

from django.urls import path:
This imports the path function from Django's urls module. 
The path function is used to define URL routes for your web application.

from todo import views:
This imports the views module from the todo app. 
It allows you to connect the URLs to the corresponding view functions 
defined in views.py, such as index and remove.



urlpatterns = []:
This is a list that holds the URL patterns (routes) for the application. 
Each path function inside the list maps a specific URL to a corresponding view function.


path('', views.index, name="todo"):
This defines the route for the homepage (an empty string '' means the root URL, e.g., http://127.0.0.1:8000/).
When a user visits the root URL, the index view from views.py will be executed.
The name="todo" provides a name for the URL pattern, 
which allows for reverse URL resolution (e.g., using redirect('todo') in your views).


path('del/<str:item_id>/', views.remove, name="del"):
This defines a route for deleting an item based on its item_id.

The <str:item_id> is a URL parameter where item_id is a string that will be passed to the remove view. 
It will capture the ID of the item you want to delete.
For example, visiting http://127.0.0.1:8000/del/5/ would trigger
the remove view with item_id equal to 5.

The name="del" allows this URL to be referenced in the code 
(e.g., in templates or views).


path('admin/', admin.site.urls):
This maps the /admin/ URL to Django's built-in admin site.
It allows you to manage your models (such as Todo) 
from the admin interface (http://127.0.0.1:8000/admin/).
'''




