from django import forms
from .models import Mainapp 


class MainappForm(forms.ModelForm):
	class Meta:
		model = Mainapp
		fields = ['email'] 

	def clean_email(self):

		return self.cleaned_data.get('email')









# ------- END OF CODE ---------