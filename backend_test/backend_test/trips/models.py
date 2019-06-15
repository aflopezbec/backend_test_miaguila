from mongoengine import Document, EmbeddedDocument, fields
 
class DateInput(EmbeddedDocument):
    date = fields.DateTimeField( null= True)
    pickup_address = fields.StringField()
    pickup_location = fields.PointField()

class CountryInput(EmbeddedDocument):
    name = fields.StringField()

class CityInput(EmbeddedDocument):
    name = fields.StringField()

class PersonInput(EmbeddedDocument):
    first_name = fields.StringField()
    last_name = fields.StringField()

class CarInput(EmbeddedDocument):
    plate = fields.StringField(max_length=6)
 
class Trip(Document):
    start = fields.EmbeddedDocumentField(DateInput)
    end = fields.EmbeddedDocumentField(DateInput)
    country = fields.EmbeddedDocumentField(CountryInput)
    city = fields.EmbeddedDocumentField(CityInput)
    passenger = fields.EmbeddedDocumentField(PersonInput)
    driver = fields.EmbeddedDocumentField(PersonInput)
    car = fields.EmbeddedDocumentField(CarInput)
    status = fields.StringField(choices = ['onWay','near','started'])
    check_code = fields.StringField()
    createdAt = fields.DateTimeField()
    updatedAt = fields.DateTimeField()
    price = fields.FloatField()
    driver_location = fields.PointField()

    meta = {'collection': 'trips'}