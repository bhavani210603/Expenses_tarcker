from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model  = Order
        fields = [
            'order_id', 'product_name', 'quantity', 'order_date',
            'meesho_amount', 'product_price', 'packing_cost',
            'platform_fees', 'bank_settlement',
            'delivery_status', 'payment_status', 'product_condition',
            'notes',
        ]
        widgets = {
            'order_date':        forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'notes':             forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'order_id':          forms.TextInput(attrs={'class': 'form-control'}),
            'product_name':      forms.TextInput(attrs={'class': 'form-control'}),
            'quantity':          forms.NumberInput(attrs={'class': 'form-control'}),
            'meesho_amount':     forms.NumberInput(attrs={'class': 'form-control'}),
            'product_price':     forms.NumberInput(attrs={'class': 'form-control'}),
            'packing_cost':      forms.NumberInput(attrs={'class': 'form-control'}),
            'platform_fees':     forms.NumberInput(attrs={'class': 'form-control'}),
            'bank_settlement':   forms.NumberInput(attrs={'class': 'form-control'}),
            'delivery_status':   forms.Select(attrs={'class': 'form-select'}),
            'payment_status':    forms.Select(attrs={'class': 'form-select'}),
            'product_condition': forms.Select(attrs={'class': 'form-select'}),
        }