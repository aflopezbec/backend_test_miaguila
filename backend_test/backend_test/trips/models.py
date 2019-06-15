from mongoengine import Document, EmbeddedDocument, fields
from django.core.exceptions import ValidationError
 
class DateInput(EmbeddedDocument):
    date = fields.DateTimeField()
    pickup_address = fields.StringField()
    pickup_location = fields.PointField()

class CountryInput(EmbeddedDocument):
    name = fields.StringField(required=True)

class CityInput(EmbeddedDocument):
    name = fields.StringField(required=True)

class PersonInput(EmbeddedDocument):
    first_name = fields.StringField(required=True)
    last_name = fields.StringField(required=True)

class CarInput(EmbeddedDocument):
    plate = fields.StringField(max_length=6, required=True)
 
class Trip(Document):
    start = fields.EmbeddedDocumentField(DateInput)
    end = fields.EmbeddedDocumentField(DateInput)
    country = fields.EmbeddedDocumentField(CountryInput)
    city = fields.EmbeddedDocumentField(CityInput)
    passenger = fields.EmbeddedDocumentField(PersonInput, required=True)
    driver = fields.EmbeddedDocumentField(PersonInput, required=True)
    car = fields.EmbeddedDocumentField(CarInput, required=True)
    status = fields.StringField(choices = ['onWay','near','started'])
    check_code = fields.StringField()
    createdAt = fields.DateTimeField(required=True)
    updatedAt = fields.DateTimeField(required=True)
    price = fields.FloatField()
    driver_location = fields.PointField()

    meta = {'collection': 'trips'}

    def clean(self):
        """Ensures that only published essays have a `pub_date` and
        automatically sets `pub_date` if essay is published and `pub_date`
        is not set"""
        if self.updatedAt or self.createdAt or self.driver or self.passenger:
            msg = 'updatedAt, createdAt, driver, passenger can not be null'
            raise ValidationError(msg)