from django import forms

flows=('out' ,'in')
paytypes=('現金', '悠遊卡', '信用卡')


class Postform(forms.Form):
    # flow = forms.CharField(max_length=5, initial='out')
    flow = forms.CharField(widget=forms.RadioSelect)
    item = forms.CharField(max_length=20, initial='')
    amount = forms.IntegerField()
    paytype = forms.CharField(max_length=10, required=False, initial='現金')
    tags = forms.CharField(max_length=40, required=False, initial='')
    description = forms.CharField(widget=forms.Textarea)