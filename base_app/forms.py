from django import forms
from base_app.models import Vendor, Item, Review
from django.contrib.auth.models import User

PAYMENT_CHOICES = (
    ('F', 'Flutterwave'),
    ('D', 'Direct transfer')
)

CATEGORY_CHOICES = (
    ('MF', 'Men\'s Fashion'),
    ('WF', 'Women\'s Fashion'),
    ('CJ', 'Clothing and Jewelry'),
    ('FO', 'Food'),
    ('WD', 'Web & Mobile Development'),
    ('ED', 'Electronics and Devices'),
    ('AS', 'Art and Stationary')
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

class VendorForm(forms.ModelForm):

    password_verification = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password Verification',  'class':'input'}))
    class Meta():
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password')
        widgets = {
        'password' : forms.PasswordInput(attrs={'placeholder':'Password',  'class':'input'}),
        'username' : forms.TextInput(attrs={'placeholder':'Username',  'class':'input'}),
        'first_name' : forms.TextInput(attrs={'placeholder': 'First Name',  'class':'input'}),
        'last_name' : forms.TextInput(attrs={'placeholder': 'Last Name',  'class':'input'}),
        'email' : forms.TextInput(attrs={'placeholder': 'Shop Email Address',  'class':'input'}),
    }

class ItemForm(forms.ModelForm):
    class Meta():
        model = Item
        fields = ('title', 'price', 'discount_price', 'category', 'label', 'slug', 'description', 'image', 'image_1', 'image_2', 'image_3', 'vendor')
        

class VendorDetailForm(forms.ModelForm):

    terms  = forms.BooleanField(widget=forms.CheckboxInput(attrs={'type':'checkbox', 'id':'terms'}), required=True)
    store_category = forms.ChoiceField(choices = CATEGORY_CHOICES, widget=forms.Select(attrs={'placeholder':'Shop Category',  'class':'input'}))
    class Meta():
        model  = Vendor
        fields = ('store_category', 'city', 'phone_number', 'shop_name')
        widgets = {
            'shop_name' : forms.TextInput(attrs={'placeholder':'Shop Name',  'class':'input'}),
            'phone_number' : forms.TextInput(attrs={'placeholder':'Phone Number',  'class':'input'}),
            'city' : forms.TextInput(attrs={'placeholder':'City',  'class':'input'}),
        }

class ReviewForm(forms.Form):
    class Meta():
        model = Review
        fields =('review')
        widgets = {
            'review' : forms.TextInput(attrs={'placeholder':'Your Review',  'class':'input'}),
        }

        
    
