# Generated by Django 4.1.6 on 2023-02-21 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("leaveRequest", "0002_rename_user_id_leaverequest_user_name_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="leaverequest", old_name="user_name", new_name="user_id",
        ),
    ]
