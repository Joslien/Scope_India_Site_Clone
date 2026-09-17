from django.db import models


class Category(models.Model):
    course_name = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name_plural = "Category"


class Courses(models.Model):
    sub_courses = models.CharField(max_length=200)
    course_name= models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True, default="No description available")
    duration = models.CharField(max_length=100, blank=True, null=True, default="6 Month + 3 Month OJT")
    fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=40000)
    location = models.TextField(blank=True, null=True, default="Kochi,Trivandum,Nagercoil")


    def __str__(self):
        return self.sub_courses

    class Meta:
        verbose_name_plural = "Courses"



# gender=[('male','Male'),('female','Female'),('other','Other')]
# courses=[('data Science & AI Course','Data Science & AI Course'),('data Analytics Course','Data Analytics Course')]
# mode=[('live online','Live online'),('classrom','Classroom')]
# loc=[('technopark tvm','Technopark TVM'),('thampanoor tvm','Thampanoor TVM'),('kochi','Kochi'),('nagercoil','Nagercoil'),('online','Online')]
class Registration(models.Model):
    fullname=models.CharField(max_length=300,default='Na')
    dob=models.DateField(default='2000-01-01')
    gender=models.CharField(max_length=300,default='Na')
    qualification=models.CharField(max_length=500,default='Na')
    number=models.CharField(default=0)
    email=models.EmailField()
    guardian=models.CharField(max_length=300,default='Na')
    occupation=models.CharField(max_length=300,default='Na')
    mobile=models.IntegerField(default=0)
    course=models.TextField(blank=True, null=True,default='Na')
    mode=models.CharField(max_length=300,default='Na')
    loc=models.CharField(max_length=300,default='Na')
    time = models.CharField(max_length=300,default='Na')
    hobbies = models.CharField(max_length=300,default='Na')
    address=models.CharField(max_length=500,default='Na')
    country = models.CharField(max_length=500,default='Na')
    state = models.CharField(max_length=500,default='Na')
    city = models.CharField(max_length=500,default='Na')
    pin=models.CharField(max_length=500,default='Na')
    file=models.FileField(upload_to="documents",default="NA")
    otp=models.CharField(max_length=10,null=True,blank=True)
    expire_time=models.DateTimeField(null=True,blank=True)
    password=models.CharField(max_length=500,default="NA")
    confirm_password=models.CharField(max_length=500,default="NA")
    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name_plural = "Registration"

# class Country(models.Model):
#     name=models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = "Country"

# class State(models.Model):
#     name=models.CharField(max_length=200)
#     country=models.ForeignKey(Country,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = "State"

# class City(models.Model):
#     name=models.CharField(max_length=200)
#     state=models.ForeignKey(State,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = "City"


class contactdetails(models.Model):
    name=models.CharField(max_length=200)
    mail=models.EmailField()
    subject=models.CharField(max_length=200)
    mssg=models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "contactdetails"



    

