from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
# This form will be used to collect user input to create or 
# update Todo items in the database.
    class Meta:
        model = Todo
        fields = '__all__'

'''
from django import forms:

This imports Django's form functionality, which allows you to create forms 
in Python to handle user input.


from .models import Todo:
This imports the Todo model from the current app's models.py. 
It's used to map the form fields to the model's fields.



class TodoForm(forms.ModelForm):
This defines a form class named TodoForm that extends Django's ModelForm class.
A ModelForm is a type of form that is automatically generated based on a 
model’s fields.

The Django ModelForm that automatically generates a form based on the fields in your Todo model.



class Meta:
The Meta class defines metadata for the TodoForm.

model = Todo:
This tells Django that this form is based on the Todo model.

fields = '__all__':
This specifies that all the fields in the Todo model should be included in the form. 
Instead of specifying individual fields,
this shortcut includes all the model’s fields in the form.




'''