from django import forms

class CreateNewTasks(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    description = forms.CharField(label="Descripción de la tarea",widget=forms.Textarea(attrs={'class':'input'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label='Nombre del Poryecto', max_length=200, widget=forms.TextInput(attrs={'class':'input'}))