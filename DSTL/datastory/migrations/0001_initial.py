# Generated by Django 4.2.1 on 2023-07-10 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Argument',
            fields=[
                ('argument_id', models.AutoField(primary_key=True, serialize=False)),
                ('argument', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attitude',
            fields=[
                ('attitude_id', models.AutoField(primary_key=True, serialize=False)),
                ('attitude', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Datastory',
            fields=[
                ('story_id', models.AutoField(primary_key=True, serialize=False)),
                ('story_content', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('dimension_id', models.AutoField(primary_key=True, serialize=False)),
                ('dimension_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Motivation',
            fields=[
                ('motivation_id', models.AutoField(primary_key=True, serialize=False)),
                ('motivation', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Viz',
            fields=[
                ('viz_id', models.AutoField(primary_key=True, serialize=False)),
                ('viz_type_name', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('strategy_id', models.AutoField(primary_key=True, serialize=False)),
                ('strategy_name', models.CharField(max_length=20)),
                ('argument', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='strategy', to='datastory.argument')),
                ('attitude', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='strategy', to='datastory.attitude')),
                ('motivation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='strategy', to='datastory.motivation')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('upload_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=45, unique=True)),
                ('file_path', models.FilePathField()),
                ('dimension', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='file', to='datastory.dimension')),
            ],
        ),
        migrations.CreateModel(
            name='DimTag',
            fields=[
                ('dimtag_id', models.AutoField(primary_key=True, serialize=False)),
                ('dimension', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dimtag', to='datastory.dimension')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dimtag', to='datastory.tag')),
            ],
        ),
        migrations.CreateModel(
            name='DataViz',
            fields=[
                ('dataviz_id', models.AutoField(primary_key=True, serialize=False)),
                ('datastory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dataviz', to='datastory.datastory')),
                ('viz', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dataviz', to='datastory.viz')),
            ],
        ),
        migrations.AddField(
            model_name='datastory',
            name='dimension',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='datastory', to='datastory.dimension'),
        ),
        migrations.AddField(
            model_name='datastory',
            name='strategy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='datastory', to='datastory.strategy'),
        ),
        migrations.AddField(
            model_name='datastory',
            name='viz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='datastory', to='datastory.viz'),
        ),
    ]
