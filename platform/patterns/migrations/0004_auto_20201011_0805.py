# Generated by Django 3.0.7 on 2020-10-11 08:05

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('patterns', '0003_auto_20201011_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urbandesignpattern',
            name='keywords',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of keywords.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Keywords'),
        ),
    ]
