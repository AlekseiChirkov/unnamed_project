from django.db import models


class News(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class NewsImage(models.Model):
    news_post = models.ForeignKey(News, default=None, on_delete=models.CASCADE,
                                  blank=True, null=True, related_name='images')
    image = models.ImageField(upload_to='news/images')

    def __str__(self):
        return str(self.news_post)

    class Meta:
        verbose_name = 'News images'
        verbose_name_plural = 'News images'
