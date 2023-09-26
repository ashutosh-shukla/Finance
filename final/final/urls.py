"""
URL configuration for final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from final import views

urlpatterns = [
    path('admin/', admin.site.urls),
   
   
     #login and signup
     
    
     #dyanmic routes
    path('',views.home,name="home"),
    path('templates/home.html',views.homepage),
    path('foreign/',views.foreign,name='foreign'),
    path('mutualfunds/',views.mf),
    path('bonds/',views.bonds),
    path('etfs/',views.etfs),
    path('stocks/',views.stocks),

    #analysis

    path('funds/',views.funds),
    path('importing/',views.importing),
    path('gdp/',views.gdp),
    path('inflation/',views.inflation),
    path('intrest/',views.intrest),
    path('manu/',views.manu),
    
     #fundamental analysis

    path('fiscalpolicy/',views.fis),
    path('governmentpolicy/',views.gov),
    path('monetrypolicy/',views.mon),

    #personal finance

    path('literacy/',views.literacy),
    path('retirement/',views.ret),
    path('budget/',views.per),
    path('savings/',views.sav),
    path('taxes/',views.tax),
    path('loan/',views.loan),
    
   

     #news

    path('market/',views.mar),
    path('companies/',views.comp),
    path('economy/',views.eco),
    path('political/',views.poli),
    path('government/',views.gov),
    path('worldwide/',views.world),

    # learning
    path('beginners/',views.f),
    path('fanalysis/',views.ic),
    path('trading/',views.inc),
    path('investing/',views.tc),
    
    
    # login pages
      path('signup/',views.signuppage,name='signup'),
     path('login/',views.loginpage,name='login'),
      path('homepage/',views.homepage,name='homepage'),
       path('logout/',views.LogoutPage,name='logout'),
]



