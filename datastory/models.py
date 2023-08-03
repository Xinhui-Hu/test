from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse


class Argument(models.Model):
    argument_id = models.AutoField(primary_key=True)
    argument = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return "Argument: %s" % self.argument

    def get_absolute_url(self):
        return reverse('datastory_argument_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('datastory_argument_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('datastory_argument_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['argument_id']
        constraints = [
            UniqueConstraint(fields=['argument'], name='unique_argument')
        ]


class Motivation(models.Model):
    motivation_id = models.AutoField(primary_key=True)
    motivation = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return "Motivation: %s" % self.motivation

    def get_absolute_url(self):
        return reverse('datastory_motivation_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('datastory_motivation_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('datastory_motivation_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['motivation_id']
        constraints = [
            UniqueConstraint(fields=['motivation'], name='unique_motivation')
        ]


class Attitude(models.Model):
    attitude_id = models.AutoField(primary_key=True)
    attitude = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return "%s" % self.attitude

    def get_absolute_url(self):
        return reverse('datastory_attitude_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('datastory_attitude_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('datastory_attitude_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['attitude_id']
        constraints = [
            UniqueConstraint(fields=['attitude'], name='unique_attitude')
        ]


class Strategy(models.Model):
    strategy_id = models.AutoField(primary_key=True)
    argument = models.ForeignKey(Argument, related_name='strategy', on_delete=models.PROTECT)
    motivation = models.ForeignKey(Motivation, related_name='strategy', on_delete=models.PROTECT)
    attitude = models.ForeignKey(Attitude, related_name='strategy', on_delete=models.PROTECT)
    strategy_name = models.CharField(max_length=20)

    def __str__(self):
        # return "Recommended Strategy: %s" % self.strategy_name
        # return '%s' % self.strategy_name
        return '%s(%s+%s+%s)' % (self.strategy_name, self.argument, self.motivation, self.attitude)

    def get_absolute_url(self):
        return reverse('datastory_strategy_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('datastory_strategy_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse(
            'datastory_strategy_delete_urlpattern',
            kwargs={'pk': self.pk}
        )

    class Meta:
        ordering = ['strategy_name']
        constraints = [
            UniqueConstraint(fields=['argument', 'motivation', "attitude"], name='unique_strategy')
        ]


class Dimension(models.Model):  # Data dimension
    dimension_id = models.AutoField(primary_key=True)
    dimension_name = models.CharField(max_length=45)

    def __str__(self):
        return "%s" % self.dimension_name

    def get_absolute_url(self):
        return reverse('datastory_dimension_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('datastory_dimension_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('datastory_dimension_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['dimension_name']
        constraints = [
            UniqueConstraint(fields=['dimension_name'], name='unique_dimension')
        ]


class Datastory(models.Model):
    story_id = models.AutoField(primary_key=True)
    story_content = models.CharField(max_length=600)
    strategy = models.ForeignKey(Strategy, related_name='datastory', on_delete=models.PROTECT)
    dimension = models.ForeignKey(Dimension, related_name='datastory', on_delete=models.PROTECT)

    def __str__(self):
        return "%s: %s" % (self.dimension, self.story_content)

    def get_absolute_url(self):
        return reverse('datastory_datastory_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('datastory_datastory_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('datastory_datastory_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['dimension']
