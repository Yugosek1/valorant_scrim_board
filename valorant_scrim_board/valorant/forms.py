from django import forms
from .models import Board, Rank
from django.utils import timezone

class ScrimModelForm(forms.ModelForm):
    start_at = forms.SplitDateTimeField(label = "対戦開始日時", widget=forms.SplitDateTimeWidget(date_attrs={"type":"date"}, time_attrs={"type":"time"}))
    class Meta:
        model = Board
        exclude = ["user", "updated_at", "created_at"]
        widgets = {
            'average_rank': forms.CheckboxSelectMultiple
        }

    # def __init__(self, user, *args, **kwargs):
    #     for field in self.base_fields.values():
    #         field.widget.attrs["class"] = "form-control"
    #     self.user = user
    #     super().__init__(*args, **kwargs)
    
    # 大事
    # __________________________________________________
    # def __init__(self, *args, **kwargs):
    #     for field in self.base_fields.values():
    #         field.widget.attrs["class"] = "form-control"
    #     super().__init__(*args, **kwargs)
    # __________________________________________________

    # # def save(self, commit=True):
    # #     valorant_obj = super().save(commit=False)
    # #     valorant_obj.user = self.user
    # #     if commit:
    # #         valorant_obj.save()
    # #     return valorant_obj