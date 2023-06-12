from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView, RedirectView


class Home(RedirectView):
    # url = '/'
    pattern_name = 'modhome'





# class Home(TemplateView):
#     template_name='school/home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['name'] = 'Santosh kumar mehra'
#         print(kwargs)
#         return context


