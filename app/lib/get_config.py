import os


def get_config(config_class: str = None, key: str = None) -> dict:
    if not config_class:
        config_class = os.getenv("CONFIG", "config.Production")
    components = config_class.split(".")
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    config_mod = mod()
    config = {}
    for config_key in dir(config_mod):
        if config_key.isupper():
            value = getattr(config_mod, config_key)
            if config_key == key:
                return value
            config[config_key] = value
    return config
