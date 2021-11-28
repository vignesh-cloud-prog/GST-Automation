from django.shortcuts import render,redirect
from .models import Product


# Create your views here.

def product_upload(request):
    if not request.user.is_superuser:
        return redirect('admin:index')
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        selling_price = request.POST.get('selling_price')
        product_desc = request.POST.get('product_desc')
        code = request.POST.get('code')
        desc = request.POST.get('desc')
        cgst = request.POST.get('cgst')
        sgst = request.POST.get('sgst')
        igst = request.POST.get('igst')
        cess = request.POST.get('cess')
        print(product_name,cgst)
        obj=Product.objects.create(seller=request.user,name=product_name,desc=product_desc,selling_price=selling_price,code=code,gst_detail=desc,cgst=cgst,sgst=sgst,igst=igst,cess=cess)
        obj.save()
    return render(request,'product_upload.html')