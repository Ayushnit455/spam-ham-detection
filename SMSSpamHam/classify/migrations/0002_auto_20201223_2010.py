# Generated by Django 3.0.6 on 2020-12-23 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classify', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HamSpamTweets',
        ),
        migrations.DeleteModel(
            name='SpamURLS',
        ),
        migrations.DeleteModel(
            name='Words_Users',
        ),
    ]