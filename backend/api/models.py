from django.db import models
from django.contrib.auth.models import User

# User Profile Model
class UserProfile(models.Model):
    USER_TYPES = [
        ('lawyer', 'Lawyer'),
        ('accountant', 'Accountant'),
        ('business', 'Business'),
        ('other', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(choices=USER_TYPES, max_length=20, default='other')
    company_name = models.CharField(max_length=225, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

# Legal Document Model
class LegalDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Compliance Check Model
class ComplianceCheck(models.Model):
    document = models.ForeignKey(LegalDocument, on_delete=models.CASCADE)
    compliance_score = models.DecimalField(decimal_places=2, max_digits=5)
    risk_level = models.CharField(max_length=20)
    issues_found = models.TextField(blank=True, null=True)
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document.title

# Contract Risk Assessment Model
class ContractRiskAssessment(models.Model):
    document = models.ForeignKey(LegalDocument, on_delete=models.CASCADE)
    risk_score = models.DecimalField(decimal_places=2, max_digits=5)
    risk_level = models.CharField(max_length=20)
    key_risks = models.TextField(blank=True, null=True)
    assessed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document.title

# AI Generated Insights Model
class AIGeneratedInsights(models.Model):
    document = models.ForeignKey(LegalDocument, on_delete=models.CASCADE)
    insights = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document.title

# AI Generated Recommendations Model
class AIGeneratedRecommendations(models.Model):
    document = models.ForeignKey(LegalDocument, on_delete=models.CASCADE)
    recommendations = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document.title

# Tax Filing and Accounting Compliance Model
class TaxAccountingCompliance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.ForeignKey(LegalDocument, on_delete=models.CASCADE, blank=True, null=True)
    filing_status = models.CharField(max_length=20)
    issues_detected = models.TextField(blank=True, null=True)
    filled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Tax Compliance for {self.user.username}'

# Document Version Control Model
class DocumentVersion(models.Model):
    document = models.ForeignKey(LegalDocument, on_delete=models.CASCADE)
    version_number = models.IntegerField()
    changes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Version {self.version_number} of {self.document.title}'

# Notification Model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.user.username}'

