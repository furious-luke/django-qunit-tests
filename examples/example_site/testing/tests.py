import os
from django.test import TestCase
from qunit_tests.tests import QUnitTestCase

class ExampleTestCase(QUnitTestCase):
    html = os.path.join(os.path.dirname(__file__), 'qunit/example.tests.html')
