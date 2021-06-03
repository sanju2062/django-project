from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact

def main(request):
    return render(request,'main.html')

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')

def why_us(request):
    return render(request,'whyus.html')

def mission(request):
    return render(request,'mission.html')

def vision(request):
    return render(request,'vision.html')

def career(request):
    return render(request,'careers.html')

def contact(request):
    if request.method == 'POST':
        post = Contact()
        post.name = request.POST.get('name')
        post.contact_no = request.POST.get('contact')
        post.email_id = request.POST.get('email')
        post.company = request.POST.get('company')
        post.save()
    return render(request,"contact.html")
def blog(request):
    return render(request,'blog.html')
# def contactpost(request):
    # if request.method == 'POST':
    #     post = Contact()
    #     post.name = request.POST.get('name')
    #     post.contact = request.POST.get('contact')
    #     post.email = request.POST.get('email')
    #     post.company = request.POST.get('company')
    #     post.save()
    #     return render(request,"contact.html")
    # else:
    #     return render(request,"contact.html")
def my_test_500_view(request):
    # Return an "Internal Server Error" 500 response code.
    return HttpResponse(status=500)
