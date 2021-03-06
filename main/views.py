from django.shortcuts import render
from main.models import *
from django.http import HttpResponse, JsonResponse
from main.models import Glavniy,Tip,About,Certificate,Doctor,Register,Prize,Faq,Why_about
from main.models import Success,Test,Latest,Staff,Partner,Contact,Opening,Information,History,History_img,Mission
from main.models import Service,ProjectType,ProjectItem,Doctor_all,Marshrut,Category,Blog,Useful

import math
# Create your views here.



def indexHandler(request):
    if request.method == 'GET':
        page = 'index'
        glavniys = Glavniy.objects.filter(status=0).order_by('-rating')
        tips = Tip.objects.all().order_by('rating')[:4]
        abouts = About.objects.all().order_by('-id')[:1]
        certificates = Certificate.objects.filter(status=0).order_by('-rating')
        doctors = Doctor.objects.filter(status=0).order_by('-rating')
        prizes = Prize.objects.filter(status=0).order_by('-rating')
        successs = Success.objects.filter(status=0).order_by('-rating')
        tests = Test.objects.filter(status=0).order_by('-rating')
        latests = Latest.objects.filter(status=0).order_by('-rating')
        staffs = Staff.objects.filter(status=0).order_by('-rating')
        faqs = Faq.objects.filter(status=0).order_by('-rating')
        partners = Partner.objects.filter(status=0).order_by('-rating')
        contacts = Contact.objects.filter(status=0)
        openings = Opening.objects.filter(status=0)
        tweets = Tweet.objects.filter(status=0)[:3]
        informations = Information.objects.filter(status=0)
        return render(request, 'index.html', {
            'page':page,
            'glavniys': glavniys,
            'tips': tips,
            'abouts': abouts,
            'certificates': certificates,
            'doctors': doctors,
            'prizes': prizes,
            'successs': successs,
            'tests': tests,
            'latests': latests,
            'staffs': staffs,
            'faqs': faqs,
            'partners': partners,
            'contacts': contacts,
            'openings': openings,
            'tweets': tweets,
            'informations': informations,


        })
    else:

        r = Register()
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        selectww = request.POST.get('selectww', '')
        from datetime import datetime
        dtn = datetime.now()
        r.data = dtn
        r.time = dtn
        r.name = name
        r.phone = phone
        r.email = email
        r.message = message
        r.selectww = selectww

        r.save()

        return JsonResponse({'success': True, 'errorMsg': '', '_success': True})

def aboutHandler(request):
    page = 'about'
    contacts = Contact.objects.filter(status=0)
    openings = Opening.objects.filter(status=0)
    tweets = Tweet.objects.filter(status=0)[:3]
    informations = Information.objects.filter(status=0)
    historys = History.objects.filter(status=0)
    history_imgs = History_img.objects.filter(status=0).order_by('-rating')
    certificates = Certificate.objects.filter(status=0).order_by('-rating')
    missions = Mission.objects.filter(status=0)
    why_abouts = Why_about.objects.filter(status=0).order_by('-rating')
    tests = Test.objects.filter(status=0).order_by('-rating')

    return render(request, 'about.html', {'page':page,
                                          'contacts': contacts,
                                          'openings': openings,
                                          'tweets': tweets,
                                          'informations': informations,
                                          'historys':historys,
                                          'history_imgs':history_imgs,
                                          'certificates':certificates,
                                          'missions':missions,
                                          'why_abouts':why_abouts,
                                          'tests':tests
                                          })


def serviceHandler(request):
    limit = int(request.GET.get('limit', 3))
    p = int(request.GET.get('p', 1))
    stop = p * limit
    start = (p-1) * limit
    projects = ProjectItem.objects.all()[start:stop]
    item_count = ProjectItem.objects.count()
    page_count = math.ceil(item_count/limit)
    page_range = range(1, page_count + 1)
    prev_p = p-1
    next_p = p+1





    page = 'service'
    contacts = Contact.objects.filter(status=0)
    openings = Opening.objects.filter(status=0)
    tweets = Tweet.objects.filter(status=0)[:3]
    informations = Information.objects.filter(status=0)
    types = ProjectType.objects.filter(status=0)
    services = Service.objects.filter(status=0)

    DATA = {
            'page':page,
            'contacts': contacts,
            'openings': openings,
            'tweets': tweets,
            'informations': informations,
            'services':services,
            'types': types,
            'projects': projects,

            'limit': limit,
            'p':p,
            'page_count': page_count,
            'page_range':page_range,
            'prev_p':prev_p,
            'next_p':next_p
            }

    return render(request, 'service.html', DATA)


def page404Handler(request):
    page = '404'
    contacts = Contact.objects.filter(status=0)
    openings = Opening.objects.filter(status=0)
    tweets = Tweet.objects.filter(status=0)[:3]
    return render(request, '404.html', {
                                        'page': page,
                                        'contacts': contacts,
                                        'openings': openings,
                                        'tweets': tweets

                                        })


def doctorsHandler(request):
    page = 'doctors'
    contacts = Contact.objects.filter(status=0)
    openings = Opening.objects.filter(status=0)
    tweets = Tweet.objects.filter(status=0)[:3]
    informations = Information.objects.filter(status=0)
    doctor_alls = Doctor_all.objects.all()
    doctors = Doctor.objects.filter(status=0)

    return render(request, 'doctors.html', {
                                        'page': page,
                                        'contacts': contacts,
                                        'openings': openings,
                                        'tweets': tweets,
                                        'informations':informations,
                                        'doctor_alls':doctor_alls,
                                        'doctors':doctors
                                        })


