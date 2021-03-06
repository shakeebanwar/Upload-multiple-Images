from django.shortcuts import render, redirect,HttpResponse
from .models import Photo,MultipleImages


def index(request):
    return render(request,'check.html')


def upload(request):
    if request.method == "POST":
        files = request.FILES.getlist('images')
        product = request.POST['product']
        checkExist = Photo.objects.filter(title = product)
        if checkExist:
            return HttpResponse('Product Already Exist in DataBase Make sure title must be Unique')
        
        else:
            photoData = Photo(title = product)
            photoData.save()
            
            for i in range(len(files)):
                imagesData = MultipleImages(photoDetails = Photo.objects.get(title = product),img = files[i])
                imagesData.save()

            
            photodata = Photo.objects.get(title = product)
            data = MultipleImages.objects.filter(photoDetails = photodata.id)

    
        return render(request,'slider.html',{'data':data})

    return render(request,'check.html')
        



  