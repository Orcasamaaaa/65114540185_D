from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views.generic import *
from 
# Create your views here.
class CourseListView(ListView):
    model = Course
    context_object_name = 'Courses'
    template_name = 'coures_list.html'

class CourseEditView(UpdateView):
    fields = ['id','teacher']
    model = Course
    template_name = 'edit.html'
    success_url = reverse_lazy('course_list')
