from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from ckeditor_uploader import views as ckeditor_views
urlpatterns = [
    path('', views.index, name= 'index'),
    path('about-us', views.aboutus, name= 'about-us'),
    path('training', views.training, name= 'training'),
    path('skill_development', views.skill_development, name= 'skill_development'),
    path('recruitments', views.recruitments, name= 'recruitments'),
    path('employee_performance_counselling', views.employee_performance_counselling, name= 'employee_performance_counselling'),
    path('our_trainers', views.our_trainers, name= 'our_trainers'),
    path('trainers/<int:pk>/', views.trainers_details, name='trainers_details'),
    path('blog', views.blog, name= 'blog'),
    path('blog/<int:pk>/', views.blog_details, name='blog_details'),
    path('blog/<int:pk>/add_comment/', views.add_comments, name='add_comments'),
    path('careers', views.careers, name= 'careers'),
    path('job_details/<str:job_position>/', views.job_details, name= 'job_details'),
    path('job_apply/<str:job_position>/', views.job_apply, name='job_apply'),
    path('contact', views.contact, name= 'contact'),



    path('user_login',views.user_login,name='user_login'),
    path('logout_user', views.logout_user, name='logout_user'),

    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    # client reviews
    path('add_client_reviews',views.add_client_reviews,name='add_client_reviews'),
    path('view_client_reviews',views.view_client_reviews,name='view_client_reviews'),
    path('update_client_reviews/<int:id>/',views.update_client_reviews,name='update_client_reviews'),
    path('delete_client_review/<int:id>/',views.delete_client_review,name='delete_client_review'),

    # clients logo
    path('add_clients_logo',views.add_clients_logo,name='add_clients_logo'),
    path('view_clients_logo',views.view_clients_logo,name='view_clients_logo'),
    path('update_clients_logo/<int:id>/',views.update_clients_logo,name='update_clients_logo'),
    path('delete_clients_logo/<int:id>/',views.delete_clients_logo,name='delete_clients_logo'),

    # Careers
    path('add_job_details',views.add_job_details,name='add_job_details'),
    path('view_job_details',views.view_job_details,name='view_job_details'),
    path('update_job_details/<int:id>',views.update_job_details,name='update_job_details'),
    path('delete_job_details/<int:id>',views.delete_job_details,name='delete_job_details'),

    # Candidate Details
    path('view_candidate_details', views.view_candidate_details, name='view_candidate_details'),
    path('delete_candidate_certificates/<int:id>/', views.delete_candidate_certificate, name='delete_candidate_certificates'),

    # Trainers
    path('add_trainers', views.add_trainers, name='add_trainers'),
    path('view_trainers',views.view_trainers,name='view_trainers'),
    path('update_trainer/<int:id>/',views.update_trainer,name='update_trainer'),
    path('delete_trainer/<int:id>/',views.delete_trainer,name='delete_trainer'),

    # Blogs
    path('add_blog_details', views.add_blog_details, name='add_blog_details'),
    path('view_blog_details',views.view_blog_details,name='view_blog_details'),
    path('update_blog_details/<int:id>/',views.update_blog_details,name='update_blog_details'),
    path('delete_blog_details/<int:id>/',views.delete_blog_details,name='delete_blog_details'),

    # Blog Comments
    path('admin_comments_view', views.admin_comments_view, name='admin_comments_view'),
    path('admin_delete_comment/<int:id>/', views.admin_delete_comment, name='admin_delete_comment'),

    # chatbot
    path('submit_query/',views.submit_query, name='submit_query'),
    path('chatbot_message_view',views.chatbot_message_view,name='chatbot_message_view'),
    path('delete_message/<int:id>/',views.delete_message,name='delete_message'),

    # Contact us
    path('contact_view',views.contact_view,name='contact_view'),
    path('delete_contact/<int:id>/',views.delete_contact,name='delete_contact'),

    path('ckeditor_upload/', views.ckeditor_upload, name='ckeditor_upload'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)