# Generated by Django 5.1.3 on 2024-11-22 12:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='is_published',
        ),
        migrations.AddField(
            model_name='post',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='PostReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('status', models.CharField(choices=[('ACC', 'Accepted'), ('REV', 'Review Required'), ('DEC', 'Declined'), ('SENT', 'Sent to review')], max_length=4)),
                ('mentor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.post')),
            ],
        ),
    ]
