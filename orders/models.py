from django.db import models

class Order(models.Model):

    DELIVERY_CHOICES = [
        ('pending',   'Pending'),
        ('shipped',   'Shipped'),
        ('delivered', 'Delivered'),
        ('returned',  'Returned'),
        ('cancelled', 'Cancelled'),
    ]

    PAYMENT_CHOICES = [
        ('awaiting',    'Awaiting'),
        ('transferred', 'Transferred to Bank'),
    ]

    CONDITION_CHOICES = [
        ('new',      'New'),
        ('good',     'Good'),
        ('damaged',  'Damaged'),
        ('returned', 'Returned Damaged'),
    ]

    # --- Order Info ---
    order_id         = models.CharField(max_length=100, unique=True)
    product_name     = models.CharField(max_length=200)
    quantity         = models.IntegerField(default=1)
    order_date       = models.DateField()

    # --- Money Fields ---
    meesho_amount    = models.DecimalField(max_digits=8, decimal_places=2, help_text="Price customer paid on Meesho")
    product_price    = models.DecimalField(max_digits=8, decimal_places=2, help_text="Your actual product cost")
    packing_cost     = models.DecimalField(max_digits=8, decimal_places=2, default=0, help_text="Packing/packaging cost")
    platform_fees    = models.DecimalField(max_digits=8, decimal_places=2, default=0, help_text="Meesho commission/fees")
    bank_settlement  = models.DecimalField(max_digits=8, decimal_places=2, default=0, help_text="Amount actually received in bank")

    # --- Auto Calculated Fields ---
    total_cost       = models.DecimalField(max_digits=8, decimal_places=2, default=0, help_text="product_price + packing_cost + platform_fees")
    profit           = models.DecimalField(max_digits=8, decimal_places=2, default=0, help_text="bank_settlement - total_cost")

    # --- Status Fields ---
    delivery_status  = models.CharField(max_length=20, choices=DELIVERY_CHOICES, default='pending')
    payment_status   = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='awaiting')
    product_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='new')

    notes            = models.TextField(blank=True)
    created_at       = models.DateTimeField(auto_now_add=True)

    # --- Auto calculate total_cost and profit before saving ---
    def save(self, *args, **kwargs):
        self.total_cost = self.product_price + self.packing_cost + self.platform_fees
        self.profit     = self.bank_settlement - self.total_cost
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order_id} - {self.product_name}"