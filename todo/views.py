from django.shortcuts import render,redirect
from django.contrib import messages

from .forms import TodoForm
from .models import Todo

def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
         form.save()
         messages.success(request, "Todo item added successfully!")
         return redirect('todo')
        
    form = TodoForm()
    page = {
        "forms":form,
        "list":item_list,
        "title": "TODO LIST",
    }
    return render(request,'todo/index.html',page)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request,"item Removed!")
    return redirect('todo')
'''
1. form = TodoForm(request.POST)
This line initializes the form with the data submitted via the POST request (request.POST). 
When a form is submitted in an HTML form, the data gets passed to the server using the POST method.
TodoForm(request.POST): 
creates an instance of the form (TodoForm) and populates it with the data 
submitted by the user. 
This is crucial because Django needs to validate and process the user input.

2. if form.is_valid():
This checks whether the data entered in the form is valid 
according to the rules defined by the TodoForm and the corresponding Todo model.

The form will be considered valid if:
All required fields in the TodoForm (i.e., title, details, and date) 
have been provided.


page = { 
    "forms": form, 
    "list": item_list, 
    "title": "TODO LIST", 
} 
return render(request, 'todo/index.html', page)


Explanation:
page = {}: 
This is a dictionary that holds the data to be passed to the template. 

"forms":form: 
The form instance (form) is passed to the template with the key "forms". 
This allows the template to render the form (TodoForm) and display it for users to add new items. 


"list":item_list: 
item_list contains a list of all Todo items, which were retrieved from the database 
and ordered by their date. 
This allows the template to display a list of existing to-do items.


"title":"TODO LIST": 
This is a static string representing the title of the page, which can be used in the template to display a heading or title tag.


return render(request, 'todo/index.html', page):
The render function combines a request, the template ('todo/index.html'), and the context dictionary (page).
The template index.html will use the provided context to render the form and the to-do list on the webpage.
The page dictionary is passed to the template so that these variables (forms, list, and title) are available in the HTML file.

Example in the template:
{{ forms }}: The form is displayed on the webpage for users to interact with.
{% for i in list %}: The list of to-do items is looped over, and each item is rendered on the page.

'''