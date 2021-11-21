from django.shortcuts import render,redirect
from .models import GST


# Create your views here.
def vendor_profile(request):
    return render(request,'vendor_profile.html')

def update_gst(request):
    if request.method == "POST":
        code = request.POST.get('code')
        desc = request.POST.get('desc')
        cgst = request.POST.get('cgst')
        sgst = request.POST.get('sgst')
        igst = request.POST.get('igst')
        cess = request.POST.get('cess')
        # obj=GST.objects.get(user=request.user)
        # if obj:
        #     obj.update(hsn=code,desc=desc,cgst=cgst,sgst=sgst,igst=igst,cess=cess)
        # else:
        #     obj = GST.objects.create(user=request.user,hsn=code,desc=desc,cgst=cgst,sgst=sgst,igst=igst,cess=cess)
        #     obj.save()

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
    #    GST.objects.filter(user=request.user).update(hsn=code,desc=desc,cgst=cgst,sgst=sgst,igst=igst,cess=cess)


    return redirect('vendor_profile')