from django.shortcuts import render,redirect
from website.forms import Contacfrom

# Create your views here.

def index(request):
    return render(request,'website/index.html')

# def contact(request):
#     return render(request,'website/contact.html')


def contact(request):
    if request.method == 'POST':
        form = Contacfrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Contacfrom()

    return render(request,'website/contact.html',{'form':form})
  

