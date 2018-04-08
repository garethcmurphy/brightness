from ..bright import brightscrape

__author__ = "Gareth Murphy"
__credits__ = ["Gareth Murphy"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Gareth Murphy"
__email__ = "garethcmurphy@gmail.com"
__status__ = "Development"


def test_scrape():
    bright = brightscrape.Scrape()
    assert isinstance(bright.bright_url, str)
