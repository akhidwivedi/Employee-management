# Generated by Django 2.2 on 2020-04-07 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('emp_code', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=30)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.position')),
            ],
        ),
    ]
