import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import ClientReview,ChatMessage, ContactModel, Client_Logo, Career_Model, Trainer, Blog, Comment, JobApplication
from .forms import ClientReviewForm, ContactModelForm, Client_Logo_Form, CareerForm, TrainersForm, BlogForm, CommentForm, JobApplicationForm






# Create your views here.
def index(request):
    clients_reviews = ClientReview.objects.all()
    client_logo = Client_Logo.objects.all()
    blogs = list(Blog.objects.all())
    random.shuffle(blogs)

    trainers = list(Trainer.objects.all())
    random.shuffle(trainers)
    return render(request, 'index.html',{'clients_reviews': clients_reviews, 'client_logo':client_logo,'blogs': blogs[:3],'trainers':trainers[:4]})

def aboutus(request):
    clients_reviews = ClientReview.objects.all()
    client_logo = Client_Logo.objects.all()
    trainers = list(Trainer.objects.all())
    random.shuffle(trainers)
    return render(request, 'about-us.html',{'clients_reviews': clients_reviews,'client_logo':client_logo,'trainers':trainers[:4]})

def training(request):
    client_logo = Client_Logo.objects.all()
    return render(request, 'training.html',{'client_logo':client_logo})

def skill_development(request):
    client_logo = Client_Logo.objects.all()
    return render(request, 'skill_development.html',{'client_logo':client_logo})

def recruitments(request):
    client_logo = Client_Logo.objects.all()
    return render(request, 'recruitments.html',{'client_logo':client_logo})

def employee_performance_counselling(request):
    client_logo = Client_Logo.objects.all()
    return render(request, 'employee_performance_counselling.html',{'client_logo':client_logo})

def our_trainers(request):
    trainers = Trainer.objects.all()
    return render(request, 'our_trainers.html',{'trainers':trainers})

