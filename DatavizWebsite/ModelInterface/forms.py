from django import forms
from ModelInterface.models import Record
from django.forms import ModelForm

class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ['profit_on_operating_activities',
        'financial_expenses',
        'sales_of_the_year',
        'sales_of_the_previous_year',
        'operating_expenses',
        'total_liabilities',
        'current_assets',
        'inventory',
        'short_term_liabilities',
        'total_assets',
        'profit_on_sales' ,
        'year']
