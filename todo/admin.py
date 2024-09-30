from django.contrib import admin
from .models import Todo
# This imports the Todo model from models.py in the current app. 
# It’s needed to make the Todo model manageable via the admin interface.

admin.site.register(Todo)
'''
This registers the Todo model with Django’s admin interface, 
making it possible to view, add, edit, and delete Todo items through the admin panel
(http://127.0.0.1:8000/admin/).
'''