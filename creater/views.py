from django.shortcuts import render
from .forms import organiserform

# Create your views here.
def addorganiser(request):
    if request.method == "POST":
        form = organiserform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = organiserform()
    
    return render(request,"createrform.html",{'form':form})