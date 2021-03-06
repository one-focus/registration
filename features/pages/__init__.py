from .french_visa_page import FrenchVisaPage
from .german_visa_page import GermanVisaPage
from .google_page import GooglePage
from .italy_consulate_page import ItalyConsulatePage
from .italy_embassy_page import ItalyEmbassyPage

page_map = {
    "google.com": GooglePage,
    "german visa": GermanVisaPage,
    "italy consulate": ItalyConsulatePage,
    "italy embassy": ItalyEmbassyPage,
    "french visa": FrenchVisaPage,
}


def factory(page_name: str):
    """Encapsulate screen creation"""
    return page_map[page_name]
