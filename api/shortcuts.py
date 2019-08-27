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


def generate_response(status_code):
    """Use this method to generate server response with status code."""
    if status_code[0] == '0':
        return {'status': 'Ok'}
    if status_code[0] == '1':
        if status_code[1] == '0':
            return {'status': 'Error', 'message': 'Not allowed'}
        if status_code[1] == '1':
            return {'status': 'Error', 'message': 'Wrong credentials'}
