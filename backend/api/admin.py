from django.contrib import admin
from .models import (
    UserProfile, LegalDocument, ComplianceCheck,
    ContractRiskAssessment, AIGeneratedInsights,
    AIGeneratedRecommendations, TaxAccountingCompliance,
    DocumentVersion, Notification
)

# Register Models
admin.site.register(UserProfile)
admin.site.register(LegalDocument)
admin.site.register(ComplianceCheck)
admin.site.register(ContractRiskAssessment)
admin.site.register(AIGeneratedInsights)
admin.site.register(AIGeneratedRecommendations)
admin.site.register(TaxAccountingCompliance)
admin.site.register(DocumentVersion)
admin.site.register(Notification)