def doctorsItemHandler(request, item_id):
    page = 'doctors'
    contacts = Contact.objects.filter(status=0)
    openings = Opening.objects.filter(status=0)
    tweets = Tweet.objects.filter(status=0)[:3]
    informations = Information.objects.filter(status=0)
    active_doctor = Doctor.objects.get(id=int(item_id))
    doctors = Doctor.objects.filter(status=0)

    return render(request, 'doctor_item.html', {
                                        'page': page,
                                        'contacts': contacts,
                                        'openings': openings,
                                        'tweets': tweets,
                                        'informations': informations,
                                        'active_doctor': active_doctor,
                                        'doctors': doctors
                                        })




def blogHandler(request):
    q = request.GET.get('q', '')
    category_id = int(request.GET.get('category_id', 0))
    year = int(request.GET.get('year', 0))
    month = int(request.GET.get('month', 0))

    limit = int(request.GET.get('limit', 4))
    p = int(request.GET.get('p', 1))
    stop = p * limit
    start = (p - 1) * limit


    if q:
        blogs = Blog.objects.filter(status=0).filter(description_1__contains=q).order_by('-rating')[start:stop]
        item_count = Blog.objects.filter(status=0).filter(description_1__contains=q).count()
    else:
        if category_id:
            if year and month:
                blogs = Blog.objects.filter(status=0).filter(category__id=category_id).filter(data__year=year).filter(data__month=month).order_by('-rating')[start:stop]
                item_count = Blog.objects.filter(status=0).filter(category__id=category_id).filter(data__year=year).filter(data__month=month).count()
            else:
                blogs = Blog.objects.filter(status=0).filter(category__id=category_id).order_by('-rating')[start:stop]
                item_count = Blog.objects.filter(status=0).filter(category__id=category_id).count()
        else:
            if year and month:
                blogs = Blog.objects.filter(status=0).filter(data__year=year).filter(data__month=month).order_by('-rating')[start:stop]
                item_count = Blog.objects.filter(status=0).filter(data__year=year).filter(data__month=month).count()
            else:
                blogs = Blog.objects.filter(status=0).order_by('-rating')[start:stop]
                item_count = Blog.objects.filter(status=0).count()

    page_count = math.ceil(item_count / limit)
    page_range = range(1, page_count + 1)
    prev_p = p - 1
    next_p = p + 1



    page = 'blog'
    contacts = Contact.objects.filter(status=0)
    openings = Opening.objects.filter(status=0)
    tweets = Tweet.objects.filter(status=0)[:3]
    informations = Information.objects.filter(status=0)
    categorys = Category.objects.all()

    ######## ARHIV ########
    blog_list = Blog.objects.filter(status=0)
    monthes = ['', 'JANUARY', 'FEBRUARY', 'MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    # result = {
    #     2020:{
    #         1:{
    #             'title': 'FEBRUARY',
    #             'count': 0
    #         }
    #     }
    # }
    result = {}

    for bl in blog_list:
        bl = bl.data
        if bl.year not in result:
            result[bl.year] = {}

        if bl.month not in result[bl.year]:
            result[bl.year][bl.month] = {
                'title': monthes[bl.month],
                'count': 0
            }

        result[bl.year][bl.month]['count'] += 1



    return render(request, 'blog.html', {
                                        'page': page,
                                        'contacts': contacts,
                                        'openings': openings,
                                        'tweets': tweets,
                                        'informations':informations,
                                        'blogs':blogs,
                                        'categorys':categorys,

                                        'limit': limit,
                                        'p': p,
                                        'page_count': page_count,
                                        'page_range': page_range,
                                        'prev_p': prev_p,
                                        'next_p': next_p,

                                        'category_id':category_id,
                                        'item_count':item_count,
                                        'q': q,
                                        'result': result,
                                        'monthes': monthes
                                        })


def contactsHandler(request):
    if request.method == 'GET':
        page = 'contacts'
        contacts = Contact.objects.filter(status=0)
        openings = Opening.objects.filter(status=0)
        tweets = Tweet.objects.filter(status=0)[:3]
        informations = Information.objects.filter(status=0)
        marshruts = Marshrut.objects.filter(status=0)
        return render(request, 'contacts.html', {
            'page': page,
            'contacts': contacts,
            'openings': openings,
            'tweets': tweets,
            'informations':informations,
            'marshruts':marshruts
        })
    else:

        c = Conform()
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        c.name = name
        c.phone = phone
        c.email = email
        c.message = message

        c.save()

    return HttpResponse({'success': True, 'errorMsg': '', '_success': True})


def usefulHandler(request):
    limit = int(request.GET.get('limit', 2))
    p = int(request.GET.get('p', 1))
    stop = p * limit
    start = (p - 1) * limit
    usefuls = Useful.objects.all()[start:stop]
    item_count = Useful.objects.count()
    page_count = math.ceil(item_count / limit)
    page_range = range(1, page_count + 1)
    prev_p = p - 1
    next_p = p + 1
    print(page_count)
    print(page_range)


    page = 'useful'
    contacts = Contact.objects.filter(status=0)
    openings = Opening.objects.filter(status=0)
    tweets = Tweet.objects.filter(status=0)[:3]
    informations = Information.objects.filter(status=0)


    return render(request, 'useful.html', {
                                        'page': page,
                                        'contacts': contacts,
                                        'openings': openings,
                                        'tweets': tweets,
                                        'informations':informations,
                                        'usefuls':usefuls,


                                        'limit': limit,
                                        'p': p,
                                        'page_count': page_count,
                                        'page_range': page_range,
                                        'prev_p': prev_p,
                                        'next_p': next_p
                                        })