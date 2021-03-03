from django import template
from blogger.models import Category

register = template.Library()

@register.inclusion_tag('blogger/cats.html')
def get_category_list():
    return {'cats': Category.objects.all()}