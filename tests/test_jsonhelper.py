

from lib.applogger import AppLogger
from lib.jsonhelper import dict_to_json, json_to_dict, os_environ_to_dict
from lib.pythonversionhelper import isinstance_of_string
from nose.tools import assert_equal
from nose.tools import assert_not_equal



LOGGER = AppLogger.create_instance()



class TestJsonHelper(object):
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        pass

    def teardown(self):
        """This method is run once after _each_ test method is executed"""

    def test_dict_to_json(self):
        data_dict = {'name': 'Jessy', 'testcase': 'test_dict_to_json'}
        data_json = dict_to_json(data_dict)
        name = data_dict['name']
        
        assert_equal( isinstance(data_dict, dict), True)
        assert_equal( isinstance_of_string(data_json), True)
        assert_equal( isinstance_of_string(name), True)
        
        
    def test_dict_to_json_str(self):
        data_dict = "{'name': 'Jessy', 'testcase': 'test_dict_to_json'}"
        data_json = dict_to_json(data_dict)
        
        assert_equal( isinstance_of_string(data_dict), True)
        assert_equal( isinstance_of_string(data_json), True)
        
        
    def test_json_to_dict(self):
        data_dict = {'name': 'Jessy', 'testcase': 'test_dict_to_json'}
        data_json = dict_to_json(data_dict)
        data_dict = json_to_dict(data_json)
        name = data_dict['name']
        
        assert_equal( isinstance(data_dict, dict), True)
        assert_equal( isinstance_of_string(data_json), True)
        assert_equal( isinstance_of_string(name), True)
        
    def test_os_environ_to_dict(self):
        env_dict = os_environ_to_dict()
        data_dict = {'name': 'Jessy', 'testcase': 'test_dict_to_json'}
        name = data_dict['name']
        home = env_dict['HOME']
        
        LOGGER.info("data_dict type: %s" %type(env_dict))
        LOGGER.info("data_dict type: %s" %type(data_dict))
        assert_equal( isinstance(env_dict, dict), True)
        assert_equal( isinstance(data_dict, dict), True)
        assert_not_equal( isinstance_of_string(env_dict), True)
        assert_not_equal( isinstance_of_string(data_dict), True)
        assert_equal( isinstance_of_string(name), True)
        assert_equal( isinstance_of_string(home), True)