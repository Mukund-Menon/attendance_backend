from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Attendee, Attendance
from .serializers import AttendeeSerializer, AttendanceSerializer

class TrackAttendanceView(APIView):
    serializer_class = AttendeeSerializer
    def post(self, request, *args, **kwargs):
        uuid = request.data.get('uuid')
        if not uuid:
            return Response({"error": "UUID is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            attendee = Attendee.objects.get(uuid=uuid)
        except Attendee.DoesNotExist:
            return Response({"error": "Attendee not found."}, status=status.HTTP_404_NOT_FOUND)
        
        attendance = Attendance.objects.create(attendee=attendee)
        attendee_data = AttendeeSerializer(attendee).data
        return Response(attendee_data, status=status.HTTP_200_OK)
