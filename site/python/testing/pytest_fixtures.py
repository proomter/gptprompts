import pytest
import tempfile


@pytest.fixture
def c_instance():
    return C()

# there is builtin temp dir in pytest
@pytest.fixture
def  temporary_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir

@pytest.fixture
def setup_tear():
    print("setup")
    yield
    print("teardown")

class C:
    def f(self):
        return 1

    def g(self):
        return 1

def test_f(c_instance):
    assert c_instance.f()==1
def test_g(c_instance):
    assert c_instance.g()==1

def test_with_tear_down(setup_tear):
    print("in test")


## we can use fixtures inside fixtures
