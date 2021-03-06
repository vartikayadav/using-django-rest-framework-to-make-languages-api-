# Generated by Django 2.0.7 on 2019-02-08 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paradigm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='languages',
            name='paradigm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='languages.Paradigm'),
        ),
        migrations.AddField(
            model_name='programmer',
            name='language',
            field=models.ManyToManyField(to='languages.Languages'),
        ),
    ]
