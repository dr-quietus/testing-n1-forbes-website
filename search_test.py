from pages.search_page import *


def test_provera_linka_drustvenih_mreza():
    provera_linka_drustvenih_mreza()


def test_prolaz_kroz_rubriku():
    prolaz_kroz_rubriku()


@pytest.mark.parametrize('search_term', ['Ekonomija', '%', 'Bitkoin', 'Bussiness', 'zena', '&', '123', 'tu%'])
def test_search(search_term):
    search(search_term)


def test_email():
    email_provera()