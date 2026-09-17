from django.shortcuts import render,HttpResponse,redirect
from .models import Category,Courses,Registration,contactdetails
from .forms import registrform
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.contrib import messages
import random
from datetime import timedelta
from django.utils import timezone
from django.shortcuts import get_object_or_404  



# Create your views here.
def index(req):
    return render(req,'index.html')


def contact(request):
    if request.method=="POST":
        name=request.POST.get("username")
        mail=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        print(name,mail,subject,message)

        contactdetails_obj=contactdetails()
        contactdetails_obj.name=name
        contactdetails_obj.mail=mail
        contactdetails_obj.subject=subject
        contactdetails_obj.mssg=message
        contactdetails_obj.save()
        # return redirect('contact')

        try:
            subject_line=subject
            message=f"""
                Name: {name}<br>
                Email: {mail}<br>
                Subject: {subject}<br>
                Message:{message}
            """
            from_email = settings.EMAIL_HOST_USER
            toemail="joslienjeromias26@gmail.com"
            send_mail(subject_line, message, from_email,[toemail])
            messages.success(request, "success-popup")
        except:
             return redirect('/contact-scope-india.html?error=1')
        
    
        return redirect('/contact-scope-india.html?sent=1')
    else:
        return render(request,'contact.html')


def about(req):
    return render(req,'about.html')
def courses(req):
    data1=Courses.objects.filter(course_name="Data Science, AI, & Data Analytics Courses")
    data2=Courses.objects.filter(course_name="Software Courses")
    data3=Courses.objects.filter(course_name="Networking, Server, Cloud, & DevOps Courses")
    data4=Courses.objects.filter(course_name="Software Testing Courses")
    data5=Courses.objects.filter(course_name="Other Courses")
    return render(req,'courses.html',{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5})

# def load_states(request):
#     country_id=request.GET.get("country_id")
#     states=State.objects.filter(country_id=country_id).values('id','name')
#     return JsonResponse(list(states),safe=False)

# def load_city(request):
#     state_id=request.GET.get("state_id")
#     cities=City.objects.filter(state_id=state_id).values('id','name')
#     return JsonResponse(list(cities),safe=False)

