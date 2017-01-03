import datetime
import unicodedata
import webbrowser
import time
import pytz
import json

from django.shortcuts 			  import render, redirect
from django.core.serializers.json import DjangoJSONEncoder
from django.utils     			  import timezone
from django.utils.timezone 		  import localtime
from test_date.views_helper import *

# Sample date_and_time input: 02/01/2017 14:51:42

def test(request):
	if "alarm_time" in request.POST: # or "date_and_time" in request.GET:
		date_and_time = uni_to_str(request.POST.get("alarm_time", "HAHAH"))
		alarm_time = datetime.datetime.strptime(date_and_time, "%d/%m/%Y %H:%M:%S")
		alarm_time = convert_to_utc(alarm_time)
	return render(request, "test.html")