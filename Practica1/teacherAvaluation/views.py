from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth import authenticate, login, logout
from teacherAvaluation.models import *

def mainpage(request):
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
		'contentbody': 'Benvinguts a el aplicatiu de evaluacio de docencia , navega pel menu per veure el llistat de les diferents entitats.'
		})
	output = template.render(variables)
	return HttpResponse(output)

def teacher(request):
	template = get_template('teachers.html')
	listOfTeachers = Teacher.objects.all()
	variables = Context({
		'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
		'contentbody': 'Llistat de teachers:',
		'teachers_list' : listOfTeachers
		})
	output = template.render(variables)
	return HttpResponse(output)

def degree(request):
	template = get_template('degrees.html')
	listOfDegrees = Degree.objects.all()
	variables = Context({
		'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
		'contentbody': 'Llistat de Carreres:',
		'degrees_list' : listOfDegrees
		})
	output = template.render(variables)
	return HttpResponse(output)

def subject(request):
	template = get_template('subjects.html')
	listOfSubjects = Subject.objects.all()
	variables = Context({
		'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
		'contentbody': 'Llistat de Carreres:',
		'subjects_list' : listOfSubjects
		})
	output = template.render(variables)
	return HttpResponse(output)

def evaluation(request):
	template = get_template('evaluation.html')
	listOfEvaluation = Evaluation.objects.all()
	variables = Context({
		'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
		'contentbody': 'Llistat de resultats evaluacio:',
		'evaluation_list' : listOfEvaluation
		})
	output = template.render(variables)
	return HttpResponse(output)

def logoutPage(request):
	logout(request)
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'Log out',
		'contentbody': 'Has tancat la sessio.',
		})
	output = template.render(variables)
	return HttpResponse(output)
