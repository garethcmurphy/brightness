from ..bright import brightness

__author__ = "Gareth Murphy"
__credits__ = ["Gareth Murphy"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Gareth Murphy"
__email__ = "garethcmurphy@gmail.com"
__status__ = "Development"


def test_doi():
    bright = brightness.Brightness()
    assert isinstance(bright.passw, str)
    assert isinstance(bright.user, str)
