from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'./myapp/index.html')

from.models import product_details
def product_details_add(request):
    if request.method == 'POST':
        product=request.POST.get('product')
        category=request.POST.get('category')
        sub_category=request.POST.get('sub_category')

        pd = product_details(product=product,category=category,sub_category=sub_category)
        pd.save()
        context = {'msg':'Added'}
        return render(request,'./myapp/product_details_add.html',context)
    else:
        return render(request, './myapp/product_details_add.html')


def product_details_view(request):
    product_list= product_details.objects.all()
    context={'product_list':product_list}
    return render(request,'./myapp/product_details_view.html',context)

def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        srch=product_details.objects.filter(product__contains=query)
        context={'product_list':srch}
        return render(request,'./myapp/product_details_view.html', context)
    else:
        return render(request,'./myapp/search.html')


#def product_details_search(request):
 #   product_list = product_details.objects.all()
  #  context = {'product_list': product_list}
   # return render(request, './myapp/product_details_search.html', context)