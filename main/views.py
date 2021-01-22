from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Blog_data
import itertools
from .forms import mainform
# Create your views here.


def go_main(request):
    return HttpResponseRedirect("index/all/")


def index(request, cat):

    categorylist = Blog_data.objects.values_list('category')

    catlist = []

    for dt in categorylist:
        for dm in dt:
            if dm not in catlist:
                catlist.append(dm)

    cate = list(itertools.chain(*categorylist))

    if cat == "all":
        df = Blog_data.objects.all().order_by('-pub_date')
    else:
        df = Blog_data.objects.filter(category=cat).order_by('-pub_date')

    return render(request, "index.html", {"data": df, "cate": catlist})


def detail_page(request, blog_id):
    details = Blog_data.objects.filter(pk=blog_id)

    return render(request, "details.html", {"details": details})


def test(request):

    if request.method == "POST":
        fm = mainform(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['number'])

    else:
        fm = fm = mainform()
    return render(request, "test.html", {'fm': fm})
