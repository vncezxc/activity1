from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from app.models import Contact, MembershipPlan, Trainer, Enrollment, Gallery, Attendance
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import User, Program, Split, Exercise, SplitExercise
from .forms import UserForm, ProgramForm, SplitForm, ExerciseForm, SplitExerciseForm 


class HomePageView (TemplateView):
    template_name = 'app/home.html'

class AboutPageView (TemplateView):
    template_name = 'app/about.html'

class ProductPageView (TemplateView):
    template_name = 'app/product.html'




# List View for Home Page
class HomePageView(TemplateView):
    template_name = 'app/home.html'


# User Views
class UserListView(ListView):
    model = User
    template_name = 'app/user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = User
    template_name = 'app/user_detail.html'
    

class UserCreateView(CreateView):
    model = User
    template_name = 'app/user_form.html'
    fields = ['username', 'email', 'gender', 'height', 'weight', 'goal']
    success_url = reverse_lazy('user_list')


class UserUpdateView(UpdateView):
    model = User
    template_name = 'app/user_update.html'
    fields = ['username', 'email', 'gender', 'height', 'weight', 'goal']
    success_url = reverse_lazy('user_list')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'app/user_delete.html'
    success_url = reverse_lazy('user_list')

class ProgramUpdateView(UpdateView):
    model = Program
    fields = [ 'user', 'program_name', 'goal', 'duration_weeks']
    template_name = 'app/program_update.html'

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'app/program_delete.html'
    success_url = reverse_lazy('program_list')

class ProgramDetailView(DetailView):
    model = Program
    context_object_name = 'prog'
    template_name = 'app/program_detail.html'
    

# Program Views
def program_list(request):
    programs = Program.objects.all()
    return render(request, 'app/program_list.html', {'programs': programs})


def program_add(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('program_list')
    else:
        form = ProgramForm()
    return render(request, 'app/program_form.html', {'form': form, 'title': 'Add New Program'})


def program_edit(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('program_list')
    else:
        form = ProgramForm(instance=program)
    return render(request, 'app/program_form.html', {'form': form, 'title': 'Edit Program'})


def program_delete(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    if request.method == 'POST':
        program.delete()
        return redirect('program_list')
    return render(request, 'app/program_confirm_delete.html', {'program': program})


def program_detail(request, program_id):
    program = get_object_or_404(Program, pk=program_id)
    return render(request,  'app/program_detail.html', {'program': program})

def Home(request):
    return render(request,"index.html")

def gallery(request):
    posts=Gallery.objects.all()
    context={"posts":posts}
    return render(request,"gallery.html",context)


def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    SelectTrainer=Trainer.objects.all()
    context={"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        phonenumber=request.POST.get('PhoneNumber')
        Login=request.POST.get('logintime')
        Logout=request.POST.get('loginout')
        SelectWorkout=request.POST.get('workout')
        TrainedBy=request.POST.get('trainer')
        query=Attendance(phonenumber=phonenumber,Login=Login,Logout=Logout,SelectWorkout=SelectWorkout,TrainedBy=TrainedBy)
        query.save()
        messages.warning(request,"Attendace Applied Success")
        return redirect('/attendance')
    return render(request,"attendance.html",context)

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    user_phone=request.user
    posts=Enrollment.objects.filter(PhoneNumber=user_phone)
    attendance=Attendance.objects.filter(phonenumber=user_phone)
    print(posts)
    context={"posts":posts,"attendance":attendance}
    return render(request,"profile.html",context)


from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST['usernumber']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

   
        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return render(request, "signup.html")

     
        User = get_user_model()

      
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, "signup.html")

     
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, "signup.html")

        try:
           
            myuser = User.objects.create_user(username=username, email=email, password=pass1)
            myuser.save()
            messages.success(request, "User created successfully. Please login.")
            return redirect('/login')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return render(request, "signup.html")

    return render(request, "signup.html")
        
   




def handlelogin(request):
    if request.method=="POST":        
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
            
        
    return render(request,"handlelogin.html")


def handleLogout(request):
    logout(request)
    messages.success(request,"Logout Success")    
    return redirect('/login')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()       
        messages.info(request,"Thanks for Contacting us we will get back you soon")
        return redirect('/contact')
        
    return render(request,"contact.html")


def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')

    Membership=MembershipPlan.objects.all()
    SelectTrainer=Trainer.objects.all()
    context={"Membership":Membership,"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        FullName=request.POST.get('FullName')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        PhoneNumber=request.POST.get('PhoneNumber')
        DOB=request.POST.get('DOB')
        member=request.POST.get('member')
        trainer=request.POST.get('trainer')
        reference=request.POST.get('reference')
        address=request.POST.get('address')
        query=Enrollment(FullName=FullName,Email=email,Gender=gender,PhoneNumber=PhoneNumber,DOB=DOB,SelectMembershipplan=member,SelectTrainer=trainer,Reference=reference,Address=address)
        query.save()
        messages.success(request,"Thanks For Enrollment")
        return redirect('/join')



    return render(request,"enroll.html",context)

