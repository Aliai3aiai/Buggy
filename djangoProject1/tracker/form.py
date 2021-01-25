from django import forms
from .models import Project, Task
from django.contrib.admin.widgets import AdminDateWidget

class ProjectForm(forms.Form):
    model = Project
    title = forms.CharField(label='Enter Title', help_text='Custom CMS',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={'cols': "80", 'rows': "10", 'class': 'form-control'}))

class TaskForm(forms.Form):
    model = Task
    title = forms.CharField(label='Enter Title', help_text='Custom CMS',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    severity = forms.IntegerField(max_value=10)
    open_date = forms.DateTimeField(widget=AdminDateWidget)
    close_date = forms.DateTimeField(widget=AdminDateWidget)
    status = forms.IntegerField()