def registration(request):
    # form=registrform()
    # return render(req,'registr.html',{'form':form})
    if request.method=="POST":
        form=registrform(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['fullname']
            dob=form.cleaned_data['dob']
            gender=form.cleaned_data['gender']
            qual=form.cleaned_data['qualification']
            num=form.cleaned_data['number']
            email=form.cleaned_data['email']
            guar_name=form.cleaned_data['guardian']
            occu=form.cleaned_data['occupation']
            guar_num=form.cleaned_data['mobile']
            course=form.cleaned_data['course']
            loc=form.cleaned_data['loc']
            mode=form.cleaned_data['Mode']
            time=form.cleaned_data['time']
            hobby=form.cleaned_data['hobby']
            add=form.cleaned_data['Address']
            coun=form.cleaned_data['country']
            state=form.cleaned_data['state']
            city=form.cleaned_data['city']
            pin=form.cleaned_data['pin']
            file=form.cleaned_data['files']
            Registration_obj=Registration()
            Registration_obj.fullname=name
            Registration_obj.dob=dob
            Registration_obj.gender=gender
            Registration_obj.qualification=qual
            Registration_obj.number=num
            Registration_obj.email=email
            Registration_obj.guardian=guar_name
            Registration_obj.occupation=occu
            Registration_obj.mobile=guar_num
            Registration_obj.course=course
            Registration_obj.loc=loc
            Registration_obj.mode=mode
            Registration_obj.time=time
            Registration_obj.hobbies=hobby
            Registration_obj.address=add
            Registration_obj.country=coun
            Registration_obj.state=state
            Registration_obj.city=city
            Registration_obj.pin=pin
            Registration_obj.file=file

            Registration_obj.save()
        
            subject = "Welcome to Our Website!"
            message = f"Hi {name},\n\nThank you for registering with us.\nYour account has been successfully created!"
            from_email = settings.EMAIL_HOST_USER
            toemail=[email]
            send_mail(subject, message, from_email,toemail)

            return HttpResponse("Data Saved to DB..................")


        
        else:
            return render(request, 'registr.html', {'form': form})
    
    else:
        form=registrform()
        return render(request,'registr.html',{'form':form})
    


def firstlogin(request):
    if request.method=="POST":
        action=request.POST.get("action")
        mail=request.POST.get("email")

        if action == "send_otp":

            data=Registration.objects.filter(email=mail)
            if data.exists():
                print("Email Exists")
                # show_email=False
                # show_otp=True
                print("it works")
                otp=str(random.randint(100000,999999))
                otp_time=timezone.now()+timedelta(minutes=5)
                subject = "OTP Verification"
                message = f"Hi Thank You For Loging In. Your OTP is {otp}. This otp is valid only for 5 minuites.Don't share otp with anyone"
                from_email = settings.EMAIL_HOST_USER
                toemail=[mail]
                send_mail(subject, message, from_email,toemail)
                print("Mail send")
                # first_obj=firs()
                # first_obj.email=mail
                # first_obj.otp=otp
                # first_obj.expire_time=otp_time
                first_obj = Registration.objects.filter(email=mail).last()
                first_obj.email = mail
                first_obj.otp = otp
                first_obj.expire_time=otp_time
                first_obj.save()
                print("saved to db")
                return render(request, "firstlogin.html", {
                    "show_email":True,
                    "show_otp": True,
                    "email": mail
                })

            else:
                print("Email does not exist")
                return render(request, "firstlogin.html", {"show_otp": False,"show_email":True,
            "error": "Email does not exist.Register here."
        })

        elif action == "verify_otp":
            # show_email=False
            show_otp=True
            mail=request.POST.get("email")
            user_otp=request.POST.get("otp_input")
            data=Registration.objects.filter(email=mail).last()
            print(data)

            if data and data.otp == user_otp and data.expire_time > timezone.now():
                print("OTP verified")
                return render(request,"firstlogin.html",{"show_email":False,
                    "show_otp": False,"show_pass":True,
                    "confirm_pass":True,"email": mail,})  
            else:
                print("OTP not verified")
                return render(request, "firstlogin.html", {
                    "show_email":True,
                    "show_otp": True,
                    "email": mail,
                    "any_error": "Invalid OTP or expired"
                })
        
        elif action =="send_pass":
            mail=request.POST.get("email")
            password=request.POST.get("pass")
            confirm=request.POST.get("conpass")

            if password!=confirm:
                return render(request, "firstlogin.html",{'Email': mail, "show_pass": True, "any_error": "Passwords do not match!"})
            pass_obj = Registration.objects.filter(email=mail).last()
            if pass_obj is not None:
                pass_obj.password = password
                pass_obj.confirm_password = confirm
                pass_obj.save()
                print("Password saved")
                return redirect("login")
            else:
        # No record found, prompt user to request OTP again
                return render(request, "firstlogin.html", {
                    "show_email": True,
                    "any_error": "Please verify OTP first before setting a password."
                })
    else:
        return render(request,"firstlogin.html",{"show_email":True})


def login(request):
    if request.GET.get("logout") == "true":

        print("Logging out...")

        request.session.flush()

        response = redirect('/login')
        response.delete_cookie('key')

        print("Logged out successfully")

        return response

    if request.COOKIES.get("key"):
        return redirect("dashboard")

    

    if request.method=="POST":
        mail=request.POST.get("email")    
        password=request.POST.get("password")    
        remember=request.POST.get("remember")

        data=Registration.objects.filter(email=mail).last()
        if data and data.password==password:
            request.session['session_mail']=mail
            print(request.session['session_mail'])
            response=redirect('/dashboard')
            # response.set_cookie('key',mail,max_age=30)
            print("Cookie set")
            if remember:  
                response.set_cookie("key", mail, max_age=7 * 24 * 60 * 60) 
                print("Cookie set for 7 days")
            else:
                response.set_cookie("key", mail)
                print("Cookie expires on browser close")
            # return render(request,"dashboard.html",{"data":data})
            return response
        
        else:
            request.session['login_error'] = "Invalid username or password"
            return redirect('/login')

    error = request.session.pop('login_error', None)
    return render(request, "login.html", {"error": error})




            
# Forgot password-------------------------------------------------!
def forgot(request):
    if request.method=="POST":
        mail=request.POST.get("email")
        action=request.POST.get("action")
        # value=Registration.objects.filter(email=mail)
        if action =="verify_email":
            value=Registration.objects.filter(email=mail)           
            if value.exists():
                print("Mail exists")
                request.session["reset_email"] = mail
                return render(request,"resetpass.html",{"show_pass":True,"confirm_pass":True,"show_email":False})
            else:
                return render(request,"resetpass.html",{"show_email":True,"error": "Email does not exist"})
            
        elif action=="send_pass":
            password=request.POST.get("pass")
            confirm=request.POST.get("conpass")
            mail=request.session.get("reset_email")
            if mail is None:
                return render(request, "resetpass.html", {
                    "show_email": True,
                    "error": "Session expired! Please verify email again."
                })

            user = Registration.objects.filter(email=mail).last()
            if user is None:
                return render(request, "resetpass.html", {
                    "show_email": True,
                    "error": "User not found! Please register."
                })

            if password== confirm:
                user = Registration.objects.filter(email=mail).last()
                user.password = password
                user.confirm_password=confirm   
                user.save()

                del request.session["reset_email"]
                return redirect("login")
            
        
            return render(request, "resetpass.html", {
                "show_pass": True,
                "confirm_pass": True,
                "show_email": False,
                "error": "Passwords do not match!"
            })
        else:

            return render(request, "resetpass.html", {"show_email": True})

    else:

        return render(request,"resetpass.html",{"show_email":True})




def dashboard(request):
    data=request.session.get('session_mail')

    
    value= request.COOKIES.get('key')
    print("Cookie value is",value)

    if value==None and data==None:
        return render(request,"login.html",{"error":"Login Here .To access Dashboard"})
    if value and not data:
        request.session['session_mail'] = value
        data = value
    
    reg = Registration.objects.get(email=data)
 
    enrolled_courses = reg.course.split(',') 

   
    

    return render(request,'dashboard.html',{'data':data,'details':reg,'enrolled_courses':enrolled_courses})


def edit(request):
    data=request.session.get('session_mail')
    details = Registration.objects.filter(email=data).last()
    data1=Courses.objects.filter(course_name="Data Science, AI, & Data Analytics Courses")
    data2=Courses.objects.filter(course_name="Software Courses")
    data3=Courses.objects.filter(course_name="Networking, Server, Cloud, & DevOps Courses")
    data4=Courses.objects.filter(course_name="Software Testing Courses")
    data5=Courses.objects.filter(course_name="Other Courses")
    if request.method=="POST":
        details.fullname=request.POST.get("fullname")
        details.dob=request.POST.get("dob")
        details.gender=request.POST.get("gender")
        details.qualification=request.POST.get("qual")
        details.number=request.POST.get("number")
        details.guardian=request.POST.get("guardian")
        details.occupation=request.POST.get("occupation")
        details.mobile=request.POST.get("guard_mobile")
        details.course=request.POST.get("course")
        details.loc=request.POST.get("loc")
        details.mode=request.POST.get("mode")
        details.time=request.POST.get("time")
        details.hobbies=request.POST.get("hobby")
        details.address=request.POST.get("address")
        details.country=request.POST.get("country")
        details.state=request.POST.get("state")
        details.city=request.POST.get("city")
        details.pin=request.POST.get("pin")

        if request.FILES.get("image"):
            details.file = request.FILES.get("image")


        details.save()
        return redirect("dashboard")
    return render(request, "editprofile.html", {"details": details,"data1": data1,
    "data2": data2,
    "data3": data3,
    "data4": data4,
    "data5": data5})




def coursedetails(request):
    data1=Courses.objects.filter(course_name="Data Science, AI, & Data Analytics Courses")
    data2=Courses.objects.filter(course_name="Software Courses")
    data3=Courses.objects.filter(course_name="Networking, Server, Cloud, & DevOps Courses")
    data4=Courses.objects.filter(course_name="Software Testing Courses")
    data5=Courses.objects.filter(course_name="Other Courses")
    data=request.session.get('session_mail')
    reg = Registration.objects.get(email=data)
 
    enrolled_courses = reg.course.split(',') 

    return render(request,"coursedetails.html",{'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data5,'enrolled_courses': enrolled_courses})


def enroll(request):
    if request.method == "POST":
        mail = request.session.get('session_mail')
        new_course = request.POST.get("course")


        reg = Registration.objects.get(email=mail)


        # get current courses as a list
        course_list = reg.course.split(',') if reg.course else []

        if new_course in course_list:
            messages.info(request, "You have already enrolled in this course.")
        else:
            course_list.append(new_course)
            reg.course = ','.join(course_list)
            reg.save()
            messages.success(request, "You are signed up for this course successfully!")

    return redirect("coursedetails")


def course_detail(request, course_id):
    course = get_object_or_404(Courses, id=course_id)


    data = request.session.get('session_mail')
    enrolled_courses = []
    if data:
        reg = Registration.objects.get(email=data)
        enrolled_courses = reg.course.split(',') if reg.course and reg.course != 'Na' else []

    already_enrolled = course.sub_courses in enrolled_courses

    return render(request, "courseid.html", {
        "course": course,
        "already_enrolled": already_enrolled
    })


        



