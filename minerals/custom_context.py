from .utils import get_mineral_groups


def add_mineral_groups(request):
    groups = get_mineral_groups()
    groups.append('Other')
    return {'groups': groups}
