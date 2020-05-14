from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,get_object_or_404,redirect
from .models import Main,UserProfile
from forSale.models import Forslar,Category
from category.models import category
from contentus.models import Contentus
from django.contrib.auth import authenticate,login, logout
from django.contrib import auth
from django.contrib.auth.models import User






def home(request):
    pageName = 'Home page '
    set = Main.objects.filter(pk = 1)
    cate = Category.objects.all()
    sale = Forslar.objects.all()[:3]
    nod = Forslar.objects.all()
    print(   type(cate ))
    print(set)

    return render(request,'front/home.html',{'sale':sale, 'cate':  Category.objects.all(),'set':set, 'title':pageName,'nod':nod})

def aboutus(request):
    pageName = 'AboutUs pange'
    set = Main.objects.filter(pk = 1)
    return render(request,'front/about.html',{'set':set,'title':pageName})

def producte(request,pk):
    pageName = 'producte Page'
    sale =  Forslar.objects.filter(pk=pk)
    dayproducte = Forslar.objects.all()[:3]
    lastproducte = Forslar.objects.all()[:2]
    return render(request,'front/producte.html',{'sale':sale,'dayproducte':dayproducte,'lastproduct':lastproducte,'title':pageName})

def panel(request):

    return render(request,'back/home.html')
def forsale(requset,pk):
    sale =  Forslar.objects.filter(pk=pk)
    return render(requset,'front/home.html',{'sale':sale})




def login(request):
    pageName = 'Home page '
    cate = Category.objects.all()
    if request.method == 'POST':
        uuser = request.POST.get('Username')
        ppassword = request.POST.get('Password')
        if uuser != '' and ppassword != '':
            user = authenticate(username = uuser,password = ppassword)

            if user is not None:

                auth.login(request,user)
                return render(request,'front/login.html')


    return render(request,'front/home.html',{'title':pageName,'cate':cate})

def logout(request):
    auth.logout(request)
    return render(request,'front/login.html')


def register(request):
    pageName = 'Home page '
    cate = Category.objects.all()
    if request.method == 'POST':
        username = request.POST.get('Username')
        useremail = request.POST.get('Email')
        userpassword = request.POST.get('Password')
        userconfpass = request.POST.get('confpassword')
        if username != '' and useremail != '' and userpassword != '' and userconfpass != '':
            if userpassword == userconfpass:
                if len(User.objects.filter(username=username)) == 0 and len(User.objects.filter(email=useremail)) == 0:
                    user = User.objects.create_user(username, useremail, userpassword)


    return render(request, 'front/home.html',{'title':pageName,'cate':cate})



def userPage(request):
    pageName = 'User page '
    cate = Category.objects.all()


    return render(request, 'front/UserPage.html',{'title':pageName,'cate':cate})
def UserProfil(request):
    userinfo = UserProfile.objects.get(user=request.user)


    return  render(request,'front/userProfil.html',{'userinfo':userinfo})

def userUpdate(request):
    userinfo = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        userName = request.POST.get('name')
        userphone = request.POST.get('phone')
        useremail = request.POST.get('email')
        usercity = request.POST.get('city')
        usercountry = request.POST.get('country')
        useraddress = request.POST.get('address')
        userimage = request.FILES.get('image')
        b = UserProfile.objects.get(user=request.user)
        b.image = userimage
        b.user = request.user
        b.phone = userphone
        b.city = usercity
        b.country = usercountry
        print(userinfo)
        b.save()
        userinfo = UserProfile.objects.get(user=request.user)
        return redirect('/userProfile/')

        return render(request,'front/userProfil.html',{'userInfo':userinfo})
    userinfo = UserProfile.objects.get(user=request.user)
    return render(request,'front/userUpdate.html',{'userInfp':userinfo})

def userChangePassword(request):
    userinfo = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        oldPassword  = request.POST.get('oldpassword')
        newPassword  = request.POST.get('newpassword')
        if oldPassword != '' and newPassword != '':

          user = authenticate(username=request.user, password=oldPassword)
          if user is not None:
              user = User.objects.get(username=request.user)
              user.set_password(newPassword)
              user.save()
              return render(request,'front/login.html')
          else:
             print("nnnnoooooooooooooo")


    return  render(request,'front/userChangePassword.html',{'userInfo': userinfo})


def userAddProducte(request):
    pageName = 'User page '
    cate = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        size = request.POST.get('size')
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        price = request.POST.get('price')
        detail = request.POST.get('detail')
        status = request.POST.get('status')
        categoryId = request.POST.get('category')
        image = request.FILES.get('image')
        category = Category.objects.get(pk = categoryId)
        if status == 0:
            status= "evet"
        else:
         status = "hayir"
        userOwner =  User.objects.get(username=request.user)

        b = Forslar(userOwner = userOwner,name = name,stats = status,category = category,pric = price,amount = amount,image = image,size = size,description = description,detail =detail,slug = name,parent = None)
        b.save()
        return render(request,'front/home.html',{'cate':cate,'title':pageName})







    return render(request,'front/userAddProducte.html',{'cate':cate,'title':pageName})












def producteCategory(request,pk):
    pageName = 'Category pange'
    cate = Category.objects.all()
    categoryData = Category.objects.get(pk= pk)
    produ = Forslar.objects.filter(category_id = pk)



    return render(request,'front/producteCategory.html',{'cate':cate,'produ':produ,'title':pageName,'categoryData':categoryData})



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
     set = Main.objects.filter(pk = 1)
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



