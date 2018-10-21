from __future__ import absolute_import, division, print_function

from importlib import import_module

try:
    from datacube_wms.wms_cfg_local import service_cfg, layer_cfg, response_cfg
except ImportError:
    from datacube_wms.wms_cfg import service_cfg, layer_cfg, response_cfg


def resp_headers(d):
    hdrs = {}
    hdrs.update(response_cfg)
    hdrs.update(d)
    return hdrs


def get_function(func):
    """Converts a config entry to a function, if necessary

    :param func: Either a Callable object or a fully qualified function name str, or None
    :return: a Callable object, or None
    """
    if not callable(func) or func is not None:
        mod_name, func_name = func.rsplit('.', 1)
        mod = import_module(mod_name)
        func = getattr(mod, func_name)
        assert callable(func)
    return func
