
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_genre_movie_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, null=True, to='films.genre'),
        ),
    ]