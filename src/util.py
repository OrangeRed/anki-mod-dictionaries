from os.path import dirname, join


def get_path(*comps: str) -> str:
    addon_dir = dirname(__file__)
    if not comps:
        return addon_dir
    else:
        return join(addon_dir, *comps)
