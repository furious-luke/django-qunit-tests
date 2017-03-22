import types, six, re
from selenium import webdriver
from django.test import SimpleTestCase, TestCase

class Wrapper(object):

    def __init__(self, test):
        self.test = test

    def __call__(self, inst):
        inst.run_test(self.test)

    def __get__(self, inst, owner):
        return types.MethodType(self, inst) if inst else self

class QUnitTestCaseMetaclass(type):

    def __new__(mcs, name, bases, attrs):
        if name != 'QUnitTestCase':
            html = attrs.get('html', None)
            if not html:
                raise Exception('QUnitTestCase requires an HTML file.')

            wd = webdriver.PhantomJS()
            wd.get(html)
            tests = wd.find_elements_by_xpath('//ol[@id="qunit-tests"]/li')
            if not tests:
                wd.quit()
                raise Exception('No tests found')
            attrs['wd'] = wd
            for ii, test in enumerate(tests):
                name = str(test.find_element_by_xpath('.//span[@class="test-name"]').get_attribute('innerHTML'))
                name = 'test_' + re.sub('\W|^(?=\d)', '_', name)
                attrs[name] = Wrapper(test)

        return super(QUnitTestCaseMetaclass, mcs).__new__(mcs, name, bases, attrs)


@six.add_metaclass(QUnitTestCaseMetaclass)
class QUnitTestCase(SimpleTestCase):
    html = None

    def run_test(self, test):
        asrts = test.find_elements_by_xpath('.//li')
        for asrt in asrts:
            self.assertEqual(test.get_attribute('class'), 'pass')

    @classmethod
    def tearDownClass(cls):
        cls.wd.quit()
        return super(QUnitTestCase, cls).tearDownClass()
