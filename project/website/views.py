# website/views.py  
from django.shortcuts import render  
from .models import *
def home(request):  
    sidebar_items = Sidebar.objects.all()
    main_about = MainAbout.objects.all()  
    faqs = FAQ.objects.all()  
    services = Services.objects.all()  


    return render(request, 'home.html',{'sidebar_items': sidebar_items,'main_about': main_about, 'services':services, 'faqs':faqs})  # Ensure you have a template at this path