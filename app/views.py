from django.shortcuts import render
import datetime
# Create your views here.
def filters(request):
    date=datetime.datetime.now()
    d={'key':'I have 1 mango', 'dates':date, 'string':'This is my string', 'c':2}
    return render(request, 'filters.html',d)