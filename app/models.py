from django.db import models
from django.urls import reverse



class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    goal = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Program(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=100)
    goal = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    duration_weeks = models.IntegerField()

    def __str__(self):
        return f"{self.program_name} ({self.user.username})"
    
    def get_absolute_url(self):
        return reverse('program_detail', kwargs={"pk": self.pk})


class Split(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    day = models.IntegerField()
    split_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.split_name} - Day {self.day} ({self.program.program_name})"


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=100)
    muscle_group = models.CharField(max_length=50)
    equipment_needed = models.CharField(max_length=50)
    exercise_type = models.CharField(max_length=50)

    def __str__(self):
        return self.exercise_name


class SplitExercise(models.Model):
    split = models.ForeignKey(Split, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    order = models.IntegerField()
    sets = models.IntegerField()
    reps = models.IntegerField()
    rest_time = models.IntegerField(help_text="Rest time in seconds")

    def __str__(self):
        return f"{self.exercise.exercise_name} in {self.split.split_name}"

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    body_fat_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    muscle_mass_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Progress on {self.date} for {self.user.username}"
    
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12)
    description=models.TextField()

    def __str__(self):
        return self.email

class Enrollment(models.Model):        
    FullName=models.CharField(max_length=25)
    Email=models.EmailField()
    Gender=models.CharField(max_length=25)
    PhoneNumber=models.CharField(max_length=12)
    DOB=models.CharField(max_length=50)
    SelectMembershipplan=models.CharField(max_length=200)
    SelectTrainer=models.CharField(max_length=55)
    Reference=models.CharField(max_length=55)
    Address=models.TextField()
    paymentStatus=models.CharField(max_length=55,blank=True,null=True)
    Price=models.IntegerField(max_length=55,blank=True,null=True)
    DueDate=models.DateTimeField(blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True,)

    def __str__(self):
        return self.FullName

class Trainer(models.Model):
    name=models.CharField(max_length=55)
    gender=models.CharField(max_length=25)
    phone=models.CharField(max_length=25)
    salary=models.IntegerField(max_length=25)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name

class MembershipPlan(models.Model):
    plan=models.CharField(max_length=185)
    price=models.IntegerField(max_length=55)

    def __int__(self):
        return self.id


class Gallery(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='gallery')
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __int__(self):
        return self.id


class Attendance(models.Model):
    Selectdate=models.DateTimeField(auto_now_add=True)
    phonenumber=models.CharField(max_length=15)
    Login=models.CharField(max_length=200)
    Logout=models.CharField(max_length=200)
    SelectWorkout=models.CharField(max_length=200)
    TrainedBy=models.CharField(max_length=200)
    def __int__(self):
        return self.id
