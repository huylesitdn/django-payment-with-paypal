from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request, 'plans/index.html', {})

def plansDetail(request, pk):
  return render(request, 'plans/checkout.html', {
    'plan': pk
  })

def plansStatus(request, pk, status):
  if status == 'success':
    return render(request, 'plans/status/success.html')
  else :
    return render(request, 'plans/status/error.html')