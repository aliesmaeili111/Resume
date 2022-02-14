from django.shortcuts import render
from. models import Article,Contacts
from .forms import ContactForm
# Create your views here.

def home(request):
    
    article = Article.objects.all()
    form = ContactForm()
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
            
    context = {
        'articles':article,
        'forms':form,
    }
    
    return render(request,'blog/base.html',context)

