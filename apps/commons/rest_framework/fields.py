from rest_framework.serializers import Field


class ChoicesDisplayField(Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super().__init__(**kwargs)

    def to_representation(self, obj):
        return {
            "value": self._choices[obj][0],
            "display": self._choices[obj][1]
        }
        return self._choices[obj]

    def to_internal_value(self, data):
        return getattr(self._choices, data)
