from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_task_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['due_date']},
        ),
    ]
