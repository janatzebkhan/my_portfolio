from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Skill , Facts , Summery ,Professional_skill,Services,Portfolio,Partners,PortfolioItem,Contact
# Create your views here.
def index(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        
        Contact.objects.create(name=name,email = email,subject = subject, message= message)
        messages.success(request, message='you mrequset is successfully done')
        return redirect('/') 
            
    skill = Skill.objects.all()
    fact = Facts.objects.all()
    summery = Summery.objects.all()
    professional = Professional_skill.objects.all()
    service = Services.objects.all()
    portfolio = Portfolio.objects.all()
    partner = Partners.objects.all()
    context = {
        'skills': skill,
        'facts' : fact,
        'summeries':summery,
        'professionals':professional,
        'services': service,
        'portfolios':portfolio,
        'partners':partner,      
    }
        
    
    return render(request,'index.html',context)



    
def portfolio_details (request):
    portfolioItem = PortfolioItem.objects.all()
    context = {
        'portfolio_Items':portfolioItem,
        
        
    }
    return render (request,'portfolio_details.html',context)
