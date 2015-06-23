# django-qunit-tests

A simple application to integrate QUnit tests into Django.

## License

GPLv2

## Dependencies

The Python based dependencies are automatically installed when using the
provided `setup.py` script. However, PhantomJS is also required in order
to run javascript without opening a browser.

If using `npm` then you should be able to install PhantomJS with: `npm -g install phantomjs`.

## Installation

After downloading and unpacking, run the setup script:
```bash
./setup.py install
```

Then, add `qunit_tests` to your `INSTALLED_APPS` list in `settings.py`:
```python
INSTALLED_APPS = (
    ...
    'qunit_tests',
)
```

## Integrating qUnit Tests

The key feature that makes integration of qUnit tests into Django
easier is the `QUnitTestCase` class. This is stored in `qunit_tests.tests`
and should be imported into any Django test code that needs to include a
qUnit test. This class inherits from Django's `TestCase` class.

To use `QUnitTestCase`, all that is required is to set a class level value
for `html`, which contains the path to the qUnit test HTML interface. And
that's all! The actual tests will be automatically imported and set on the
class using metaclasses.

As an example, this what a simple test integration looks:

```python
import os
from qunit_tests.tests import QUnitTestCase

class SomethingTestCase(QUnitTestCase):
    html = os.path.join(os.path.dirname(__file__), 'qunit/test_something.html')
```
