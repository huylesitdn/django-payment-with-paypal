from django.shortcuts import render
from django.http import HttpResponse

from .models import Plan

# Create your views here.
def index(request):
  plans = Plan.objects.all()
  print(plans[1].price)
  return render(request, 'plans/index.html', {'plans': plans, 'price_basic_ye': plans[1].price, 'price_pro_ye': plans[3].price})

def plansDetail(request, pk):
  plans = Plan.objects.all()
  plan = Plan.objects.get(id=pk)

  if plan.limit == True:
    switch_plan = 'Pro'
    switch_plan_id = plans[2].id
  else:
    switch_plan = 'Basic'
    switch_plan_id = plans[0].id

  return render(request, 'plans/checkout.html', {
    'id': pk,
    'plan': plan,
    'price_basic_ye': plans[1].price, 
    'price_pro_ye': plans[3].price,
    'switch_plan': switch_plan,
    'switch_plan_id': switch_plan_id
  })

def plansStatus(request, pk, status):
  if status == 'success':
    return render(request, 'plans/status/success.html')
  else :
    return render(request, 'plans/status/error.html')