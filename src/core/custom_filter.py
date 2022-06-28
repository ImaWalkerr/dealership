from rest_framework.filters import SearchFilter


class CustomSearchFilter(SearchFilter):
    def filter_queryset(self, request, queryset, view):
        search_terms = self.get_search_terms(request)

        if not search_terms:
            return queryset.none()

        return super().filter_queryset(request, queryset, view)
