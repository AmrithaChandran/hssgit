from django.forms import ModelForm
from django.views import generic
from django.shortcuts import render, redirect

# Create your views here.
from HSSapp.models import User


class Reg_form(ModelForm):
    class Meta():
        model=User
        fields=['username','password','email','phone','state','district','area']


class Register(generic.TemplateView):
    template_name = 'HSSapp/registration.html'
    model_name=User
    form_class=Reg_form

    def get(self,request,*args,**kwargs):
        context={}
        context['form']=self.form_class
        return render(request,self.template_name,context=context)

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect('register')