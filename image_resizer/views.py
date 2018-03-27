from django.shortcuts import render
from django.http import HttpResponse
from image_resizer.forms import upload_image
from PIL import Image
import webbrowser
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            check_form=upload_image(request.POST,request.FILES)
            if check_form.is_valid():
                catch_image=check_form.cleaned_data['image']
                catch_width=request.POST['width']
                catch_height=request.POST['height']
                ext = ".jpg"
                temp_image=Image.open(catch_image)
                resize_catch =temp_image.resize((int(catch_width), int(catch_height)), Image.ANTIALIAS)
                resize_catch.save("ANTIALIAS" + ext)
                return HttpResponse(webbrowser.open('file:///F:/major_project/mp/ondemandservices/ANTIALIAS.jpg'))
            else:
                flag=1
                return render(request,'image_resizer/index.html',{'flag_for_form_validation':flag,'form':upload_image})
        else:
            return render(request,'image_resizer/index.html',{'form':upload_image})

    else:
        return render(request,'image_resizer/signinfirst.html',{})