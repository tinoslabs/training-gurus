from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.


# Client Reviews
class ClientReview(models.Model):
    client_name = models.CharField(max_length=100, null=True, blank=True)
    client_image = models.ImageField(upload_to='client_images/', null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    def __str__(self):
        return f"{self.client_name} - {self.designation}"

# Clients Logo

class Client_Logo(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    logo = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name

# Careers 
class Career_Model(models.Model):    
    job_position = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    salary = models.IntegerField()
    job_details = models.TextField(blank=True, null=True)
    posted_date = models.DateField()
    # end_date = models.DateField()
    post_end_date = models.DateTimeField()
    
    def is_active(self):
        return self.post_end_date >= timezone.now()

# Job application
class JobApplication(models.Model):
    career = models.ForeignKey(Career_Model, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    applied_date = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Trainers
class Trainer(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='trainers/', null=True, blank=True)
    training_video = models.FileField(upload_to='trainers/videos/', null=True, blank=True)

    def __str__(self):
        return self.name

# Blog
class Blog(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/',blank=True, null=True)
    created_date = models.DateTimeField(default=now,blank=True, null=True)

    def __str__(self):
        return self.name

# Blog Comment
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    comment_text = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=now,blank=True, null=True)

    def __str__(self):
        return f'Comment by {self.name}'

# Contact model

class ContactModel(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Chatbot
class ChatMessage(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"