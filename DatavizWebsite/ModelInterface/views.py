
from django.template import loader
from django.shortcuts import render, redirect

from django.http import HttpResponse, Http404
from .models import Record, Data
from .forms import RecordForm
import pickle
import pandas as pd


def index(request):
    return render(request, 'ModelInterface/index.html', {})

def select(request):
    values = [{"name": "1st year", "url":"year/1" },
              {"name":"2snd year", "url":"year/2" },
              {"name":"3rd year", "url":"year/3" },
              {"name":"4th year", "url":"year/4" },
              {"name":"5th year", "url":"year/5" },]
    return render(request, 'ModelInterface/yearselection.html', {"values":values})

# Create your views here.
def submit(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save()
            record.Predict()
            return redirect("result", submission_id=record.pk)
    else:
        form = RecordForm()
    return render(request, 'ModelInterface/form.html', {"form": form})

def result(request, submission_id):
    try:
        context = {}
        record = Record.objects.get(pk=submission_id)
        context.update({"title": "Here is your result"})
        context.update({"text": "Note that this result is purely indicative, it only attests of a trend and provides no guaranty\n"})
        context.update({"tab": [[0, record.GetValues()]]})
        context.update({"columns": record.GetHeader()})
    except:
        raise Http404("This submission doesn't exists")
    return render(request, "ModelInterface/tabledisplay.html", context)

def year(request, year_id):
    if(year_id<1 or year_id>5):
        raise Http404("This year doesn't exists")
    else:
        context = {}
        context.update({"title": ""})
        context.update({"text": "Note that this result is purely indicative, it only attests of a trend and provides no guaranty\n"})
        objects = Data.objects.filter(Year=year_id)
        context.update({"tab": [[i,[objects[i].X1,objects[i].X2,objects[i].X3,objects[i].X4,objects[i].X5,objects[i].X6,objects[i].X7,objects[i].X8,objects[i].X9,objects[i].X10,objects[i].X11,objects[i].X12,objects[i].Class]] for i in range(len(objects))]})
        context.update({"columns": ["X{}".format(i+1) for i in range(12)]+["Bankruptcy"]})

    return render(request, "ModelInterface/tabledisplay.html", context)

def summary(request):
    records = Record.objects.all()
    tab = [[i,records[i].GetValues()] for i in range(len(records))]
    context = {}
    context.update({"title": "Results provided by our models"})
    context.update({"text": "Note that we do not ask you enough variables, so we never get bankruptcy predictions we've added some to show you how they are represented"})
    context.update({"tab": tab})
    context.update({"columns": records[0].GetHeader()})
    return render(request, "ModelInterface/tabledisplay.html", context)

def loaddata(request):
    if request.user.is_superuser:
        for i in range(5):
            model = pickle.load(open("saves/data{}.save".format(i+1), "rb"))
            model["bankruptcy"]=model["bankruptcy"].astype(int)
            model["bankruptcy"] = model["bankruptcy"].astype(str)
            serie=model["bankruptcy"].map({"0":"No bankruptcy","1":"bankruptcy"})
            model["Class"]=serie
            model = model.drop("bankruptcy", axis=1)
            values = model.to_dict('r')
            for dict in values:
                dict.update({"Year":i+1})
                data = Data(**dict)
                data.save()
    return redirect("index")

def team(request):
    return render(request, "ModelInterface/team.html", {})

def ipynb(request):
    return render(request, "ModelInterface/ipynb.html", {})




