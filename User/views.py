from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect ,HttpResponse
from django.core.context_processors import csrf
from django.contrib import auth

from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.views.decorators.csrf import csrf_exempt

from forms import member_registration_form, member_update_form
from django.contrib.auth.models import User

#from Article.models import article
import json
# Create your views here.

@csrf_exempt
def register(request):
	
	args = {}
	args['Signed_In'] = False
	args['Error'] = []
	
	Username = request.POST.get('username',None)
	Email = request.POST.get('email',None)
	First_name = request.POST.get('first_name',None)
	Password = request.POST.get('password',None)
	
	print Username
	
	if None in [Username,Email,First_name,Password]:
		args['Error'].append('Invalid User Data')
	else:
		if len(User.objects.filter(username = Username)) + len(User.objects.filter(email = Email))==0:
			User(
				username = Username,
				email = Email,
				first_name = First_name,
				password = Password,
			).save()
			args['Signed_In'] = True
		else:	
			args['Error'].append('Username or Email already registered')
			
	return HttpResponse(json.dumps(args),content_type='application/json')


@csrf_exempt
def login(request):

	args = {}
	args['Logged_In'] = False
	args['Error'] = []
	
	Username = request.POST.get('username',None)
	Password = request.POST.get('password',None)
	
	if len(User.objects.filter(username=Username,password=Password))==1:
		args['Logged_In'] = True
	else:
		args['Error'].append('Invalid Login')
	
	return HttpResponse(json.dumps(args),content_type='application/json')

'''
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profile(request):

	if request.user == AnonymousUser():
			return HttpResponseRedirect('/login')
	
	letter_length = 250
	
	articles = article.objects.filter(user=request.user.username).order_by('hits')[::-1]
	for an_article in articles:
		if len(an_article.content)>letter_length:
			an_article.content = an_article.content[:letter_length]+'...'
			
	return render_to_response('user_profile.html', 
		{
		'user':request.user.username, 
		'articles':articles
		}
	)


@login_required(login_url='/login')
def update(request):
	
	if request.user == AnonymousUser():
			return HttpResponseRedirect('/login')
	
	if request.POST:
		form = member_update_form(request.POST,request.FILES,instance=request.user.profile)
		if form.is_valid():
			a = form.save(commit = False)
			a.save()
			return HttpResponseRedirect('/profile')
	else:
		user = request.user
		profile = user.profile
		form  = member_update_form(instance = profile)
		
	args = {}
	args.update(csrf(request))
	args['form'] = form
		
	return render_to_response('user_update.html',args)
	
	
@cache_control(no_cache=True, must_revalidate=True, no_store=True)	
def logout(request):
	
	if hasattr(request, 'user'):
	     	request.user = AnonymousUser()
	
	auth.logout(request)
	request.session.flush()
	
	return HttpResponseRedirect('/')
'''
