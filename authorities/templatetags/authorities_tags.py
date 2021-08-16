from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def user_authorities(
    context,
):
    try:
        return context.request.user.authorities.all()
    except AttributeError:
        return []
