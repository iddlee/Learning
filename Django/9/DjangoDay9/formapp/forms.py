from django import forms

class MilkForm(forms.Form):
    name = forms.CharField(label="牛奶名称",max_length=5)
    price = forms.FloatField(label="牛奶价格",required=False)
