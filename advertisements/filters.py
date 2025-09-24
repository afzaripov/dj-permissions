from django_filters import rest_framework as filters

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    creator = filters.NumberFilter(field_name="creator__id")
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)
    created_at = filters.DateFromToRangeFilter(field_name="created_at")

    class Meta:
        model = Advertisement
        fields = ["creator", "status"]