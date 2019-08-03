# Import Times

This package lets you print out import times like you were using the `-X importtime` runtime flag to Python 3.7, but with Python < 3.7.

Put the following at the top of your main module:
```
from import_times import enable_import_times

enable_import_times()
```

I've only tested this with Python 3.6 so far.

Caveats:
- The timing information is probably different because 3.7 does their timing in `import.c` directly.
- You can't get timing information for things imported by default before any of your code is run.

