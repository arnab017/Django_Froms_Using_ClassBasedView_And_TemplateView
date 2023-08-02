from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,FormView
from app.forms import *
# Create your views here.

class Data_Rendering(TemplateView):
    template_name = 'Data_Rendering.html'
    
    #-----if we want to render context to frontend we have to use get_context_data
    #-----so inorder to use get_context_data we need to use method overriding
    #-----after that we need to perform chaining to create dictionary and return as a context
    def get_context_data(self,**kwargs):
        ECDO = super().get_context_data(**kwargs)
        ECDO['name'] = 'CONTEXT DATA'
        return ECDO

#-----by using template view we are taking the input from the user and inserting into database
class Employee_Form_Insert(TemplateView):
    template_name = 'Employee_Form_Insert.html'
    
    def get_context_data(self,**kwargs):
        ECDO = super().get_context_data(**kwargs)
        SFO = Employee_Form(label_suffix='')
        ECDO['SFO'] = SFO
        return ECDO
    
    def post(self,request):
        SFD=Employee_Form(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('<center><h1 style="font-family:Arial">Data Inserted Successfully</h1></center>')

class Employee_Form_Insert_FormView(FormView):
    template_name = 'Employee_Form_Insert_FormView.html'
    #-----now the form class will perform all the operation like -- get_context_data,call super(), create form object
    form_class = Employee_Form
    #-----for validation we have to use form_valid method
    def form_valid(self,form):  #-----form is a variable which will store the collected data
        form.save()
        return HttpResponse('<center><h1 style="font-family:Arial">Data Inserted Successfully</h1></center>')
        