# Generated by Django 5.1.1 on 2024-09-16 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_alter_movie_launch_date_booking"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="Image",
            field=models.ImageField(
                default="defaultmovie.jpeg", upload_to="profile_pics"
            ),
        ),
    ]
