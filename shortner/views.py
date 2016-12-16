from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import DockURL
from analytics.models import ClickEvent
from . forms import SubmitUrlForm
# Create your views here.

# def dock_redirect_view(request, shortcode = None, *args, **kwargs):
# 	obj = get_object_or_404(DockURL, shortcode = shortcode)
# 	print "check here "+str(obj.url)
# 	return HttpResponseRedirect(obj.url)

class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		context = {
			"title":"Niky.co",
			"form":the_form,
		}
		return render(request, "shortner/home.html", context)

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		context = {
			"title":"Niky.co",
			"form":form,
		}
		template = "shortner/home.html"
		if form.is_valid():
			new_url = form.cleaned_data.get('url')
			obj, created = DockURL.objects.get_or_create(url = new_url)
			context = {
			"object": obj,
			"created":created,
					}
			if created:
				template = "shortner/success.html"
			else:
				template = "shortner/already-exists.html"	
		return render(request, template, context)


class UrlRedirectView(View):
	def get(self, request, shortcode = None, *args, **kwargs):
		# obj = get_object_or_404(DockURL, shortcode = shortcode)
		qs = DockURL.objects.filter(shortcode__iexact= shortcode)
		if qs.count()!=1 and not qs.exists():
			raise Http404
		obj = qs.first()
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url+'/')
			

	


'''def dock_redirect_view(request, shortcode = None, *args, **kwargs):
	
	# try:
	# 	obj = DockURL.objects.get(shortcode  = shortcode)
	# except:
	# 	obj = DockURL.objects.all().first()
	# 
	
	obj = get_object_or_404(DockURL, shortcode = shortcode)
	# obj_url = obj.url
	# obj_url = None
	# qs = DockURL.objects.filter(shortcode__iexact = shortcode.upper())
	# if qs.exists() and qs.count() == 1:
	# 	obj = qs.first()
	# 	obj_url = obj.url
	return HttpResponse("Hello {sc}".format(sc = obj.url))
	'''		