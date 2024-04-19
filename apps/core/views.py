from django.views.generic import (
    TemplateView
)


class IndexView(TemplateView):
    template_name = 'landing.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['doc_title'] = 'Home'
        return context
