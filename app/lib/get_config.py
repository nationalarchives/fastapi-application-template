def get_config(config_class):
    components = config_class.split(".")
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    config_mod = mod()
    config = {}
    for key in dir(config_mod):
        if key.isupper():
            config[key] = getattr(config_mod, key)
    return config
