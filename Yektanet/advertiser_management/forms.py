from django import forms


class AdForm(forms.Form):
    title = forms.CharField(max_length=50)
    img_url = forms.URLField(max_length=100)
    link = forms.URLField(max_length=100)
    advertiser_id = forms.IntegerField()
