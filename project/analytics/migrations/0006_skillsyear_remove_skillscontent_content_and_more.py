# Generated by Django 5.0.1 on 2024-01-21 16:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_remove_demandcontent_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillsYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.JSONField(null=True)),
                ('load_dttm', models.DateTimeField(auto_now_add=True)),
                ('graphic', models.ImageField(null=True, upload_to='images/skills')),
            ],
        ),
        migrations.RemoveField(
            model_name='skillscontent',
            name='content',
        ),
        migrations.RemoveField(
            model_name='skillscontent',
            name='graphic',
        ),
        migrations.AlterField(
            model_name='demandcontent',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='geographycontent',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='skillscontent',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='skillscontent',
            name='graphics',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='analytics.skillsyear'),
        ),
    ]
