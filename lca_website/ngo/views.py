from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .forms import SignupForm
from .models import Ngo


def signup(request):
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
        return render(request, "ngo/signup.html")

class NgoListView(ListView):
    model = Ngo
    queryset = Ngo.objects.filter(Q(approved=True)).values("id", "name")
    context_object_name = "ngo_list"
    template_name = "ngo_list.html"


class NgoDetailView(DetailView):
    model = Ngo
    queryset = Ngo.objects.filter(Q(approved=True))
    template_name = "ngo/view.html"
