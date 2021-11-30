from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
