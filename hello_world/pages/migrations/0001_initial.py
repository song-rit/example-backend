# Generated by Django 3.0.5 on 2020-04-27 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=300)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('?', 'Unknown')], default='?', max_length=1)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('race', models.CharField(choices=[('ASIAN', 'Asian'), ('BLACK', 'Black'), ('LATINO', 'Latino'), ('WHITE', 'White'), ('OTHER', 'Other'), ('?', 'Unknown')], default='?', max_length=10)),
            ],
        ),
    ]