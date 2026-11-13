from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter

from .models import ShortURL


class ShortURLFilter(filters.FilterSet):
    status = filters.ChoiceFilter(
        choices=[("active", "Active"), ("expired", "Expired")],
        method="filter_status",
    )
    tag = filters.CharFilter(field_name="tags__name", lookup_expr="iexact", distinct=True)
    created_after = filters.IsoDateTimeFilter(field_name="created_at", lookup_expr="gte")
    created_before = filters.IsoDateTimeFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = ShortURL
        fields = ["is_active"]

    def filter_status(self, queryset, name, value):
        if value == "active":
            return queryset.active_urls()
        return queryset.expired_urls()


class StableOrderingFilter(OrderingFilter):
    def get_ordering(self, request, queryset, view):
        ordering = super().get_ordering(request, queryset, view)
        return [*ordering, "-id"] if ordering else ordering
