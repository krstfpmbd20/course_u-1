# Generated by Django 4.2.7 on 2023-11-24 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('indicator_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('indicator', models.CharField(max_length=4)),
                ('indicator_name', models.CharField(max_length=50)),
                ('indicator_description', models.CharField(max_length=1000)),
                ('skills', models.ManyToManyField(to='website.skill')),
            ],
        ),
        migrations.CreateModel(
            name='MBTI',
            fields=[
                ('mbti', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('mbti_question', models.CharField(max_length=1000)),
                ('option_a', models.CharField(max_length=1000)),
                ('option_b', models.CharField(max_length=1000)),
                ('ans_a', models.CharField(max_length=15)),
                ('ans_b', models.CharField(max_length=15)),
                ('acr_a', models.CharField(default='a', max_length=1)),
                ('acr_b', models.CharField(default='b', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='MBTISet',
            fields=[
                ('mbti_set_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('mind', models.FloatField(default=0)),
                ('energy', models.FloatField(default=0)),
                ('nature', models.FloatField(default=0)),
                ('tactics', models.FloatField(default=0)),
                ('identity', models.CharField(blank=True, max_length=4, null=True)),
                ('indicator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personality.indicator')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user',)},
            },
        ),
        migrations.CreateModel(
            name='MBTIResponse',
            fields=[
                ('mbti_response_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('is_answered', models.BooleanField(default=False)),
                ('selected_option', models.IntegerField(default=0)),
                ('mbti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personality.mbti')),
                ('mbti_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personality.mbtiset')),
            ],
            options={
                'unique_together': {('mbti_set', 'mbti')},
            },
        ),
    ]