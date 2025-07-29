from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UniversityCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=50)),
                ('duration_weeks', models.PositiveIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_universities', to='universities.course')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='university_courses', to='universities.university')),
            ],
            options={
                'unique_together': {('university', 'course', 'semester')},
            },
        ),
    ]