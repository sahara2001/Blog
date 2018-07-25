from django.shortcuts import render
from django.shortcuts import HttpResponse
from posts import models


# Create your views here.
def index(request):

    #request.GET
    #return HttpResponse("infosfdsafdsafsdafasfHAHAHAHHHA")
    #return render(request, "template/index.html",)
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print(username, password)


        
        #add data to database
        models.UserInfo.objects.create(user=username, pwd=password)     # ??? why always warning ???, no objects member in static ?
    
    #get data from database
    user_list = models.UserInfo.objects.all()

    return render(request, "template/index.html",{"data":user_list})
