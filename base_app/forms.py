from django import forms
from base_app.models import Vendor

PAYMENT_CHOICES = (
    ('F', 'Flutterwave'),
    ('D', 'Direct transfer')
)

class CheckoutForm(forms.Form):
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Address',  'class':'input'
    }))
    phone = forms.CharField(max_length = 13, widget=forms.TextInput(attrs = {
        'placeholder': 'Phone',  'class':'input'
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'City',  'class':'input'}))
    different_shipping_address = forms.BooleanField(widget=forms.CheckboxInput(attrs={'type':'checkbox', 'id':'shiping-address'}), required=False)
    order_notes = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Order Notes', 'class':'input'}), required=False)
    save_info = forms.BooleanField(widget=forms.CheckboxInput(attrs={'type':'checkbox', 'id':'save_info'}), required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
    terms  = forms.BooleanField(widget=forms.CheckboxInput(attrs={'type':'checkbox', 'id':'terms'}), required=True)

    #Deliver to different billing address

    address_diff = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Address',  'class':'input'
    }), required=False)
    phone_diff = forms.CharField(max_length = 11, widget=forms.TextInput(attrs = {
        'placeholder': 'Phone',  'class':'input'
    }), required=False)
    city_diff = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'City',  'class':'input'}), required=False)

#class VendorForm(forms.ModelForm):
    
    #class Meta:
        #model = Vendor
        
    
