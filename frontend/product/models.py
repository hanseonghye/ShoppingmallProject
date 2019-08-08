from django.db import models

class ProductImage(models.Model):
    main = models.ImageField()
    content = models.ImageField()

    class Meta:
        db_table = "product_image"