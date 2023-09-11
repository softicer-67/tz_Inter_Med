from django import template
register = template.Library()


@register.simple_tag(takes_context=True)
def next_page(context):
    request = context['request']
    page = context['page']

    params = request.GET.copy()
    params['page'] = page.next_page_number
    return f"?{params.urlencode()}"
