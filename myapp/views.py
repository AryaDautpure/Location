from django.shortcuts import render, redirect
from django.views import View
from .models import Country
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.
class CountryView(View):
    def get(self, request ,id=None):
        if id:
            
            data = Country.objects.get(id=id)
            if data.is_active:
                data.is_active = False
                data.save()
            else:
                 data.is_active = True
                 data.save()
            return redirect('/')
        else:
            data = Country.objects.all()
            context = {'data':data }
            return render(request,'html/country.html',context)
        
        
    
    def post(self, request):
        data = Country.objects.all()
        country_name= request.POST.get('country_name')
        slug = request.POST.get('slug')
        code = request.POST.get('code')
        flag = request.FILES.get('flag')
        state_available = request.POST.get('state_available')
        
        if not state_available:
            state_available=False
        if Country.objects.filter(code=code).exists():
            messages.error(request,f"{code} already exists!")
            return redirect('/')
        
        if Country.objects.filter(slug=slug).exists():
            messages.error(request,f"{slug} already exists!")
            
            return redirect('/')
            
        Country.objects.create(name=country_name ,slug=slug,code = code,flag=flag ,is_state_available = state_available)
        messages.success(request,f"Country created successfully")
        return redirect('/')

    
def Delete_view(self,request,id=id):
    data = Country.objects.get(id=id) 
    data.delete()
    messages.success(request,f"{data.name} deleted successfully")
    
    
    