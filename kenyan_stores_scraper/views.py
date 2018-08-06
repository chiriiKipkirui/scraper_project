from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import  *
from .forms import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View
from easy_pdf.rendering import render_to_pdf
from itertools import chain
from django.contrib.auth import logout,authenticate,login

# scraping for products from jumia to the Products table on the db


global general_details
general_details = []

def red(request):
    return redirect("kenyan_stores_scraper:home")


def home(request):
    general_details = []
    jumia_ids = [x.product_id.id for x in Jumia.objects.all()]
    killmall_ids = [x.product_id.id for x in Killmall.objects.all()]
    avechi_ids = [x.product_id.id for x in Avechi.objects.all()]
    all_ids = list(chain(jumia_ids,killmall_ids,avechi_ids))
    final_ids = []
    for b,c in enumerate(all_ids):
        if c not in final_ids:
            final_ids.append(c)
        else:
            pass
    final_ids.sort()
    product_list= [Products.objects.filter(id=i) for i in final_ids]
    products = []
    for x in product_list:
        for y in x:
            products.append(y)
    query = request.GET.get("search_keyword")


    if query:
        query_list = query.split(' ')
        
        # products = Products.objects.all().filter(product_name__icontains =query_list[0]).filter(product_name__icontains=query_list[1])
        
        if len(query_list)>1:
            products = Products.objects.all().filter(product_name__icontains =query_list[0]).filter(product_name__icontains=query_list[1])
        else:
            products = Products.objects.all().filter(product_name__icontains=query_list[0])
                                                  

    paginator = Paginator(products, 25) # Show 25 contacts per page

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
    tracked = TrackedProducts.objects.filter(product=product_id).exists()
    if tracked:
        tracked=True
    else:
        tracked = False


    jumia_details = Jumia.objects.filter(product_id = product_id.id)
    killmall_details = Killmall.objects.filter(product_id = product_id.id)
    avechi_details = Avechi.objects.filter(product_id = product_id.id)
    context = {
    'jumia_prods':jumia_details,
    'killmall_prods': killmall_details,
    'avechi_details':avechi_details,
    'product':product_id,
    'tracked':tracked

    }
   
    general_details.append(context)
   
  

    return render(request,"main/results.html",context)


def logout_view(request):
    logout(request)
    return redirect("kenyan_stores_scraper:login")

def registration_view(request):
    form = RegistrationForm(None)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            user = User.objects.create_user(username=username,password=password,
                    first_name=first_name,last_name=last_name,email=email)
            user.save()
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('/')
        return render(request, 'accounts/signup.html', {'form': form})
    return render(request, 'accounts/signup.html', {'form':form})


def tracking_views(request):
    products_tracked = TrackedProducts.objects.filter(user=request.user)
    count = len(products_tracked)
    
    if len(products_tracked)>1:
        products_list = [Products.objects.filter(id=prod.product.id) for prod in products_tracked]
        products=[]
        for prod in products_list:
            for i in prod:
                products.append(i)
    elif len(products_tracked)==1:
        
        products = Products.objects.filter(id=products_tracked[0].product.id)
        
       
    else:
        products = ''
        
    return render(request,'main/products.html',{'products':products,'count':count})



def delete_product(request,id):
    product = TrackedProducts.objects.get(product=Products.objects.get(pk=id))
    product.delete()

    return redirect("kenyan_stores_scraper:details",pk=id)

def add_to_tracked(request,prod_id):
    product_item = Products.objects.get(id=prod_id)
    exist  = TrackedProducts.objects.filter(product=product_item).exists()
    if exist:
        return redirect('kenyan_stores_scraper:home')
    else:
        product = TrackedProducts.objects.create(user=request.user,product = product_item,status=True)
        product.save()
        return redirect("kenyan_stores_scraper:details",pk=prod_id)



class GeneratePdf(View):
    
    def get(self, request, *args, **kwargs):
        data = general_details[0]
        pdf = render_to_pdf('pdf/contentpage.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
        
