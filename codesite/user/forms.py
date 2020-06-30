from django import forms
from codesite.models import Savings,Loan

class FormSavings(forms.Form):
    CHOICES_SCHEME = [('Biweekly : Tuesday - Friday', 'Biweekly : Tuesday - Friday'), ('Weekly : Friday', 'Weekly : Friday')]
    CHOICES_DURATION = [('1 Week', '1 Week'), ('2 Weeks', '2 Weeks'),
                        ('3 Week', '3 Week'), ('1 Month', '1 Month'),
                        ('2 Months', '2 Months'), ('3 Months', '3 Months'),
                        ('4 Months', '4 Months'), ('5 Months', '5 Months') ]

    amount   =  forms.CharField(help_text='Amount',widget=forms.TextInput(attrs={'onkeypress':'return (event.charCode !=8 && event.charCode ==0 ||  ((event.charCode >= 48 && event.charCode <= 57) && (event.charCode !=190 ) )) ', 'label':'Pls. makeyour input in decimal form.' }))
    interest =  forms.CharField(help_text='Interest',widget=forms.TextInput(attrs={'pattern':'[0-9]+', 'label':'Pls. makeyour input in decimal form.' }))
    scheme_field = forms.ChoiceField(help_text='Scheme',widget=forms.Select, choices=CHOICES_SCHEME)
    duration =   forms.ChoiceField(help_text='Duration',widget=forms.Select, choices=CHOICES_DURATION)
    duedate = forms.DateField(label='duedate',help_text='Duration',widget=forms.TextInput)




    def clean_amount(self):
        data = self.cleaned_data['amount']
        if len( data ) > 12:
            raise forms.ValidationError("The input only accept smaller length of money value.")

        try:
            oknum = float(data)           # ValueError if cannot be converted
        except ValueError:
            raise forms.ValidationError("Pls. makeyour input in decimal form.")
        return data

class FormLoans(forms.ModelForm):

    class Meta:
        model = Loan
        fields = ( 'memberid','total_amount', 'installment_amount','interest','scheme', 'duration' ,'duedate' )

        def clean_total_amount(self):
            data = self.cleaned_data['total_amount']
            if len( data ) > 12:
                raise forms.ValidationError("The input only accept smaller length of money value.")

            try:
                oknum = float(data)           # ValueError if cannot be converted
            except ValueError:
                raise forms.ValidationError("Pls. makeyour input in decimal form.")
            return data
        def clean_interest(self):
            data = self.cleaned_data['interest']
            if len( data ) > 12:
                raise forms.ValidationError("The input only accept smaller length of money value.")

            try:
                oknum = float(data)           # ValueError if cannot be converted
            except ValueError:
                raise forms.ValidationError("Pls. makeyour input in decimal form.")
            return data
