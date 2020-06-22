"""Template tag."""
from django import template
from users.models import CustomUser

register = template.Library()


@register.filter
def get_user(val):
    """Check if value is none."""
    user = CustomUser.objects.get(id=val)
    return user.first_name if user.first_name else user.email
