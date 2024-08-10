from django.shortcuts import render,redirect
from website.forms import Contacfrom
from website.models import Banner

# Create your views here.

def index(request):
    banner = Banner.objects.all()
    context = {

        'banner' : banner
    }
    return render(request,'website/index.html',context)

def contact(request):
    if request.method == 'POST':
        form = Contacfrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Contacfrom()
    return render(request,'website/contact.html',{'form':form})




  

