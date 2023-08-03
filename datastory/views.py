from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404  # redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from datastory.forms import ArgumentForm, StrategyForm, MotivationForm, AttitudeForm, DatastoryForm, DimensionForm

from datastory.models import (
    Argument, Motivation, Attitude, Strategy, Datastory, Dimension
)

from datastory.utils import PageLinksMixin


# Create your views here.


class ArgumentList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Argument
    permission_required = 'datastory.view_argument'


class ArgumentDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Argument
    permission_required = 'datastory.view_argument'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        argument = self.get_object()
        strategy_list = argument.strategy.all()
        context['strategy_list'] = strategy_list
        return context


class ArgumentCreate(CreateView):
    form_class = ArgumentForm
    model = Argument
    permission_required = 'datastory.add_instructor'


class ArgumentUpdate(UpdateView):
    form_class = ArgumentForm
    model = Argument
    template_name = 'datastory/argument_form_update.html'
    permission_required = 'datastory.change_argument'


class ArgumentDelete(DeleteView):
    model = Argument
    success_url = reverse_lazy('datastory_argument_list_urlpattern')
    permission_required = 'datastory.delete_argument'

    def get(self, request, pk):
        argument = get_object_or_404(Argument, pk=pk)
        strategy = argument.strategy.all()
        if strategy.count() > 0:
            return render(
                request,
                'datastory/argument_refuse_delete.html',
                {'argument': argument,
                 'strategies': strategy,
                 }
            )
        else:
            return render(
                request,
                'datastory/argument_confirm_delete.html',
                {'argument': argument}
            )


class StrategyList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    model = Strategy
    permission_required = 'datastory.view_strategy'


class StrategyDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Strategy
    permission_required = 'datastory.view_strategy'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        strategy = self.get_object()
        argument = strategy.argument
        motivation = strategy.motivation
        attitude = strategy.attitude
        datastory_list = strategy.datastory.all()
        context['argument'] = argument
        context['motivation'] = motivation
        context['attitude'] = attitude
        context['datastory_list'] = datastory_list
        return context


class StrategyCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = StrategyForm
    model = Strategy
    permission_required = 'datastory.add_strategy'


class StrategyUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = StrategyForm
    model = Strategy
    template_name = 'datastory/strategy_form_update.html'
    permission_required = 'datastory.change_strategy'


class StrategyDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Strategy
    success_url = reverse_lazy('datastory_strategy_list_urlpattern')
    permission_required = 'datastory.delete_strategy'

    def get(self, request, pk):
        strategy = get_object_or_404(Strategy, pk=pk)
        datastory = strategy.datastory.all()
        if datastory.count() > 0:
            return render(
                request,
                'datastory/strategy_refuse_delete.html',
                {'strategy': strategy,
                 'datastory': datastory, }
            )
        else:
            return render(
                request,
                'datastory/strategy_confirm_delete.html',
                {'strategy': strategy}
            )


class MotivationList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    model = Motivation
    permission_required = 'datastory.view_motivation'


class MotivationDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Motivation
    permission_required = 'datastory.view_motivation'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        motivation = self.get_object()
        strategy_list = motivation.strategy.all()
        context['strategy_list'] = strategy_list
        return context


class MotivationCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = MotivationForm
    model = Motivation
    permission_required = 'datastory.add_motivation'


class MotivationUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = MotivationForm
    model = Motivation
    template_name = 'datastory/motivation_form_update.html'
    permission_required = 'datastory.change_motivation'


class MotivationDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Motivation
    success_url = reverse_lazy('datastory_motivation_list_urlpattern')
    permission_required = 'datastory.delete_motivation'

    def get(self, request, pk):
        motivation = get_object_or_404(Motivation, pk=pk)
        strategies = motivation.strategy.all()
        if strategies.count() > 0:
            return render(
                request,
                'datastory/motivation_refuse_delete.html',
                {'motivation': motivation,
                 'strategies': strategies,
                 }
            )
        else:
            return render(
                request,
                'datastory/motivation_confirm_delete.html',
                {'motivation': motivation}
            )


class AttitudeList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    model = Attitude
    permission_required = 'datastory.view_attitude'


class AttitudeDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Attitude
    permission_required = 'datastory.view_attitude'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        attitude = self.get_object()
        strategy_list = attitude.strategy.all()
        context['strategy_list'] = strategy_list
        return context


class AttitudeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = AttitudeForm
    model = Attitude
    permission_required = 'datastory.add_attitude'


class AttitudeUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = AttitudeForm
    model = Attitude
    template_name = 'datastory/attitude_form_update.html'
    permission_required = 'datastory.change_attitude'


class AttitudeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Attitude
    success_url = reverse_lazy('datastory_attitude_list_urlpattern')
    permission_required = 'datastory.delete_attitude'

    def get(self, request, pk):
        attitude = get_object_or_404(Attitude, pk=pk)
        strategy = attitude.strategy.all()
        if strategy.count() > 0:
            return render(
                request,
                'datastory/attitude_refuse_delete.html',
                {'attitude': attitude,
                 'strategy': strategy,
                 }
            )
        else:
            return render(
                request,
                'datastory/attitude_confirm_delete.html',
                {'attitude': attitude}
            )


class DimensionList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Dimension
    permission_required = 'datastory.view_dimension'


class DimensionDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Dimension
    permission_required = 'datastory.view_dimension'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        dimension = self.get_object()
        datastory_list = dimension.datastory.all()
        context['datastory_list'] = datastory_list
        return context


class DimensionCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = DimensionForm
    model = Dimension
    permission_required = 'datastory.add_dimension'


class DimensionUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = DimensionForm
    model = Dimension
    template_name = 'datastory/dimension_form_update.html'
    permission_required = 'datastory.change_dimension'


class DimensionDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Dimension
    success_url = reverse_lazy('datastory_dimension_list_urlpattern')
    permission_required = 'datastory.delete_dimension'

    def get(self, request, pk):
        dimension = get_object_or_404(Dimension, pk=pk)
        datastory = dimension.datastory.all()
        if datastory.count() > 0:
            return render(
                request,
                'datastory/dimension_refuse_delete.html',
                {'dimension': dimension,
                 'datastory': datastory, }
            )
        else:
            return render(
                request,
                'datastory/dimension_confirm_delete.html',
                {'dimension': dimension}
            )


class DatastoryList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    model = Datastory
    permission_required = 'datastory.view_datastory'


class DatastoryDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Datastory
    permission_required = 'datastory.view_datastory'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        datastory = self.get_object()
        dimension = datastory.dimension
        strategy = datastory.strategy
        context['dimension'] = dimension
        context['strategy'] = strategy
        return context


class DatastoryCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = DatastoryForm
    model = Datastory
    permission_required = 'datastory.add_datastory'


class DatastoryUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = DatastoryForm
    model = Datastory
    template_name = 'datastory/datastory_form_update.html'
    permission_required = 'datastory.change_datastory'


class DatastoryDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Datastory
    success_url = reverse_lazy('datastory_datastory_list_urlpattern')
    permission_required = 'datastory.delete_datastory'
