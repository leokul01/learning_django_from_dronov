from django.db import models

class New(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    content = models.TextField()
    pub_date = models.DateField(db_index=True, auto_now_add = True)

    class Meta:
        db_table = 'news_category'
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

    def __str__(self):
        return self.title
