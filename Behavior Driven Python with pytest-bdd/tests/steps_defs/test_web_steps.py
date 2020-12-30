import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Constant variables
DUCKDUCKGO_HOME = 'https://duckduckgo.com/'


# Scenarios
scenarios('../features/web.feature')


# When Steps
@when(parsers.parse('the user searches for "{text}"'))
@when(parsers.parse('the user searches for the phrase {text}"'))
def search_phrase(browser, text):
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(text + Keys.RETURN)


# Then Steps
@then(parsers.parse('one of the results contains "{phrase}"'))
def results_have_one(browser, phrase):
    xpath = f"//div[@id='links']//*[contains(text(), '{phrase}')]"
    results = browser.find_elements_by_xpath(xpath)
    assert len(results) > 0


@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    # Check search result list
    # A more comprehensive test would check results for matching phrases
    # Check the list before the search phrase for correct implicit waiting
    links_div = browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    
    # Check search phrase
    search_input = browser.find_element_by_name('q')
    assert not search_input.get_attribute('value') == phrase