from django.http import HttpResponse
from django.template import Context , RequestContext
from django.template.loader import get_template
from django.contrib.auth import authenticate, logout
from teacherAvaluation.models import *
from django.http import Http404

def mainpage(request):
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
		'contentbody': 'Benvinguts a el aplicatiu de evaluacio de docencia , navega pel menu per veure el llistat de les diferents entitats.'
		})
	output = template.render(variables)
	context_instance = RequestContext(request)
	return HttpResponse(output,context_instance)

def teacher(request):
	template = get_template('teachers.html')
	listOfTeachers = Teacher.objects.all()
	variables = Context({
		'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
		'contentbody': 'Llistat de Professors:',
		'teachers_list' : listOfTeachers
		})
	output = template.render(variables)
	context_instance = RequestContext(request)
	return HttpResponse(output,context_instance)

def singular_teacher(request,teacher_id):
	#template= get_template('single_teacher.html')
	try:
		template= get_template('single_teacher.html')
		teacher = Teacher.objects.get(idTeacher=teacher_id)
		variables = Context({
			'contentbody': 'Dades Personals Professor:',
			'titlehead': 'Teacher Avaluation',
			'pagetitle': 'Evaluacio de docencia',
			'nameteacher': teacher.name,
			'sex': teacher.sexe,

			'nationality': teacher.nationality
			})
		output = template.render(variables)
		context_instance = RequestContext(request)
	except:
		raise Http404
       		
	return HttpResponse(output,context_instance)


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
	context_instance = RequestContext(request)
	return HttpResponse(output,context_instance)

def subject(request):
	template = get_template('subjects.html')
	listOfSubjects = Subject.objects.all()
	variables = Context({
		'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
		'contentbody': 'Llistat de Assignatures:',
		'subjects_list' : listOfSubjects
		})
	output = template.render(variables)
	context_instance = RequestContext(request)
	return HttpResponse(output,context_instance)

def evaluation(request):
	template = get_template('evaluation.html')
	listOfEvaluation = Evaluation.objects.all()
	variables = Context({
		'titlehead': 'Teacher Avaluation',
		'pagetitle': 'Evaluacio de docencia',
		'contentbody': 'Llistat de Evaluacions - Professors:',
		'evaluation_list' : listOfEvaluation
		})
	output = template.render(variables)
	context_instance = RequestContext(request)
	return HttpResponse(output,context_instance)

def logoutPage(request):
	logout(request)
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'Log out',
		'contentbody': 'Has tancat la sessio.',
		})

	output = template.render(variables)
	context_instance = RequestContext(request)
	return HttpResponse(output,context_instance)
