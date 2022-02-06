from django import forms


class DayForm(forms.Form):
    day = forms.IntegerField(label='Day: ', max_value=6, min_value=1)
