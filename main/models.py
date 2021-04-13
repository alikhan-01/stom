from django.db import models
#from ckeditor.fields import RichTextField
from datetime import datetime

# Create your models here.

class Glavniy(models.Model):
    mini_description1 = models.CharField(max_length=300, blank=True)
    title = models.CharField(max_length=300)
    mini_description2 = models.CharField(max_length=300, blank=True)
    description = models.TextField(max_length=170,blank=True)
    logo = models.ImageField(upload_to='upload')
    rating = models.IntegerField(default=0)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.title


class Tip(models.Model):
    icon = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    mini_description = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    mini_description = models.CharField(max_length=200)
    quote_1 = models.CharField(max_length=200)
    quote_2 = models.CharField(max_length=200)
    quote_3 = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='upload')

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    logo_in = models.ImageField(upload_to='upload')
    rating = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Doctor(models.Model):
    logo = models.ImageField(upload_to='upload')
    last_name = models.CharField(max_length=300)
    first_name = models.CharField(max_length=300)
    position = models.CharField(max_length=300)
    info_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    facebook = models.CharField(max_length=300, blank=True)
    telegram = models.CharField(max_length=300, blank=True)
    whatsapp = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.last_name


class Register(models.Model):
    selectww = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    email = models.EmailField(max_length=300, blank=True)
    data = models.DateField(blank=True)
    time = models.TimeField(auto_now=False, auto_now_add=False, blank=True)
    message = models.TextField(blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Prize(models.Model):
    title = models.CharField(max_length=300)
    number = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title


class Success(models.Model):
    last_name = models.CharField(max_length=300)
    first_name = models.CharField(max_length=300)
    position = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)
    mini_logo = models.ImageField(upload_to='upload')
    description = models.TextField()
    mini_description = models.CharField(max_length=300, blank=True)
    job_1 = models.CharField(max_length=300, blank=True)
    job_2 = models.CharField(max_length=300, blank=True)
    logo_left = models.ImageField(upload_to='upload')
    logo_right = models.ImageField(upload_to='upload')
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.last_name


class Test(models.Model):
    logo = models.ImageField(upload_to='upload')
    description = models.TextField()
    last_name = models.CharField(max_length=300)
    first_name = models.CharField(max_length=300)
    position = models.CharField(max_length=300)
    mini_logo = models.ImageField(upload_to='upload')
    rating = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.last_name


class Latest(models.Model):
    logo = models.ImageField(upload_to='upload')
    data = models.DateField()
    comment = models.IntegerField(default=0)
    title = models.CharField(max_length=300)
    name_author = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.title


class Staff(models.Model):
    title = models.CharField(max_length=300)
    mini_description = models.CharField(max_length=300)
    description = models.TextField()
    logo = models.ImageField(upload_to='upload')
    last_name = models.CharField(max_length=300)
    first_name = models.CharField(max_length=300)
    position = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Faq(models.Model):
    icon = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    description = models.TextField()
    rating = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Partner(models.Model):
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    rating = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(max_length=300)
    phone = models.CharField(max_length=300, blank=True)
    address = models.CharField(max_length=300, blank=True)
    email = models.CharField(max_length=300, blank=True)
    email_ssylka = models.CharField(max_length=300, blank=True)
    facebook = models.CharField(max_length=300, blank=True)
    instagram = models.CharField(max_length=300, blank=True)
    telegram = models.CharField(max_length=300, blank=True)
    whatsapp = models.CharField(max_length=300, blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Opening(models.Model):
    title = models.CharField(max_length=300)
    time_from = models.CharField(max_length=300, blank=True)
    time_before = models.CharField(max_length=300, blank=True)
    mini_description = models.CharField(max_length=300, blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Tweet(models.Model):
    title = models.CharField(max_length=60)
    mini_description = models.CharField(max_length=60, blank=True)
    data = models.DateField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Information(models.Model):
    title = models.CharField(max_length=300,blank=True)
    meet_description = models.TextField(blank=True)
    number_description = models.TextField(blank=True)
    success_description = models.TextField(blank=True)
    testimonial_description = models.TextField(blank=True)
    latest_description = models.TextField(blank=True)
    about_mini_description = models.TextField(blank=True)
    make_mini_description = models.TextField(blank=True)
    service_mini_description = models.TextField(blank=True)
    service_item_description = models.TextField(blank=True)
    service_title_description = models.TextField(blank=True)
    latest_mini_description = models.TextField(blank=True)
    dc_mini_description = models.TextField(blank=True)
    con_mini_description = models.TextField(blank=True)
    con_us_mini_description = models.TextField(blank=True)
    useful_mini_description = models.TextField(blank=True)
    useful_description = models.TextField(blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class History(models.Model):
    title = models.CharField(max_length=300,blank=True)
    description = models.TextField(blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class History_img(models.Model):
    title = models.CharField(max_length=300, blank=True)
    logo = models.ImageField(upload_to='upload')
    rating = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Mission(models.Model):
    title = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    description_1 = models.CharField(max_length=300, blank=True)
    description_2 = models.CharField(max_length=300, blank=True)
    description_3 = models.CharField(max_length=300, blank=True)
    description_4 = models.CharField(max_length=300, blank=True)
    youtube = models.CharField(max_length=300,blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Why_about(models.Model):
    title = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    description_1 = models.CharField(max_length=300, blank=True)
    description_2 = models.CharField(max_length=300, blank=True)
    description_3 = models.CharField(max_length=300, blank=True)
    description_4 = models.CharField(max_length=300, blank=True)
    rating = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Service(models.Model):
    icon = models.CharField(max_length=300, blank=True)
    title = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    rating = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class ProjectType(models.Model):
    title = models.CharField(max_length=300, blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class ProjectItem(models.Model):
    title = models.CharField(max_length=300, blank=True)
    description_1 = models.CharField(max_length=300)
    description_2 = models.CharField(max_length=300)
    type = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='upload')

    def __str__(self):
        return self.title

class Doctor_all(models.Model):
    title = models.CharField(max_length=300, blank=True)
    description_1 = models.TextField(blank=True)
    mini_1 = models.CharField(max_length=300)
    mini_2 = models.CharField(max_length=300)
    mini_3 = models.CharField(max_length=300)
    description_2 = models.TextField(blank=True)
    description_3 = models.TextField(blank=True)
    logo = models.ImageField(upload_to='upload')
    mini_description = models.TextField()
    last_name = models.CharField(max_length=300, blank=True)
    first_name = models.CharField(max_length=300, blank=True)
    position = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    logo = models.ImageField(upload_to='upload')
    data = models.DateField()
    comment = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    title = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_author = models.CharField(max_length=300)
    description_1 = models.TextField()
    description_2 = models.TextField(blank=True)
    rating = models.IntegerField(default=0)
    status = models.IntegerField(default=0)


    def __str__(self):
        return self.title


class Marshrut(models.Model):
    title = models.CharField(max_length=300,blank=True)
    icon = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Conform(models.Model):
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    email = models.EmailField(max_length=300, blank=True)
    message = models.TextField(blank=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Useful(models.Model):
    logo_before = models.ImageField(upload_to='upload')
    logo_after = models.ImageField(upload_to='upload')
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    rating = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


