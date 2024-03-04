from django.shortcuts import render
from app.models import Categories,Course

def BASE(request):
    return render(request,'base.html')

def HOME(request):
    category = Categories.objects.all().order_by("id")[0:5]
    course = Course.objects.filter(status = "PUBLISH").order_by('id')
    

    context = {
        'category':category,
        'course':course,

    }
    return render(request,'main/home.html', context)
    