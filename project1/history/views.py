from django.shortcuts import render,redirect
from  .models import *
from .forms import *
from .filters import *
from django.http import JsonResponse
from django.conf import settings
import os
# Create your views here.
def home(request):
    mon_img=historical_data.objects.values_list('Im',flat='True')
    image_urls = [os.path.join(settings.MEDIA_URL, path) for path in mon_img]

    context={'Images':image_urls}
    for value in image_urls:
        print(value)
    return render(request,"index.html",context)

def monument(request,pk):
    inst_to_be_printed=historical_data.objects.get(pk=pk)
    context={'monument':inst_to_be_printed}
    link=inst_to_be_printed.Gmap
    img_url=inst_to_be_printed.Im.url
    context['link']=link
    context['Im_url']=img_url
    return render(request,"monument.html",context)

def contact_us(request):
    if(request.method=='POST'):
        frm=Contactform(request.POST)
        if(frm.is_valid()):
            frm.save()
            return redirect("/")
        else:
            print(frm.errors)
    else:
        frm=Contactform()
    context={'frm':frm}
    return render(request,"Contact Us.html",context)

def search(request):
    monu=historical_data.objects.all()
    
    searched=searchfilter(request.GET,queryset=monu)
    monu=searched.qs
    context={'monuments':monu,'searched':searched}

    return render(request,'search.html',context)

def get_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(Country_id=country_id).values('id', 'Name')
    return JsonResponse(list(states), safe=False)

def about(request):
    return render(request,'About Us.html')