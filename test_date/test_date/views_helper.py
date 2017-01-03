import datetime
import unicodedata
import webbrowser
import time
import pytz

from django.shortcuts import render, redirect
from django.utils     import timezone
from django.utils.timezone import localtime

def uni_to_str(uni):
	"""
	Converts the given unicode string to a pythonic one.
	"""
	return unicodedata.normalize('NFKD', uni).encode('ascii','ignore')

def convert_to_utc(alarm_time):
	"""
	Takes naive alarm_time in local timezone format and converts to UTC aware alarm_time.
	"""
	local = timezone.get_current_timezone()
	local_dt = local.localize(alarm_time, is_dst=None)
	utc_dt = local_dt.astimezone(pytz.utc)
	return utc_dt