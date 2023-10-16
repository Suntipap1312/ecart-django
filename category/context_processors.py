from .models import Category

# Global variable
def menu_link(request):
    links = Category.objects.all()
    return dict(links=links)