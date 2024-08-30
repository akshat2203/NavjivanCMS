from django import forms
from .models import ClientProfile, ClientDocument, ClientQualification


class ClientProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClientProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['address'].widget = forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
        self.fields['date_of_birth'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})

    class Meta:
        model = ClientProfile
        fields = [
            'surname',
            'first_name',
            'last_name',
            'fathers_name',
            'mothers_name',
            'date_of_birth',
            'gender',
            'marital_status',
            'cast',
            'mobile_number',
            'email',
            'address',
            'city',
            'taluka',
            'district',
            'pincode',
            'height',
            'weight',
            'chest',
            'edu_qualification',
            'photo',
            'signature'
        ]


class ClientDocumentForm(forms.ModelForm):
    class Meta:
        model = ClientDocument
        fields = '__all__'


class ClientQualificationForm(forms.ModelForm):
    class Meta:
        model = ClientQualification
        fields = '__all__'
