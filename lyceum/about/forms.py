from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        # validators=[start_with_a],
    )
    email = forms.EmailField(
        label='Mail',
        max_length=100,
    )
