from django.contrib import admin
from django.urls import include,path
from . import views
from .group import page as groupview
from .user import page as userview

from rest_framework import routers
from .api import restview

router = routers.DefaultRouter()
router.register(r'/loan', restview.LoanViewSet)
router.register(r'/member', restview.MemberViewSet)
router.register(r'/group', restview.GroupViewSet)
router.register(r'/loanpayment', restview.LoanPaymentsViewSet)
router.register(r'/savings', restview.SavingsViewSet)
# router.register(r'/savings/passdue',restview.SavingsViewSet)

urlpatterns = [

	path('', views.indexpage),
	path('about', views.aboutpage),
	path('tos', views.tospage),
	path('loans', views.loanspage),
	path('partners', views.partnerspage),
	path('login', views.loginformpage),
	path('signout', views.signout),

	# path('passbook', views.signout),
	path('passbook/savings', userview.SavingsListView.as_view() ),
	path('passbook/savings/<int:id>', userview.SavingsDetailView.as_view() ),
	path('passbook/savings/print/<int:id>', userview.SavingsDetailView.as_view() ),
	path('passbook/add/savings', userview.AddSavingsPage ),
	path('passbook/add/loans', userview.AddLoansPage ),
	# path('passbook/loans', views.signout),


	path('group/loans', groupview.LoansView.as_view() ),
	# path('group/savings', views.savings),
	# path('group/<int:salesid>', views.list),





	path('api',  include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
