from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import Contacts, Interactions
from collections import OrderedDict

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'email',
            'groups',
        ]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [
            'url',
            'name',
        ]


class ChoicesField(serializers.Field):
    """
    https://stackoverflow.com/a/37481202
    """
    def __init__(self, choices, **kwargs):
        self._choices = OrderedDict(choices)
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        for i in self._choices:
            if self._choices[i] == data:
                return i
        raise serializers.ValidationError("Acceptable values are {0}.".format(list(self._choices.values())))


class InteractionSerializer(serializers.HyperlinkedModelSerializer):
    action = ChoicesField(choices=Interactions.action_choices)

    class Meta:
        model = Interactions
        fields = [
            'url',
            'action',
            'notes',
            'created_at',
            'contact',
        ]

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    interactions = InteractionSerializer(many=True, read_only=True)

    class Meta:
        model = Contacts
        fields = [
            'url',
            'name',
            'phone_number',
            'website',
            'address',
            'employees',
            'notes',
            'interactions',
        ]
