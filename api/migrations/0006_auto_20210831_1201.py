# Generated by Django 3.2.6 on 2021-08-31 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_answer_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.IntegerField(choices=[(1, 'option 1'), (2, 'option 2'), (3, 'option 3'), (4, 'option 4')], default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
