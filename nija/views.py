from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.
# def index(request):
#     return render(request,'index.html')

def base(request):
    return render(request, 'base.html')




def form_one_view(request):
    form = DojoForm() # form your working with 
    second_form = NijaForm()

    if request.method == 'POST':
        form = DojoForm(request.POST)
        second_form = NijaForm(request.POST)
        if form.is_valid():
            form.save()
        if second_form.is_valid():
            second_form.save()
    objs_ = Nija.objects.all()
    objs = Dojo.objects.all()
    context = {'form':form,'second_form':second_form, 'objs':objs, 'objs_':objs_}
    return render(request, 'index.html', context)

# def form_two_view(request):
#     second_form = NijaForm() # form your working with 

#     if request.method == 'POST':
#         second_form = NijaForm(request.POST)
#         if second_form.is_valid():
#             second_form.save()
#     objs = Nija.objects.all()
#     context = {'second_form':second_form, 'objs':objs}

#     return render(request, 'other.html', context)