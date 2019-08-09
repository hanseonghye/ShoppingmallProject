from django.db import models

class ProductImage(models.Model):
    main = models.ImageField(upload_to='main/')
    content = models.ImageField(upload_to='content/')

    class Meta:
        db_table = "product_image"


    def __str__(self):
        return f'ProductImage : {self.main}'