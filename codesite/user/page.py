from codesite.models import Savings, Loan
from codesite.user.forms import FormSavings
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.base import TemplateView , View
from django.views.generic import ListView, DetailView
from django.views import View
import logging


class SavingsObjectMixin:
    model = Savings
    params = 'id'
    def get_object(self):
        qs = super().get_queryset()
        obj = qs.filter(memberid=self.request.user.id)
        return obj


class SavingsDetailView(SavingsObjectMixin, DetailView):
    template_name = "savings-detail.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        qs = self.object
        context = super(SavingsDetailView, self).get_context_data(**kwargs)
        context["object"] = qs.filter(id=self.kwargs.get("id"))

        return context


class SavingsListView(SavingsObjectMixin,ListView):
    model = Savings
    paginate_by = 4
    template_name = 'user-savings.html'
    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(memberid=self.request.user.id)
        return qs.filter(memberid=self.request.user.id)

def AddSavingsPage(request):
    html = 'Pay Savings'
    context = {  'page_title' : 'Add Savings' }
    logging.error("Saving Saving Saving")
    logging.error(request)
    logging.error(vars(request))
    add_savings = FormSavings()
    if request.method == 'POST':
        add_savings = FormSavings(request.POST)

        if add_savings.is_valid():
            try:
                s3 = Savings(memberid=request.user.id, amount=add_savings.cleaned_data["amount"] ,
                                        interest=add_savings.cleaned_data["interest"] ,
                                        scheme=add_savings.cleaned_data["scheme_field"] ,
                                        duration=add_savings.cleaned_data["duration"], duedate=add_savings.cleaned_data["duedate"], )
                s3.save()

            except  Exception as inst:
              logging.warning("An exception occurred")
              logging.error("An exception occurred")
              logging.error(type(inst))
              logging.warning( inst.args )

              raise
        return HttpResponseRedirect('/tos')
    else:
        html = 'Pay Savings In Your Nearest 7Eleven Store'

    return render(request, 'add-savings.html', {'html': html, 'form': add_savings} )
            # logging.error("Saving Saving Saving POST")
            # logging.error("Saving Saving Saving POST")
            # logging.error("Saving Saving Saving POST csrf_processing_done")
            # logging.error(   request.csrf_processing_done )
            # logging.error(   request.csrf_processing_done )
        # add_savings.cleaned_data["amount"]
        # add_savings.cleaned_data["interest"]
        # add_savings.cleaned_data["scheme_field"]
        # add_savings.cleaned_data["duration"]
        # logging.error( add_savings.cleaned_data["duedate"] )
        # logging.error( add_savings.cleaned_data["duedate"] )
    # logging.error("signform valisssd before csrf")
    # logging.error("signform valisssd before csrf")
    # logging.error("signform valisssd before csrf")
    #
    # logging.error("signform valisssd")
    # logging.error("signform valisssd")
    # logging.error(add_savings.is_valid())
    # logging.error(add_savings.is_bound)
    # logging.error(add_savings.errors.as_json())

        # logging.error("Saving Saving Saving VAR REQUEST")
        # logging.error("Saving Saving Saving VAR _post")
        # logging.error("Saving Saving Saving VAR _post")
        # logging.error(request._post)
        # logging.error(request._body)
        # logging.error(request.environ)
        # logging.error(" self.object  self.object  self.object ")
        # logging.error(" self.object  self.object  self.object ")
        # logging.error( self.object )
        # logging.error(qs.filter(id=self.kwargs.get("id")))
        # logging.error(vars(qs.query) )
        # logging.error(qs )
        # logging.error("-----Context-----")
        # logging.error( self.object.filter(id=self.kwargs.get("id"))  )
        # logging.error("--Context--")
        # logging.error( vars(self.object[1]) )
        # logging.error("--Context--")
        # logging.error( self.object.filter(id=self.kwargs.get("id")) )
        # logging.error("Context")
        # logging.error(vars( super(SavingsDetailView, self) ))

        # logging.error(context["object"])
