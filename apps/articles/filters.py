import django_filters


class PubDateFilter(django_filters.FilterSet):
    month = django_filters.NumberFilter(
        field_name="pub_date", lookup_expr="month"
    )
    year = django_filters.NumberFilter(
        field_name="pub_date", lookup_expr="year"
    )
    o = django_filters.OrderingFilter(
        choices=(("pub_date", "Month"),),
        fields={
            "month": "pub_date",
        },
    )
