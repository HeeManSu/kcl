# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import sys
import typing
import ctypes
import os
import importlib
import json
import inspect

import kclvm.kcl.info as kcl_info
import kclvm.compiler.extension.plugin.plugin as kcl_plugin
import kclvm.api.object.internal.option as option
import kclvm.api.object as objpkg


from sys import version_info as _swig_python_version_info

if _swig_python_version_info >= (2, 7, 0):

    def swig_import_helper():
        import importlib

        pkg = __name__.rpartition(".")[0]
        mname = ".".join((pkg, "_kclvm_plugin")).lstrip(".")
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module("_kclvm_plugin")

    _kclvm_plugin = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):

    def swig_import_helper():
        from os.path import dirname
        import imp

        fp = None
        try:
            fp, pathname, description = imp.find_module(
                "_kclvm_plugin", [dirname(__file__)]
            )
        except ImportError:
            import _kclvm_plugin

            return _kclvm_plugin
        try:
            _mod = imp.load_module("_kclvm_plugin", fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod

    _kclvm_plugin = swig_import_helper()
    del swig_import_helper
else:
    import _kclvm_plugin
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if name == "thisown":
        return self.this.own(value)
    if name == "this":
        if type(value).__name__ == "SwigPyObject":
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if not static:
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if name == "thisown":
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError(
        "'%s' object has no attribute '%s'" % (class_type.__name__, name)
    )


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (
        self.__class__.__module__,
        self.__class__.__name__,
        strthis,
    )


try:
    _object = object
    _newclass = 1
except __builtin__.Exception:

    class _object:
        pass

    _newclass = 0

try:
    import weakref

    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


class _kclvm_plugin_AppContextBase(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(
        self, _kclvm_plugin_AppContextBase, name, value
    )
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(
        self, _kclvm_plugin_AppContextBase, name
    )
    __repr__ = _swig_repr

    def __init__(self, rust_invoke_json_ptr):
        if self.__class__ == _kclvm_plugin_AppContextBase:
            _self = None
        else:
            _self = self
        this = _kclvm_plugin.new__kclvm_plugin_AppContextBase(
            _self, rust_invoke_json_ptr
        )
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    __swig_destroy__ = _kclvm_plugin.delete__kclvm_plugin_AppContextBase
    __del__ = lambda self: None

    def _clear_options(self):
        return _kclvm_plugin._kclvm_plugin_AppContextBase__clear_options(self)

    def _add_option(self, key, value):
        return _kclvm_plugin._kclvm_plugin_AppContextBase__add_option(self, key, value)

    def _run_app(
        self,
        _start_fn_ptr,
        _kclvm_main_ptr,
        strict_range_check,
        disable_none,
        disable_schema_check,
        list_option_mode,
        debug_mode,
        buffer_size,
    ):
        return _kclvm_plugin._kclvm_plugin_AppContextBase__run_app(
            self,
            _start_fn_ptr,
            _kclvm_main_ptr,
            strict_range_check,
            disable_none,
            disable_schema_check,
            list_option_mode,
            debug_mode,
            buffer_size,
        )

    def _get_warn(self):
        return _kclvm_plugin._kclvm_plugin_AppContextBase__get_warn(self)

    def _get_cxx_invoke_proxy_ptr(self):
        return _kclvm_plugin._kclvm_plugin_AppContextBase__get_cxx_invoke_proxy_ptr(
            self
        )

    def _call_rust_method(self, name, args_json, kwargs_json):
        return _kclvm_plugin._kclvm_plugin_AppContextBase__call_rust_method(
            self, name, args_json, kwargs_json
        )

    def _call_py_method(self, name, args_json, kwargs_json):
        return _kclvm_plugin._kclvm_plugin_AppContextBase__call_py_method(
            self, name, args_json, kwargs_json
        )

    def __disown__(self):
        self.this.disown()
        _kclvm_plugin.disown__kclvm_plugin_AppContextBase(self)
        return weakref_proxy(self)


_kclvm_plugin_AppContextBase_swigregister = (
    _kclvm_plugin._kclvm_plugin_AppContextBase_swigregister
)
_kclvm_plugin_AppContextBase_swigregister(_kclvm_plugin_AppContextBase)


class AppContext(_kclvm_plugin_AppContextBase):
    def __init__(self, app_dll_name: str):
        self._is_windows: bool = os.name == "nt"

        self._start_func_name: str = ""
        self._app_dll_name = app_dll_name
        self._plugin_dict: typing.Dict[str, any] = {}

        if self._is_windows:
            _executable_root = os.path.dirname(sys.executable)
            self._kclvm_runtime = ctypes.CDLL(f"{_executable_root}\\kclvm.dll")
            self._app_lib = ctypes.CDLL(app_dll_name)
        else:
            self._kclvm_runtime = ctypes.CDLL(app_dll_name)
            self._app_lib = ctypes.CDLL(app_dll_name)

        self._kclvm_runtime.kclvm_plugin_init.restype = None
        self._kclvm_runtime.kclvm_plugin_init.argtypes = [ctypes.c_longlong]

        self._kclvm_runtime.kclvm_plugin_invoke_json.restype = ctypes.c_char_p
        self._kclvm_runtime.kclvm_plugin_invoke_json.argtypes = [
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_char_p,
        ]

        rust_invoke_json_ptr = ctypes.cast(
            self._kclvm_runtime.kclvm_plugin_invoke_json, ctypes.c_void_p
        ).value
        super().__init__(rust_invoke_json_ptr)

        self._kclvm_runtime.kclvm_plugin_init(self._get_cxx_invoke_proxy_ptr())

    def InitOptions(self, arguments):
        self._clear_options()
        for kv in arguments or []:
            key, value = kv
            if isinstance(value, (bool, list, dict)):
                value = json.dumps(value)
            elif isinstance(value, str):
                value = '"{}"'.format(value.replace('"', '\\"'))
            else:
                value = str(value)
            self._add_option(key, value)

    def RunApp(
        self,
        *,
        start_func_name="_kcl_run",
        strict_range_check=None,
        disable_none=None,
        disable_schema_check=None,
        list_option_mode=None,
        debug_mode=None,
        buffer_size=0,
    ) -> str:
        self._start_func_name = start_func_name

        _start = getattr(self._kclvm_runtime, start_func_name)
        _start_ptr = ctypes.cast(_start, ctypes.c_void_p).value

        if hasattr(self._app_lib, "kclvm_main"):
            _kclvm_main = getattr(self._app_lib, "kclvm_main")
            _kclvm_main_ptr = ctypes.cast(_kclvm_main, ctypes.c_void_p).value
        elif hasattr(self._app_lib, "kclvm_main_win"):
            _kclvm_main = getattr(self._app_lib, "kclvm_main_win")
            _kclvm_main_ptr = ctypes.cast(_kclvm_main, ctypes.c_void_p).value
        else:
            _kclvm_main_ptr = 0

        if disable_none:
            disable_none = 1
        else:
            disable_none = 0

        if strict_range_check:
            strict_range_check = 1
        else:
            strict_range_check = 0

        if disable_schema_check:
            disable_schema_check = 1
        else:
            disable_schema_check = 0

        if list_option_mode:
            list_option_mode = 1
        else:
            list_option_mode = 0

        if debug_mode:
            debug_mode = 1
        else:
            debug_mode = 0

        json_result = self._run_app(
            _start_ptr,
            _kclvm_main_ptr,
            strict_range_check,
            disable_none,
            disable_schema_check,
            list_option_mode,
            debug_mode,
            buffer_size,
        )
        return json_result

    def GetWarn(self) -> str:
        json_warn_result = self._get_warn()
        return json_warn_result

    def CallMethod(self, name: str, args_json: str, kwargs_json: str) -> str:
        return self._call_rust_method(name, args_json, kwargs_json)

    def _call_py_method(self, name: str, args_json: str, kwargs_json: str) -> str:
        try:
            return self._call_py_method_unsafe(name, args_json, kwargs_json)
        except Exception as e:
            return json.dumps({"__kcl_PanicInfo__": f"{e}"})

    def _get_plugin(self, plugin_name: str) -> typing.Optional[any]:
        if plugin_name in self._plugin_dict:
            return self._plugin_dict[plugin_name]

        module = kcl_plugin.get_plugin(plugin_name)
        self._plugin_dict[plugin_name] = module
        return module

    def _call_py_method_unsafe(
        self, name: str, args_json: str, kwargs_json: str
    ) -> str:
        dotIdx = name.rfind(".")
        if dotIdx < 0:
            return ""

        modulePath = name[:dotIdx]
        mathodName = name[dotIdx + 1 :]

        plugin_name = modulePath[modulePath.rfind(".") + 1 :]

        module = self._get_plugin(plugin_name)
        mathodFunc = None

        for func_name, func in inspect.getmembers(module):
            if func_name == kcl_info.demangle(mathodName):
                mathodFunc = func
                break

        args = []
        kwargs = {}

        if args_json:
            args = json.loads(args_json)
            if not isinstance(args, list):
                return ""
        if kwargs_json:
            kwargs = json.loads(kwargs_json)
            if not isinstance(kwargs, dict):
                return ""

        result = mathodFunc(*args, **kwargs)
        return json.dumps(result)

    def __del__(self):
        self._free_library()

    def _free_library(self):
        if os.name == "nt":
            import ctypes.wintypes

            kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
            kernel32.FreeLibrary.argtypes = [ctypes.wintypes.HMODULE]
            kernel32.FreeLibrary(self._app_lib._handle)
            self._app_lib = None
            # kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
            # kernel32.FreeLibrary.argtypes = [ctypes.wintypes.HMODULE]
            # kernel32.FreeLibrary(self._app_dll._handle)
            pass
        else:
            # libdl = ctypes.CDLL("libdl.so")
            # libdl.dlclose(self._app_dll._handle)
            pass


def main(args: typing.List[str]):
    if len(args) < 2:
        print("usage: kclvm_plugin app.[dll|dylib|so]")
        sys._exit(1)

    ctx = AppContext(args[1])
    ctx.RunApp(args[2:])


if __name__ == "__main__":
    main(sys.argv)

# This file is compatible with both classic and new-style classes.