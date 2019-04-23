from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'goods_category'
        ordering = ['name',]
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name

class Good(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    in_stock = models.BooleanField(default=True, db_index=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'goods_good'
        ordering = ['name',]
        unique_together = ('category', 'name')
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        s = self.name
        if not self.in_stock:
            s = s + ' (нет в наличии)'
        return s

    def save(self, *args, **kwargs):
        super(Good, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        super(Good, self).delete(*args, **kwargs)
    
