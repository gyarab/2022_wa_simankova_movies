from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_movie_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='films.genre'),
        ),
    ]