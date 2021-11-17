from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Activity
from django.template import RequestContext
from django.http import HttpResponse, FileResponse
import csv
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter


def home(request):
    return render(request, 'Sales/home.html', {})

def activity(request):
    activity_list = Activity.objects.all()
    return render(request, 'Sales/activity.html', {'activity_list': activity_list,
                                                   })
def admin(request):
    return render(request, 'Sales/sadmin.html', {})

def companies(request):
    if request.method == "POST":
        companysearched = request.POST['companysearched']
        activitiesj = Activity.objects.filter(company__icontains=companysearched)
        return render(request, 'Sales/companies.html', {'companysearched': companysearched,
                                                   'activitiesj': activitiesj})
    else:
        activity_list = Activity.objects.all()
        return render(request, 'Sales/companies.html', {'activity_list': activity_list})



def importf(request):
    return render(request, 'Sales/importf.html', {})

def jobs(request):
    if request.method == "POST":
        jobsearched = request.POST['jobsearched']
        activitiesj = Activity.objects.filter(jobnumber__icontains=jobsearched)
        return render(request, 'Sales/jobs.html', {'jobsearched': jobsearched,
                                                   'activitiesj': activitiesj})
    else:
        activity_list = Activity.objects.all()
        return render(request, 'Sales/jobs.html', {'activity_list': activity_list})

def profile(request):
    return render(request, 'Sales/profile.html', {})

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched2 = request.POST['searched2']
        searched3 = request.POST['searched3']
        searched4 = request.POST['searched4']
        activities = Activity.objects.filter(jobnumber__icontains=searched)
        activities2 = Activity.objects.filter(company__icontains=searched2)
        activities3 = Activity.objects.filter(location__icontains=searched3)
        activities4 = Activity.objects.filter(refnumber__icontains=searched4)
        return render(request, 'Sales/search.html', {'searched':searched,
                                                     'searched2':searched2,
                                                     'searched3': searched3,
                                                     'searched4': searched4,
                                                     'activities':activities,
                                                     'activities2':activities2,
                                                     'activities3':activities3,
                                                     'activities4':activities4,})
    else:
        return render(request, 'Sales/search.html', {})

def statement(request):
    return render(request, 'Sales/statement.html', {})

def report(request):
    return render(request, 'Sales/report.html', {})

def venue_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venues.csv'

    writer = csv.writer(response)

    venues = Activity.objects.all()

    writer.writerow(['Job Number', 'Reference Number', 'Receiving Date', 'Company'])

    for venue in venues:
        writer.writerow([venue.jobnumber, venue.refnumber, venue.rdate, venue.company])
    return response

def venue_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    venues = Activity.objects.all()

    lines = []


    for venue in venues:
        lines.append("")
        lines.append("")
        lines.append(f'Job Number: {venue.jobnumber}')
        lines.append(f'Company: {venue.company}')
        refnumber_string = str(venue.refnumber)
        lines.append(f'Reference Number: {refnumber_string}')
        rdate_string = str(venue.rdate)
        lines.append(rdate_string)
        lines.append(venue.location)

    image = "Sales/static/images/small.jpg"
    c.drawImage(image, 10, 10, width=80, height=80)

    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='venue.pdf')


@csrf_protect
def login(request):
     csrfContext = RequestContext(request)
     return render('search.html', csrfContext)



