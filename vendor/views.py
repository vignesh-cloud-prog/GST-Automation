from django.shortcuts import render,redirect
from .models import GST


# Create your views here.

def vendor_profile(request):
    if request.user.is_superuser:
        return render(request,'vendor_profile.html')
    else :
        return redirect('admin:index')

def update_gst(request):
    if not request.user.is_superuser:
        return redirect('admin:index')
        
    if request.method == "POST":
        code = request.POST.get('code')
        desc = request.POST.get('desc')
        cgst = request.POST.get('cgst')
        sgst = request.POST.get('sgst')
        igst = request.POST.get('igst')
        cess = request.POST.get('cess')
    
        try:
            obj=GST.objects.get(user=request.user)
            obj.hsn=code
            obj.desc=desc
            obj.cgst=cgst
            obj.sgst=sgst
            obj.igst=igst
            obj.cess=cess
            obj.save()
            print("updated")
        except GST.DoesNotExist:
            obj = GST.objects.create(user=request.user,hsn=code,desc=desc,cgst=cgst,sgst=sgst,igst=igst,cess=cess)
            obj.save()
            print("saved")
        print(code,desc,sgst,cgst,igst,cess)

    return redirect('vendor_profile')