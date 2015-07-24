from django.shortcuts import render
from django.http import HttpResponseRedirect ,HttpResponse

from django.views.decorators.csrf import csrf_exempt
import json

from Pdf.pdf_engine import *
from Pdf.recommender import closest_user

# Create your views here.

@csrf_exempt
def upload_pdf(request):
	
	if request.method == "POST":
		
		destination_path = open("static/pdf/"+request.POST['file_name'], "wb+")
		pdf = request.FILES['pdf']
		destination_path.write(pdf.read())
		destination_path.close()
		json_data = {"status": "SUCCESSFUL"}
		word_cloud(request.POST['file_name'])
	else:
		json_data = {"status": "UNSUCCESSFUL"}
	
	return HttpResponse(json.dumps(json_data))


@csrf_exempt
def pdf_search(request):
	
	if request.method == "POST":
		json_data = probe_corpus()
		json_data['keywords'] = {request.POST['keywords']:1}
		args = []
		offset = int(request.POST['offset'])
		for i,x in enumerate(closest_user("keywords",json_data)[offset*10:(offset+1)*10]):
			args.append( {'id':str(i), 'name':x[1]} )
	else:
		args = {"status": "UNSUCCESSFUL"}
	
	return HttpResponse(json.dumps(args))


def pdf_show(request,pdf_id):

	return HttpResponse(open('static/pdf/'+pdf_id), content_type = 'application/pdf')
