from django import forms
from .models import ClientReview, ContactModel, Client_Logo, Career_Model, Trainer, Blog, Comment, JobApplication

# Clien Review
class ClientReviewForm(forms.ModelForm):
    class Meta:
        model = ClientReview
        fields = '__all__'

# Clients Logo
class Client_Logo_Form(forms.ModelForm):
    class Meta:
        model = Client_Logo
        fields = '__all__'

# Trainer
class TrainersForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'

# Blog
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

# Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

# Careers 
class CareerForm(forms.ModelForm):
    class Meta:
        model = Career_Model
        fields = '__all__'

# Job Application 
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'resume']

# Contact us
class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'