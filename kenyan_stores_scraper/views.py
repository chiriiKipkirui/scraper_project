from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import  *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View
from easy_pdf.rendering import render_to_pdf

# scraping for products from jumia to the Products table on the db


def red(request):
    return redirect("kenyan_stores_scraper:home")
global general_details
general_details = []

def home(request):
    products = Products.objects.all()
    if products.count()>10:
        products = Products.objects.all()[:10]
    else:
        products = Products.objects.all()
    query = request.GET.get("search_keyword")


    if query:
        query_list = query.split(' ')
        
        # products = Products.objects.all().filter(product_name__icontains =query_list[0]).filter(product_name__icontains=query_list[1])
        
        if len(query_list)>1:
            products = Products.objects.all().filter(product_name__icontains =query_list[0]).filter(product_name__icontains=query_list[1])
        else:
            products = products.filter(product_name__icontains=query_list[0])
                                                  

    paginator = Paginator(products, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)
    context = {
    'products':products
    }
  
    return render(request,'main/index.html',context)






def details(request,pk):
    product_id = Products.objects.get(pk=pk)

    jumia_details = Jumia.objects.filter(product_id = product_id.id)
    killmall_details = Killmall.objects.filter(product_id = product_id.id)
    avechi_details = Avechi.objects.filter(product_id = product_id.id)
    context = {
    'jumia_prods':jumia_details,
    'killmall_prods': killmall_details,
    'avechi_details':avechi_details,
    'product':product_id

    }
   
    general_details.append(context)
   
  

    return render(request,"main/results.html",context)

class GeneratePdf(View):
    
    def get(self, request, *args, **kwargs):
        data = general_details[0]
        pdf = render_to_pdf('pdf/contentpage.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
        
    
