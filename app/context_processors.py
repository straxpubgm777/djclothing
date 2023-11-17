from app.models import *

def categories(request):
    categories = Category.objects.all()
    subCategories = SubCategory.objects.all()
    return {'categories': categories,"subCategories":subCategories}