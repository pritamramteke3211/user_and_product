# Generated by Django 3.2.9 on 2021-11-03 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_postcomment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='parent',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
