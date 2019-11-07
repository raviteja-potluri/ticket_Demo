from django import forms
from ticket.models import TicketDetails,NotesDetails,UserObjects
class TicketDetailsForm(forms.ModelForm):
    class Meta:
        model = TicketDetails
        fields = "__all__"
class UserObjects(forms.ModelForm):
    class Meta:
        model = UserObjects
        fields = "__all__"
class NotesDetails(forms.ModelForm):
    class Meta:
        model = NotesDetails
        fields = "__all__"
