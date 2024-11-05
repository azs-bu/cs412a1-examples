from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import Result

# Create your views here.

class ResultsListView(ListView):
    '''View to display list of marathon results.'''

    template_name = 'marathon_analytics/results.html'
    model = Result
    context_object_name = "results"
    paginate_by = 50

    def get_queryset(self) -> QuerySet[Any]:
        '''return the set of Results'''

        # use the superclass version of the queryset
        qs = super().get_queryset()
        # return qs[:25] # return 25 records for now

        # if we have a search paramter, use it to filter the query set
        if 'city' in self.request.GET:
            
            city = self.request.GET['city']
            if city: # not empty string:
                qs = Result.objects.filter(city__icontains=city)

        return qs
