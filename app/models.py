from django.db import models




class SizeProduct(models.Model):
    SIZES = (
        ("SML", 'SML'),
        ("MED", 'MED'),
        ("LRG", 'LRG'),
        ("XLG", 'XLG'),
    )
    size = models.CharField('Size', choices=SIZES, max_length=30)

    @staticmethod
    def get_default_sizes():
        # Retrieve all available sizes and return them as a list of choices
        return [size[0] for size in SizeProduct.SIZES]

    def __str__(self):
        return self.size

class ColorProduct(models.Model):
    COLORS = (
        ("Red", "Red"),
        ("Black", "Black"),
        ("White", "White"),
        ("Yellow", "Yellow"),
    )
    color = models.CharField('Color', choices=COLORS,max_length=30)
    def __str__(self):
        return self.color

class MoreImages(models.Model):
    image = models.FileField()
    product = models.ForeignKey("Products", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}"


class Category(models.Model):
    categories = models.CharField(max_length=50)
    def __str__(self):
        return self.categories

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,related_name='subcategory',blank=True)
    def __str__(self):
        return self.name

class Products(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    price = models.CharField(max_length=50)
    out_of_stock = models.BooleanField(default=False)
    size = models.ManyToManyField(SizeProduct, related_name="product_size", blank=True, default=SizeProduct.get_default_sizes)
    color = models.ManyToManyField("ColorProduct", related_name="product_color", blank=True)
    image = models.ImageField(upload_to='products/')
    subCategory = models.ForeignKey("SubCategory", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.pk}'