def trainers_details(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    return render(request, 'trainers_details.html',{'trainer':trainer})

def blog(request):
    blogs = Blog.objects.all().order_by('-created_date')
    return render(request, 'blog.html', {'blogs': blogs})

def blog_details(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = blog.comments.all().order_by('-id')
    recent_blogs = Blog.objects.all().order_by('-created_date')[:5] 

    return render(request, 'blog_details.html', {
        'blog': blog,
        'comments': comments,
        'recent_blogs': recent_blogs,
    })

def add_comments(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment_text = request.POST.get('comment_text')
        
        if name and email and comment_text:
            Comment.objects.create(blog=blog, name=name, email=email, comment_text=comment_text)
            messages.success(request, 'Your comment has been successfully added!')
        else:
            messages.error(request, 'All fields are required.')

    return redirect('blog_details', pk=pk)

def careers(request):
    jobs = Career_Model.objects.filter()
    return render(request, 'careers.html',{'jobs':jobs})

def job_details(request,job_position):
    job_details = get_object_or_404(Career_Model, job_position=job_position)
    return render(request,'job_details.html',{'job_details':job_details})

def job_apply(request, job_position):
    job = get_object_or_404(Career_Model, job_position=job_position)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.career = job
            application.save()
            messages.success(request, 'Your application has been submitted successfully.')
            return redirect('job_apply', job_position=job_position)
    else:
        form = JobApplicationForm()

    return render(request, 'job_apply.html', {'form': form, 'job': job})

def contact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your submission has been successfully sent!')
            return redirect('contact')
    else:
        form = ContactModelForm()
    return render(request,'contact.html',{'form': form})


@csrf_protect
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.success(request, ("There Was An Error Loging In, Try Again..."))
            return redirect('user_login')
    return render(request, 'authenticate/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out"))
    return redirect('index')

 

@login_required(login_url='user_login')
def admin_dashboard(request):
    return render(request,'admin_pages/admin_dashboard.html')


# Client Reviews
@login_required(login_url='user_login')
def add_client_reviews(request):
    if request.method == 'POST':
        form = ClientReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_client_reviews') 
    else:
        form = ClientReviewForm()

    return render(request, 'admin_pages/add_client_reviews.html', {'form': form})


@login_required(login_url='user_login')
def view_client_reviews(request):
    client_reviews = ClientReview.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_client_reviews.html', {'client_reviews': client_reviews})


@login_required(login_url='user_login')
def update_client_reviews(request, id):
    client_reviews = get_object_or_404(ClientReview, id=id)
    if request.method == 'POST':
        form = ClientReviewForm(request.POST, request.FILES, instance=client_reviews)
        if form.is_valid():
            form.save()
            return redirect('view_client_reviews')
    else:
        form = ClientReviewForm(instance=client_reviews)
    return render(request, 'admin_pages/update_client_reviews.html', {'form': form, 'client_reviews': client_reviews})

    

@login_required(login_url='user_login')
def delete_client_review(request,id):
    client_reviews = ClientReview.objects.get(id=id)
    client_reviews.delete()
    return redirect('view_client_reviews')

# Client Logo
@login_required(login_url='user_login')
def add_clients_logo(request):
    if request.method == 'POST':
        form = Client_Logo_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_clients_logo') 
    else:
        form = Client_Logo_Form()

    return render(request, 'admin_pages/add_clients_logo.html', {'form': form})

@login_required(login_url='user_login')
def view_clients_logo(request):
    logo = Client_Logo.objects.all().order_by('-id')
    return render(request,'admin_pages/view_clients_logo.html',{'logo':logo})

@login_required(login_url='user_login')
def update_clients_logo(request,id):
    logos = get_object_or_404(Client_Logo, id=id)
    if request.method == 'POST':
        form = Client_Logo_Form(request.POST, request.FILES, instance=logos)
        if form.is_valid():
            form.save()
            return redirect('view_clients_logo')
    else:
        form = Client_Logo_Form(instance=logos)
    return render(request, 'admin_pages/update_clients_logo.html', {'form': form, 'logos': logos})

@login_required(login_url='user_login')
def delete_clients_logo(request,id):
    logos = Client_Logo.objects.get(id=id)
    logos.delete()
    return redirect('view_clients_logo')

# Add Job Details
@login_required(login_url='user_login')
def add_job_details(request):
    if request.method == 'POST':
        form = CareerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_job_details') 
    else:
        form = CareerForm()

    return render(request, 'admin_pages/add_job_details.html', {'form': form})

@login_required(login_url='user_login')
def view_job_details(request):
    job_details = Career_Model.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_job_details.html', {'job_details': job_details})

@login_required(login_url='user_login')
def update_job_details(request, id):
    job_details = get_object_or_404(Career_Model, id=id)
    if request.method == 'POST':
        form = CareerForm(request.POST, request.FILES, instance=job_details)
        if form.is_valid():
            form.save()
            return redirect('view_job_details')
    else:
        form = CareerForm(instance=job_details)
    return render(request, 'admin_pages/update_job_details.html', {'form': form, 'job_details': job_details})


@login_required(login_url='user_login')
def delete_job_details(request,id):
    job_details = Career_Model.objects.get(id=id)
    job_details.delete()
    return redirect('view_job_details')

# Job Application
@login_required(login_url='user_login')
def view_candidate_details(request):
    certificates = JobApplication.objects.all().order_by('-id')
    context = {
        'certificates': certificates,
    }
    return render(request, 'admin_pages/view_candidate_details.html', context)

@login_required(login_url='user_login')
def delete_candidate_certificate(request, id):
    certificate = get_object_or_404(JobApplication, id=id)
    certificate.delete()
    return redirect('view_candidate_details')

# Trainers

@login_required(login_url='user_login')
def add_trainers(request):
    if request.method == 'POST':
        form = TrainersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_trainers') 
    else:
        form = TrainersForm()

    return render(request, 'admin_pages/add_trainers.html', {'form': form})


@login_required(login_url='user_login')
def view_trainers(request):
    trainers = Trainer.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_trainers.html', {'trainers': trainers})


@login_required(login_url='user_login')
def update_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == 'POST':
        form = TrainersForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('view_trainers')
    else:
        form = TrainersForm(instance=trainer)
    return render(request, 'admin_pages/update_trainers.html', {'form': form, 'trainer': trainer})

@login_required(login_url='user_login')
def delete_trainer(request,id):
    trainer = Trainer.objects.get(id=id)
    trainer.delete()
    return redirect('view_trainers')

# Trainers

@login_required(login_url='user_login')
def add_blog_details(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_blog_details') 
    else:
        form = BlogForm()

    return render(request, 'admin_pages/add_blog_details.html', {'form': form})


@login_required(login_url='user_login')
def view_blog_details(request):
    blogs = Blog.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_blog_details.html', {'blogs': blogs})


@login_required(login_url='user_login')
def update_blog_details(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('view_blog_details')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'admin_pages/update_blog_details.html', {'form': form, 'blog': blog})

@login_required(login_url='user_login')
def delete_blog_details(request,id):
    blogs = Blog.objects.get(id=id)
    blogs.delete()
    return redirect('view_blog_details')


# Blog Comments
@login_required(login_url='user_login')
def admin_comments_view(request):
    comments = Comment.objects.all().order_by('-id')
    return render(request, 'admin_pages/admin_comments_view.html', {'comments': comments})

# You might need a delete view for comments, like admin_delete_comment
@login_required(login_url='user_login')
def admin_delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('admin_comments_view')

# Contact 
@login_required(login_url='user_login')
def contact_view(request):
    contacts = ContactModel.objects.all().order_by('-id')
    return render(request,'admin_pages/contact_view.html',{'contacts':contacts})

@login_required(login_url='user_login')
def delete_contact(request,id):
    contact = ContactModel.objects.get(id=id)
    contact.delete()
    return redirect('contact_view')



# Chatbot 
def submit_query(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and phone_number and email and message:
            # Save the data to the ChatMessage model
            ChatMessage.objects.create(
                name=name,
                phone_number=phone_number,
                email=email,
                message=message
            )
            return JsonResponse({'message': 'Data saved successfully'}, status=200)
        else:
            return JsonResponse({'error': 'All fields are required'}, status=400)

@login_required(login_url='user_login')
def chatbot_message_view(request):
    chatbot = ChatMessage.objects.all().order_by('-id')
    return render(request,'admin_pages/chatbot_message_view.html',{'chatbot':chatbot})

@login_required(login_url='user_login')
def delete_message(request,id):
    chatbot = ChatMessage.objects.get(id=id)
    chatbot.delete()
    return redirect('chatbot_message_view')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

@csrf_exempt
def ckeditor_upload(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        upload = request.FILES['upload']
        file_extension = os.path.splitext(upload.name)[1].lower()
        
        # Check if the uploaded file is an image or a PDF
        if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']:
            folder = 'images'
        elif file_extension == '.pdf':
            folder = 'pdfs'
        else:
            return JsonResponse({'uploaded': False, 'error': 'Unsupported file type.'})

        # Save the file in the appropriate folder
        file_name = default_storage.save(f'{folder}/{upload.name}', ContentFile(upload.read()))
        file_url = default_storage.url(file_name)
        return JsonResponse({
            'uploaded': True,
            'url': file_url
        })
    
    return JsonResponse({'uploaded': False, 'error': 'No file was uploaded.'})