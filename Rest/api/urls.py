from restapp.views import index,person,PersonAPI,RegisterAPI,loginAPI


from django.urls import path

urlpatterns = [
    path('index/', index , name = 'index'),
    path('person/',person,name='person'),
    path('persons/',PersonAPI.as_view()),
    path('Register/',RegisterAPI.as_view()),
    path('login/',loginAPI.as_view()),

]