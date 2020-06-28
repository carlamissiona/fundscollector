from django.contrib import admin
from django.urls import include,path
from . import views

from rest_framework import routers
from .api import restview

router = routers.DefaultRouter()
router.register(r'/loan', restview.LoanViewSet)
router.register(r'/member', restview.MemberViewSet)
router.register(r'/group', restview.GroupViewSet)
router.register(r'/loanpayment', restview.LoanPaymentsViewSet)
router.register(r'/savings', restview.SavingsViewSet)

urlpatterns = [

	path('', views.indexpage),
	path('about', views.aboutpage),
	path('tos', views.tospage),
	path('loans', views.loanspage),
	path('partners', views.partnerspage),
	path('login', views.loginformpage),
	path('signout', views.signout),

	path('api',  include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
