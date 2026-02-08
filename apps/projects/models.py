from django.db import models

from apps.lookups.models import (
    PriorityLevel,
    ProjectType,
    BudgetSource,
    FiscalYear,
    RoadType,
)
from apps.locations.models import Location
from apps.engineers.models import Engineer
from apps.chairpersons.models import Chairperson
from apps.contractors.models import Contractor

class Project(models.Model):
    """
    Core project entity.
    """
    STATUS_CHOICES = (
        ("ONGOING", "Ongoing"),
        ("DELAYED", "Delayed"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    )

    project_code = models.CharField(max_length=50, unique=True)
    project_name = models.CharField(max_length=250)

    priority = models.ForeignKey(
        PriorityLevel,
        on_delete=models.PROTECT,
        related_name="projects"
    )

    project_type = models.ForeignKey(
        ProjectType,
        on_delete=models.PROTECT,
        related_name="projects"
    )

    ward_no = models.PositiveIntegerField(default=16)
    municipality = models.CharField(max_length=100, default="Kathmandu")
    district = models.CharField(max_length=100, default="Kathmandu")
    province = models.CharField(max_length=100, default="Bagmati")

    location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        related_name="projects"
    )

    total_approved_budget = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True
    )

    budget_source = models.ForeignKey(
        BudgetSource,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    fiscal_year = models.ForeignKey(
        FiscalYear,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    assigned_engineer = models.ForeignKey(
        Engineer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    chairperson = models.ForeignKey(
        Chairperson,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    contractor = models.ForeignKey(
        Contractor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    proposed_date = models.DateField(null=True, blank=True)
    approved_date = models.DateField(null=True, blank=True)
    planned_start_date = models.DateField(null=True, blank=True)
    planned_completion_date = models.DateField(null=True, blank=True)
    planned_duration_days = models.PositiveIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="Ongoing"
    )

    class Meta:
        db_table = "projects"
        ordering = ["-created_at"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return f"{self.project_code} – {self.project_name}"
