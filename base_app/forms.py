from django import forms

PAYMENT_CHOICES = {
    ('F', 'Flutterwave'),
    ('D', 'Direct transfer')
}

class CheckoutForm(forms.Form):
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Address'
    }))
    zip_code = forms.CharField()
    different_billing_address = forms.BooleanField(widget=forms.CheckboxInput())
    save_info = forms.BooleanField(widget=forms.CheckboxInput())
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(), choices=PAYMENT_CHOICES)