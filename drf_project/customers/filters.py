import django_filters
from .models import Customer

class CustomerFilter(django_filters.FilterSet):
    age = django_filters.CharFilter(field_name= 'age', lookup_expr='iexact')
    cname= django_filters.CharFilter(field_name= 'cname', lookup_expr='icontains')
    #cid = django_filters.RangeFilter(field_name= 'cid')  #From id to id (works for int only)
    id_min = django_filters.CharFilter(method = 'filter_by_id_range', label = 'FROM CUST ID')
    id_max = django_filters.CharFilter(method = 'filter_by_id_range', label = 'TO CUST ID')
    class Meta:
        model = Customer
        fields = ['age','cname', 'id_min', 'id_max']

    def filter_by_id_range(self, queryset, name, value):
        if  name == 'id_min':
            return queryset.filter(cid__gte=value)
        elif name == 'id_max':
            return queryset.filter(cid__lte=value)
        return queryset