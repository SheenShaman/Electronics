from django.views.generic import TemplateView


class MainView(TemplateView):

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)
        return context_data
