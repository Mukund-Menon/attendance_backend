from django.contrib import admin

from attendance.models import Attendee, Attendance

admin.site.register(Attendee)
admin.site.register(Attendance)
