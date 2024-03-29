# Generated by Django 4.1.7 on 2023-04-24 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_alter_person_bio_alter_person_phone_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='isbn',
            new_name='edition',
        ),
        migrations.AddField(
            model_name='review',
            name='rate',
            field=models.TextField(default='1', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.CharField(max_length=46, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
