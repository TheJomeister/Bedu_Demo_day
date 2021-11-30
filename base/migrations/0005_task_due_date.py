from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
