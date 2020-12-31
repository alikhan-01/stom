from django.contrib import admin

from  main.models import *

##################################
class GlavniyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Glavniy,GlavniyAdmin)


##################################
class TipAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tip,TipAdmin)


##################################
class AboutAdmin(admin.ModelAdmin):
    pass

admin.site.register(About,AboutAdmin)


##################################
class CertificateAdmin(admin.ModelAdmin):
    pass

admin.site.register(Certificate,CertificateAdmin)


##################################
class DoctorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Doctor,DoctorAdmin)


##################################
class RegisterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Register,RegisterAdmin)


##################################
class PrizeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Prize,PrizeAdmin)


##################################
class SuccessAdmin(admin.ModelAdmin):
    pass

admin.site.register(Success,SuccessAdmin)


##################################
class TestAdmin(admin.ModelAdmin):
    pass

admin.site.register(Test,TestAdmin)


##################################
class LatestAdmin(admin.ModelAdmin):
    pass

admin.site.register(Latest,LatestAdmin)


##################################
class StaffAdmin(admin.ModelAdmin):
    pass

admin.site.register(Staff,StaffAdmin)


##################################
class FaqAdmin(admin.ModelAdmin):
    pass

admin.site.register(Faq,FaqAdmin)


##################################
class PartnerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Partner,PartnerAdmin)


##################################
class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact,ContactAdmin)


##################################
class OpeningAdmin(admin.ModelAdmin):
    pass

admin.site.register(Opening,OpeningAdmin)


##################################
class TweetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tweet,TweetAdmin)


##################################
class InformationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Information,InformationAdmin)


##################################
class HistoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(History,HistoryAdmin)


##################################
class History_imgAdmin(admin.ModelAdmin):
    pass

admin.site.register(History_img,History_imgAdmin)


##################################
class MissionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Mission,MissionAdmin)


##################################
class Why_aboutAdmin(admin.ModelAdmin):
    pass

admin.site.register(Why_about,Why_aboutAdmin)


##################################
class ServiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Service,ServiceAdmin)


##################################
class ProjectTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProjectType,ProjectTypeAdmin)


##################################
class ProjectItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProjectItem,ProjectItemAdmin)


# Register your models here.
