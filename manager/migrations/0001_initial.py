# Generated by Django 3.2.9 on 2023-11-18 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.crypto
import django.utils.timezone
import manager.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='name')),
                ('email', models.CharField(max_length=50, null=True, verbose_name='email address')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=13, null=True, region=None, unique=True, verbose_name='phone')),
                ('subject', models.CharField(max_length=50, null=True, verbose_name='subject')),
                ('message', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExtendedAdmin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('main', models.BooleanField(default=False)),
                ('is_installed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'extended_admins',
                'db_table': 'extended_admin',
            },
        ),
        migrations.CreateModel(
            name='ExtendedAuthUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=13, null=True, region=None, unique=True, verbose_name='phone')),
                ('initials', models.CharField(blank=True, max_length=10, null=True)),
                ('is_client', models.BooleanField(blank=True, default=False, null=True)),
                ('serial_no', models.CharField(blank=True, default=django.utils.crypto.get_random_string, max_length=100, null=True)),
                ('bgcolor', models.CharField(blank=True, default=manager.models.bgcolor, max_length=10, null=True)),
                ('followers', models.IntegerField(blank=True, default=0, null=True)),
                ('following', models.IntegerField(blank=True, default=0, null=True)),
                ('upvotes', models.IntegerField(blank=True, default=0, null=True)),
                ('downvotes', models.IntegerField(blank=True, default=0, null=True)),
                ('articles', models.IntegerField(blank=True, default=10, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='profiles/placeholder.jpg', null=True, upload_to='profiles/')),
                ('role', models.CharField(blank=True, choices=[('employee', 'Employee'), ('admins', 'Admin')], max_length=200, null=True)),
                ('nickname', models.CharField(blank=True, default='Your nickname', max_length=100, null=True)),
                ('facebook', models.URLField(blank=True, default='https://facebook.com/username', null=True)),
                ('twitter', models.URLField(blank=True, default='https://twitter.com/username', null=True)),
                ('instagram', models.URLField(blank=True, default='https://instagram.com/username', null=True)),
                ('github', models.URLField(blank=True, default='https://github.com/username', null=True)),
                ('bio', models.TextField(blank=True, default='something about you...', null=True)),
                ('company', models.CharField(blank=True, default='Devme', max_length=100, null=True)),
                ('shipping_address', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'extended_auth_users',
                'db_table': 'extended_auth_user',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='title')),
                ('link', models.CharField(blank=True, max_length=50, null=True, verbose_name='link')),
                ('caption', models.CharField(blank=True, max_length=50, null=True, verbose_name='caption')),
                ('project_id', models.CharField(default=manager.models.generate_id, max_length=50, verbose_name='project id')),
                ('likes', models.IntegerField(blank=True, null=True, verbose_name='likes')),
                ('views', models.IntegerField(blank=True, null=True, verbose_name='views')),
                ('comments', models.IntegerField(blank=True, null=True, verbose_name='comments')),
                ('replies', models.IntegerField(blank=True, null=True, verbose_name='replies')),
                ('upvote', models.IntegerField(blank=True, null=True, verbose_name='upvote')),
                ('downvote', models.IntegerField(blank=True, null=True, verbose_name='downvote')),
                ('tags', models.CharField(blank=True, max_length=250, null=True, verbose_name='tags')),
                ('category', models.CharField(blank=True, max_length=100, null=True, verbose_name='tag')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='gallary/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.project')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('name', models.CharField(blank=True, default=False, max_length=100, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('profile_pic', models.CharField(blank=True, default=False, max_length=100, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'review_tbl',
                'db_table': 'review_tbl',
            },
        ),
        migrations.CreateModel(
            name='SubscribersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, null=True, unique=True, verbose_name='email address')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectReplies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.projectcomments')),
            ],
        ),
        migrations.CreateModel(
            name='ExtendedProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='gallary/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.project')),
            ],
        ),
        migrations.CreateModel(
            name='DesignModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, default=False, max_length=100, null=True)),
                ('progress', models.IntegerField(blank=True, default=0, null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'design_tbl',
                'db_table': 'design_tbl',
            },
        ),
    ]
