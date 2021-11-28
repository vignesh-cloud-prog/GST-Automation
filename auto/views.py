from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import GST_Table
from django.db.models import Q

import requests
from bs4 import BeautifulSoup


# Create your views here.
def get_gst_page():
    url="https://cbic-gst.gov.in/gst-goods-services-rates.html"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(url))
    doc = BeautifulSoup(response.text, 'html.parser')
    return doc

def index(request):
    GST_Table.objects.all().delete()
    filtered_gst_count=GST_Table.objects.count()
    print(f"Count: {filtered_gst_count}\nStarting... ")
    doc = get_gst_page()
    table= doc.find('table',attrs={'id':'goods_table'})
    table_body=table.find('tbody')
    rows= table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        hsn=cols[1].find(text=True)
        desc=cols[2].find(text=True)
        cgst=cols[3].find(text=True)
        sgst=cols[4].find(text=True)
        igst=cols[5].find(text=True)
        cess=""
        if len(cols)==7:
            cess=cols[6].text.replace("%","")

        # print(hsn,desc,cgst,sgst,igst,cess)
        obj=GST_Table.objects.create(hsn=hsn,desc=desc,cgst=cgst,sgst=sgst,igst=igst,cess=cess)
        obj.save()
    filtered_gst_count=GST_Table.objects.count()

    print(f"Count: {filtered_gst_count}\nDone😎 ")


    return render(request,'index.html')

def gst_search(request,query):
    filtered_gst=GST_Table.objects.filter(Q(hsn__contains=query) | Q(desc__contains=query))[:]
    filtered_gst_json = serializers.serialize('json', filtered_gst)
    return HttpResponse(filtered_gst_json, content_type='application/json')