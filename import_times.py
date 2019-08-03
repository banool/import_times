import importlib.util as iu
import importlib._bootstrap as ib
import importlib._bootstrap_external as ibe

from contextlib import contextmanager
import inspect
import sys
import time


_done = set()
_import_level = 0
_accumulated = 0


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
    _accumulated = 0
    start = time.time()
    yield
    end = time.time()
    total = int((end - start) * 1000000)
    _import_level -= 1
    indentation = " " * _import_level * 2
    print(
        "import time: {:9d} | {:10d} | {}{}".format(
            total - _accumulated, total, indentation, module_name
        ),
        file=sys.stderr,
    )
    _accumulated += total


def _get_new_loader(f):

    def new(loader, module, *args, **kwargs):
        with _timer(module.__name__):
            out = f(loader, module, *args, **kwargs)
        return out

    return new


def enable_import_times():
    print("import time: self [us] | cumulative | imported package", file=sys.stderr)
    loaders = set()
    for module in [iu, ib, ibe]:
        loaders.update([i[1] for i in inspect.getmembers(module, inspect.isclass)])

    for l in loaders:
        if not hasattr(l, "exec_module"):
            continue
        l.exec_module = _get_new_loader(l.exec_module)
