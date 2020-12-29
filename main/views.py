from django.shortcuts import render
from main.models import *
from main.models import Glavniy,Tip,About,Certificate,Doctor,Register,Prize,Faq,Why_about
from main.models import Success,Test,Latest,Staff,Partner,Contact,Opening,Information,History,History_img,Mission
from django.http.response import JsonResponse
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
        print ('*' * 100)
        r = Register()
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        email = request.POST.get('email', '')
        from datetime import datetime
        dtn = datetime.now()
        r.data = dtn
        r.time = dtn
        r.name = name
        r.phone = phone
        r.email = email
        r.message = message

        #r.filial_id = int(address)
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


