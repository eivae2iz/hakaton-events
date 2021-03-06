from rest_framework import serializers
from datetime import datetime

from event.models import Event


class GetEventsSerializer(serializers.Serializer):
    sort_by = serializers.CharField(max_length=1, help_text='t=time, m=members', required=False, default='t')
    query_string = serializers.CharField(max_length=100, help_text="Query string", default='')
    lat_ne = serializers.FloatField(help_text="Latitude of the north east", default=60)
    lng_ne = serializers.FloatField(help_text="Longitude of the north east", default=40)
    lat_sw = serializers.FloatField(help_text="Latitude of the south west", default=50)
    lng_sw = serializers.FloatField(help_text="Longitude of the south west", default=30)
    start_date = serializers.DateTimeField(help_text="Start date of event", required=False)
    end_date = serializers.DateTimeField(help_text="End date of event", required=False)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'lat', 'lng', 'start_date', 'end_date',
                  'photo', 'ext_id', 'title', 'external_url', )
        #exclude = ( "id",)


class GetEventSerializer(serializers.Serializer):
    ext_id = serializers.CharField()


class EventFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ( )


class EventsSerializer(serializers.Serializer):
    events = EventSerializer(many=True)
