from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Пост')
    link = models.CharField(max_length=255, verbose_name='Ссылка')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def amount_votes(self):
        return self.votes.count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Vote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes', db_index=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    author_name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    post = models.ForeignKey(Post, verbose_name="фильм", on_delete=models.CASCADE, related_name="post_comment")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f"{self.name} - {self.post.title}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
