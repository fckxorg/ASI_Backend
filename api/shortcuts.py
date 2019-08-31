"""Useful shortcuts for api.views module."""

import json
from django.core.serializers import serialize


def decode_json(request):
    """Use this method to decode json from request."""
    return json.loads(request.body.decode('utf-8'))


def serialize_pitches(pitches):
    """Use this method to serialize list of pitch objects."""
    pitches_data = {'pitches': []}
    pitch_fields = ['name', 'description', 'preview', 'tags']
    pitches = json.loads(serialize('json', pitches, fields=pitch_fields))
    for pitch in pitches:
        pitches_data['pitches'].append({**pitch['fields'], 'id': pitch['pk']})
    return pitches_data
