from rest_framework_mongoengine.serializers import DocumentSerializer
from rest_framework.serializers import ModelSerializer
from backend_test.trips.models import Trip
 
class DynamicFieldsModelSerializer(ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        fields = self.context['request'].query_params.get('fields')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class TripSerializer(DynamicFieldsModelSerializer, DocumentSerializer):
    """
    Serializer by trips documents
    """
    class Meta:
        model = Trip
        fields = '__all__'