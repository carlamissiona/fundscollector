from codesite.models import Loan, Member,Group

from django.views.generic.base import TemplateView , View
from django.views.generic import ListView, DetailView


from django.views import View
# Create your views here.
class LoansView(ListView):
    template_name = 'group-loans.html'
    context_object_name = 'object_list'
    model = Loan
    def get_queryset(self):
    	# google.googlemain()
    	#Feature before accessing home call google authentication
    	#Feature but google logged in must be the email of the registered user
        
    	query_objects = { 'loans' : Loan.objects.all()  }
    	return query_objects
