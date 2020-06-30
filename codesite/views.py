from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from codesite.models import Loan, Member,Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# # from django.views.decorators.http import require_POST  -- use with decorator above methofd
# @require_POST
# def cart_add(request, product_id):

from django.views import View
# Create your views here.
def indexpage(request):
    loans = Loan.objects.all().order_by('-duedate')[:12]
    return render(request, 'index.html', {'html': "page_title - Home", 'loans' : loans  })

def aboutpage(request):
    return render(request, 'about.html', {'title': " About " })

def tospage(request):
    return render(request, 'tos.html', {'title': " Terms of Service " })

def loginformpage(request):
    if request.user.is_authenticated:
        return redirect('/tos')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/about')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'title': " Login " })

def joinusformpage(request):
    return render(request, 'login.html', {'title': " Registration " })

@login_required(login_url="/login/")
def partnerspage(request):
    return render(request, 'login.html', {'title': " Registration " })

def loanspage(request):
    return render(request, 'loans.html', {'title': " List of Loans " })

@login_required
def signout(request):
    logout(request)
    return redirect('/about')
