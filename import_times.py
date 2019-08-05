loader_modules = []
import importlib.util as iu
loader_modules.append(iu)
import importlib._bootstrap as ib
loader_modules.append(ib)
try:
    import importlib._bootstrap_external as ibe
    loader_modules.append(ibe)
except ImportError:
    pass

from contextlib import contextmanager
import inspect
import sys
import time


_done = set()
_import_level = 0
_accumulated = []


@contextmanager
def _timer(module_name):
    global _done
    global _import_level
    global _accumulated
    if module_name in _done:
        yield
        return
    _done.add(module_name)
    _import_level += 1
    _accumulated.append(0)
    start = time.time()
    yield
    end = time.time()
    total = int((end - start) * 1000000)
    _import_level -= 1
    indentation = " " * _import_level * 2
    print(
        "import time: {:9d} | {:10d} | {}{}".format(
            total - _accumulated[-1], total, indentation, module_name
        ),
        file=sys.stderr,
    )
    _accumulated.pop()
    if _accumulated:
        _accumulated[-1] += total


def _get_new_loader(f):
    def new(loader, *args, **kwargs):
        module = "__unknown__"
        if len(args):
            module = args[0].__name__
        with _timer(module):
            global _import_level
            try:
                out = f(loader, *args, **kwargs)
            except:
                _import_level -= 1
                raise

        return out

    return new


def enable_import_times():
    print("import time: self [us] | cumulative | imported package", file=sys.stderr)
    loaders = set()
    for module in loader_modules:
        loaders.update([i[1] for i in inspect.getmembers(module, inspect.isclass)])

    for l in loaders:
        if not hasattr(l, "exec_module"):
            continue
        l.exec_module = _get_new_loader(l.exec_module)
