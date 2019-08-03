# Import Times ⏱⏱⏱

This package lets you print out import times like you were using the `-X importtime` runtime flag to Python 3.7, but with Python < 3.7 (I've tested it as working with 3.4+).

Put the following at the top of your main module:
```
from import_times import enable_import_times

enable_import_times()
```

Caveats:
- The timing information is probably different because 3.7 does its timing in `import.c` directly.
- You can't get timing information for things imported before any of your code is run (of course).

I haven't put this on PyPI yet, so to install this you can put this in your Pipfile:
```
import_times = {editable = true,git = "https://github.com/banool/import_times.git"}
```

or this in your requirements.txt:
```
git+git://github.com/banool/import_times.git
```

Good luck!! 🤠🤠🤠
