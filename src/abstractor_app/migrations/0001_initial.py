# Generated by Django 3.1.7 on 2021-03-28 23:35

import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abstraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grantors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32767, null=True), size=None)),
                ('grantees', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32767, null=True), size=None)),
                ('books', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=4, null=True), size=None)),
                ('pages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=4, null=True), size=None)),
                ('reception_numbers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20, null=True), size=None)),
                ('document_types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32767, null=True), size=None)),
                ('recording_dates', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10, null=True), size=None)),
                ('legals', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32767, null=True), size=None)),
                ('related_documents', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32767, null=True), size=None)),
                ('comments', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32767, null=True), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grantor', models.CharField(max_length=32767, null=True)),
                ('grantee', models.CharField(max_length=32767, null=True)),
                ('page', models.CharField(max_length=4, null=True)),
                ('book', models.CharField(max_length=4, null=True)),
                ('reception_number', models.CharField(max_length=20, null=True)),
                ('document_type', models.CharField(max_length=32767, null=True)),
                ('recording_date', models.CharField(max_length=10, null=True)),
                ('legal', models.CharField(max_length=32767, null=True)),
                ('related', models.CharField(max_length=32767, null=True)),
                ('comment', models.CharField(max_length=32767, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
