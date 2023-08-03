from django import forms

from datastory.models import Argument, Motivation, Attitude, Strategy, Datastory, Dimension


class ArgumentForm(forms.ModelForm):
    class Meta:
        model = Argument
        fields = '__all__'

    def clean_argument(self):
        return self.cleaned_data['argument'].strip()  # remove white space


class MotivationForm(forms.ModelForm):
    class Meta:
        model = Motivation
        fields = '__all__'

    def clean_motivation(self):
        return self.cleaned_data['motivation'].strip()  # remove white space


class AttitudeForm(forms.ModelForm):
    class Meta:
        model = Attitude
        fields = '__all__'

    def clean_attitude(self):
        return self.cleaned_data['attitude'].strip()  # remove white space


class StrategyForm(forms.ModelForm):
    class Meta:
        model = Strategy
        fields = '__all__'


class DatastoryForm(forms.ModelForm):
    class Meta:
        model = Datastory
        fields = '__all__'


class DimensionForm(forms.ModelForm):
    class Meta:
        model = Dimension
        fields = '__all__'

    def clean_dimension_name(self):
        return self.cleaned_data['dimension_name'].strip()
