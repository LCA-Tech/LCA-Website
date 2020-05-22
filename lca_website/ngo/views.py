from django.shortcuts import render, HttpResponseRedirect
from django.http import *
from .forms import SignupForm
from .models import Ngo
from django.template import loader


def homepage(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    response = "The links in this page redirects you to the respective ngo pages"
    print (response)
    k = Ngo.objects.order_by('name')
    template = loader.get_template('ngo/index.html')
    context = {
        'k': k,
    }
    return HttpResponse(template.render(context, request))


def detail(request, name):
    response = "These are NGO details "
    print(response)
    try:
        k = Ngo.objects.get(pk=name)
    except Ngo.DoesNotExist:
        raise Http404("NGO does not exist")
    return render(request, 'ngo/detail.html', {'name' : k})


def results(request, name):
    response = "You're looking at the results of ngo %s."
    print(response)
    return HttpResponse(response % name)


def ngo_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            ngo_name = form.cleaned_data["name"]
            reg_number = form.cleaned_data["registration_number"]
            category = form.cleaned_data["category"]
            address = form.cleaned_data["address"]
            contact_number = form.cleaned_data["contact_number"]
            email_address = form.cleaned_data["email_address"]
            website = form.cleaned_data["website"]
            ngo = Ngo(
                name=ngo_name,
                reg_number=reg_number,
                category=category,
                address=address,
                contact_number=contact_number,
                email_address=email_address,
                website=website,
            )
            ngo.save()
            template_data = {}
            template_data["alert_success"] = "NGO registration awating approval"
            return render(request, "index.html", template_data)
        else:
            template_data = {}
            template_data["errors"] = form.errors
            return HttpResponseRedirect("/ngo/signup")
    else:
        return render(request, "ngo_signup.html")