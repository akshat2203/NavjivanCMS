import os
from uuid import uuid4
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
NULL_AND_BLANK = {"null": True, "blank": True}


class ClientProfile(models.Model):

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]

    MARITAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
        ('separated', 'Separated'),
    ]

    CAST_CHOICES = [
        ('sc', 'SC'),
        ('st', 'ST'),
        ('obc', 'OBC'),
        ('ews', 'EWS'),
        ('general', 'GENERAL'),
    ]

    # Personal Information
    unique_number = models.CharField(max_length=20, unique=True, **NULL_AND_BLANK)
    surname = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    fathers_name = models.CharField(max_length=50)
    mothers_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)
    cast = models.CharField(max_length=10, choices=CAST_CHOICES)

    # Contact Information
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    taluka = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    pincode = models.IntegerField()

    # Physical Attributes
    height = models.IntegerField(validators=[MinValueValidator(1)], **NULL_AND_BLANK)
    weight = models.IntegerField(validators=[MinValueValidator(1)], **NULL_AND_BLANK)
    chest = models.IntegerField(validators=[MinValueValidator(1)], **NULL_AND_BLANK)

    # Education Qualification
    edu_qualification = models.CharField(max_length=50)

    # Photo and Signature
    photo = models.ImageField(upload_to="Photos-Signature/")
    signature = models.ImageField(upload_to="Photos-Signature/")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ClientDocument(models.Model):
    client = models.OneToOneField(ClientProfile, on_delete=models.CASCADE, related_name='documents')

    # Caste Certificate
    cast_certificate_number = models.CharField(max_length=20)
    cast_certificate_date = models.DateField()
    cast_certificate_img = models.FileField(upload_to="Documents/")

    # OBC Certificate
    obc_certificate_number = models.CharField(max_length=20)
    obc_certificate_date = models.DateField()
    obc_certificate_provider = models.CharField(max_length=20)
    obc_certificate_img = models.FileField(upload_to="Documents/")

    # Aadhar Card
    aadhar_card_number = models.CharField(max_length=20)
    aadhar_card_img = models.FileField(upload_to="Documents/")

    def __str__(self):
        return f"Documents for {self.client.first_name} {self.client.last_name}"


class ClientQualification(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE, related_name='qualifications')

    # Education Qualification Details
    degree = models.CharField(max_length=100)
    percentage = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    board = models.CharField(max_length=50)
    passing_year = models.IntegerField(validators=[MinValueValidator(1900)])
    attempt = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])
    marksheet = models.FileField(upload_to="Marksheets/")

    def __str__(self):
        return f"{self.degree} ({self.passing_year}) - {self.client.first_name} {self.client.last_name}"



# def document_upload_path(instance, filename):
#     """Generate file upload path."""
#     ext = filename.split('.')[-1]
#     filename = f"{uuid4().hex}.{ext}"
#     return os.path.join("documents", str(instance.client.id), filename)
#
# def photo_upload_path(instance, filename):
#     """Generate photo upload path."""
#     ext = filename.split('.')[-1]
#     filename = f"{uuid4().hex}.{ext}"
#     return os.path.join("photos", str(instance.client.id), filename)