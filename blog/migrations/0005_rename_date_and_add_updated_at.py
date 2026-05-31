from django.conf import settings
from django.db import migrations, models
from django.utils import timezone


def copy_date_to_timestamps(apps, schema_editor):
    Post = apps.get_model("blog", "Post")
    for post in Post.objects.all():
        dt = timezone.make_aware(
            timezone.datetime.combine(post.date, timezone.datetime.min.time())
        )
        post.created_at = dt
        post.updated_at = dt
        post.save(update_fields=["created_at", "updated_at"])


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_post_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="updated_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.RunPython(
            copy_date_to_timestamps,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.RemoveField(
            model_name="post",
            name="date",
        ),
        migrations.AlterField(
            model_name="post",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=models.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="upload"),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created_at"]},
        ),
    ]
