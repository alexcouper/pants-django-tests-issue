import os


_CLEANUPS = {}


def _cleanup(name, value):
    if value is None:
        del os.environ[name]
    else:
        os.environ[name] = value


def pytest_runtest_setup(item):
    old_value = os.environ.get('DJANGO_SETTINGS_MODULE')
    _CLEANUPS[item] = lambda: _cleanup('DJANGO_SETTINGS_MODULE', old_value)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'project1.config.settings'


def pytest_runtest_teardown(item, nextitem):
    _CLEANUPS.get(item, lambda: None)()