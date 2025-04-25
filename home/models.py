from django.db import models

# Create your models here.

class Startup(models.Model):
    CATEGORY_CHOICES = [
        ('MEDTECH', 'MedTech'),
        ('DIAGNOSTICS', 'Diagnostics'),
        ('DRUG_DISCOVERY', 'Drug Discovery'),
        ('BIO_IT', 'Bio-IT'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')
    description = models.TextField(blank=True, null=True)
    founded_date = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
      

class FundingRound(models.Model):
    STAGE_CHOICES = [
        ('PRE_SEED', 'Pre-Seed'),
        ('SEED', 'Seed'),
        ('SERIES_A', 'Series A'),
        ('SERIES_B', 'Series B'),
        ('SERIES_C', 'Series C'),
        ('SERIES_D_PLUS', 'Series D+'),
        ('OTHER', 'Other'),
    ]

    # Link to the Startup model
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name='funding_rounds')
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES)
    amount = models.DecimalField(max_digits=15, decimal_places=2, help_text="Funding amount in USD") # Use DecimalField for money
    funding_date = models.DateField()
    investors = models.TextField(blank=True, null=True, help_text="Comma-separated list of main investors")

    class Meta:
        # Optional: Order rounds by date by default
        ordering = ['-funding_date']

    def __str__(self):
        return f"{self.startup.name} - {self.get_stage_display()} - {self.funding_date}"
