from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,get_object_or_404,redirect
from .models import Main
from forSale.models import Forslar
from category.models import category
from contentus.models import Contentus



def home(request):
    pageName = 'Home page '
    set = Main.objects.filter(pk = 2)
    cat = category.objects.all()
    sale = Forslar.objects.all()[:3]
    print(sale)

    return render(request,'front/home.html',{'sale':sale, 'cat':cat ,'set':set, 'title':pageName})

def aboutus(request):
    pageName = 'AboutUs pange'
    set = Main.objects.filter(pk = 2)
    return render(request,'front/about.html',{'set':set,'title':pageName})

def producte(request,pk):
    sale =  Forslar.objects.filter(pk=pk)
    return render(request,'front/producte.html',{'sale':sale})

def panel(request):

    return render(request,'back/home.html')
def forsale(requset,pk):
    sale =  Forslar.objects.filter(pk=pk)
    print(sale)
    return render(requset,'front/home.html',{'sale':sale})
def addProducte(requset):
    cat = category.objects.all()
    if requset.method == 'POST':
        pName = requset.POST.get('name')
        pStats =requset.POST.get('stats')
        pSize =requset.POST.get('size')
        pPrice =requset.POST.get('price')
        pDescription =requset.POST.get('description')
        pCategory =requset.POST.get('category')
        nameCategory = category.objects.get(pk = pCategory).name

        if pName == ' ' or pPrice == ' ':
            error = 'there is some file is empty....'
            return render(requset,'back/error.html',{'error':error})
        try:
            myfile = requset.FILES['myImg']
            fs = FileSystemStorage()
            fileName = fs.save(myfile.name, myfile)
            url = fs.url(fileName)
            b = Forslar(name = pName,stats = pStats,category = nameCategory,pric = pPrice,size = pSize ,picurl = url,picname= fileName,description= pDescription)
            b.save()
        except:
            error = 'there is some error111'
            return render(requset,'back/error.html',{'error':error})
    return render(requset,'back/addproducte.html',{'cat':cat})






    return render(requset,'back/addproducte.html',{'producte':producte})


def ediTP(request , pk):
    list = Forslar.objects.all()
    editP = Forslar.objects.get(pk = pk)
    if request.method == 'POST':
        pName = request.POST.get('name')
        pStats = request.POST.get('stats')
        pSize = request.POST.get('size')
        pPrice = request.POST.get('price')
        pDescription = request.POST.get('description')
        myfile = request.FILES['myImg']
        fs = FileSystemStorage()
        fileName = fs.save(myfile.name, myfile)
        url = fs.url(fileName)
        if pName == ' ' or pPrice == ' ':
            error = 'there is some file is empty....'
            return render(request, 'back/error.html', {'error': error})
        try:

            b = Forslar.objects.get(pk =pk )
            fss = FileSystemStorage()
            fss.delete(b.url)
            b.name = pName
            b.stats = pStats
            b.size = pSize
            b.pric = pPrice
            b.picurl = url
            b.picname = fileName
            b.description = pDescription
            b.save()


        except:
            b = Forslar.objects.get(pk=pk)
            fs = FileSystemStorage()
            fileName = fs.save(myfile.name, myfile)
            url = fs.url(fileName)
            b.picurl = url
            b.picname = fileName
            b.name = pName
            b.stats = pStats
            b.size = pSize
            b.pric = pPrice
            b.description = pDescription
            b.save()
            return render(request,'back/listProducte.html',{'list':list})

    return render(request,'back/editeProducte.html',{'editP':editP})


def listProducte(requset):
    list = Forslar.objects.all()

    return render(requset,'back/listProducte.html',{'list':list})
def deteteP(request,pk):
    list = Forslar.objects.all()

    try:
      b = Forslar.objects.get(pk=pk)
      fss = FileSystemStorage()
      fss.delete(b.picname)
      b.delete()
    except:
        error = 'some thing worng'
        return render(request,'back/error.html',{'error':error})


    return render(request, 'back/listProducte.html', {'list': list})
def addCategory(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        if name != '':
            try:
                b = category(name = name)
                b.save()
                print(b);
                print("this is new")
            except:
                error = 'there is some worng'
                return render(request,'back/error.html',{'error':error})


    return render(request,'back/addCategory.html')


def listCategory(request):
    cat = category.objects.all()
    return render(request,'back/listeCategory.html',{'cat':cat})
def setting(request):
    set = Main.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        Aboutus = request.POST.get('Aboutus')
        PageFacebook = request.POST.get('PageFacebook')
        PageTw = request.POST.get('PageTw')
        pageyout = request.POST.get('pageyout')
        pagelink = request.POST.get('pagelink')
        tel = request.POST.get('tel')
        myfile = request.FILES['myImg']
        fs = FileSystemStorage()
        fileName = fs.save(myfile.name, myfile)
        url = fs.url(fileName)
        b = Main(name = name,about = Aboutus,picurl = url,picname= fileName,pagefa = PageFacebook,pagetw = PageTw,pageyt = pageyout,pageLink = pagelink,pageTe = tel)
        b.save()
        msg  = 'the information update '
        return render(request,'back/masaje.html',{'msg':msg})



    return render(request,'back/setting.html',{'set':set})
def contantus(request):
     pageName = 'ContenUs'
     set = Main.objects.filter(pk = 2)
     if request.method == 'POST':
          name = request.POST.get('name')
          email = request.POST.get('Email')
          tel = request.POST.get('Telephone')
          subjeste = request.POST.get('Subject')
          message = request.POST.get('Message')
          if name != '' and email != '' and message != '':
              b = Contentus(name =name, email = email ,tel = tel ,subject = subjeste,message = message)
              b.save()

     return render(request,'front/contantus.html',{'set':set,'title':pageName})

def listMessage(request):
    cont = Contentus.objects.all()
    return render(request,'back/listMessage.html',{'cont':cont})



def deleteMessage(request, pk):

    cont = Contentus.objects.all()
    d = Contentus.objects.filter(pk=pk)
    d.delete()
    return render(request,'back/listMessage.html',{'cont':cont})



