from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.postgres.fields import ArrayField

grantor_model = models.CharField(max_length=32767, null=True)
grantee_model = models.CharField(max_length=32767, null=True)
book_model = models.CharField(max_length=4, null=True)
page_model = models.CharField(max_length=4, null=True)
book_model = models.CharField(max_length=4, null=True)
reception_number_model = models.CharField(max_length=20, null=True)
document_type_model = models.CharField(max_length=32767, null=True)
recording_date_model = models.CharField(max_length=10, null=True)
legal_model = models.CharField(max_length=32767, null=True)
related_model = models.CharField(max_length=32767, null=True)
comment_model = models.CharField(max_length=32767, null=True)

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username

class Document(models.Model):
    # county = models.CharField(max_length=20, null=True)
    grantor = grantor_model
    grantee = grantee_model
    book = book_model
    page = page_model
    reception_number = reception_number_model
    document_type = document_type_model
    # document_date = models.CharField(null=True)
    recording_date = recording_date_model
    legal = legal_model
    related = related_model
    comment = comment_model

    def __str__(self):
        return f'{self.reception_number}'
        # return f'{self.county}-{self.reception_number}'


class Abstraction(models.Model):
    # counties = ArrayField(Document.county)
    grantors = ArrayField(grantor_model)
    grantees = ArrayField(grantee_model)
    books = ArrayField(book_model)
    pages = ArrayField(page_model)
    reception_numbers = ArrayField(reception_number_model)
    document_types = ArrayField(document_type_model)
    recording_dates = ArrayField(recording_date_model)
    legals = ArrayField(legal_model)
    related_documents = ArrayField(related_model)
    comments = ArrayField(comment_model)

    def __str__(self):
        return f'{self.id}: {len(self.grantors)} documents'
