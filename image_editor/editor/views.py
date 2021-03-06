from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import ImageForm, ImageEditForm
from .models import Image
from django.views.generic import View
from PIL import Image as im
from io import StringIO, BytesIO

class HomeView(View):
    def get(self, request):
        images = Image.objects.all()
        context = {'images': images}
        return render(request, 'home.html', context)

class UploadImageView(View):
    def post(self, request):
        if self.request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save(commit=True)
                return HttpResponseRedirect(reverse('editor:home'))
            else:
                return HttpResponseRedirect(reverse('editor:upload'))
    def get(self, request):
        form = ImageForm()
        return render(request, 'upload.html', {'form': form})


def viewImage(request, id):
    obj = get_object_or_404(Image, id=id)
    return render(request, 'viewImage.html', {'obj': obj})


# изменяет изображение физически на бэкенде
class EditImageView(View):
    def post(self, request, id):
        if self.request.method == 'POST':
            image = Image.objects.get(id=id)
            form = ImageEditForm(request.POST)
            if form.is_valid():
                height = form.cleaned_data['height']
                width = form.cleaned_data['width']
                pil_image = im.open(image.img.path)
                resize_image = pil_image.resize((height, width))

                temp = BytesIO()
                resize_image.save(temp, format="JPEG")
                show_resized_img = temp.getvalue()
                return HttpResponse(show_resized_img, content_type="image/jpeg")
            else:
                form = ImageEditForm()
    def get(self, request, id):
        form = ImageEditForm()
        image = Image.objects.get(id=id)
        img = image.img
        return render(request, 'resize.html', {'form': form, 'image': image, 'img': img})