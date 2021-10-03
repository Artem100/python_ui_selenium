import logging

import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, \
    JavascriptException, WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def format_selector(by, locator, name=None):
	selector = (by, locator)
	name = name if name else selector
	return selector, name

class BasePage():


    def __init__(self, driver):
        self.driver = driver

    driver = None
    timeout = 10

    def browser_close(self):
        self.driver.quit()

    def open_page_via_url(self, url):
        logging.info(f"Open page via {url}")
        self.driver.get(url)

    def refresh_page(self):
        logging.info(f"Refresh current page")
        self.driver.refresh()

    def __timeout_element_error(self, selector, name):
        """ Timeout Webdriver and NoSuchElementException"""
        allure.attach(self.driver.get_screenshot_as_png(), name=f"Element {name} Timeout exception",
                      attachment_type=allure.attachment_type.PNG)
        logging.error(f"Timeout - < {name} > element not found: {selector}")
        raise Exception(f"Timeout - < {name} > element not found: {selector}")

    # AssertionError
    def __element_doesnt_contain_expected_value_error(self, name, value, result):
        allure.attach(self.driver.get_screenshot_as_png(), name=f"Element {name} does not contain expected text: {value}",
                      attachment_type=allure.attachment_type.PNG)
        logging.error(f"Element < {name} > doesn't contain expected value. \nExpected value: {value},\nActual value: {result}")
        raise AssertionError(f"Element < {name} > doesn't contain expected value. \nExpected value: {value},\nActual value: {result}")

    def __cant_click_on_the_element_error(self, selector, name):
        """ErrorHandler, ElementClickInterceptedException"""
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=f"Driver can't click on {name} element",
                      attachment_type=allure.attachment_type.PNG)
        logging.error(f"Can't click on {name} element: {selector}")
        raise Exception(f"Can't click on {name} element: {selector}")

    # WebDriverWait
    def __element_isnt_display_on_page(self, selector, name):
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=f"Element isn't displayed: {name} on page",
                      attachment_type=allure.attachment_type.PNG)
        logging.error(f"WebDriverWait exception: Element < {selector} > isn't displayed: {name} on page")
        assert Exception(f"WebDriverWait exception: Element < {selector} > isn't displayed: {name} on page")

    def __browser_system_error(self, e):
        logging.error(f"Some problems with browser\n{e}")
        assert False, f"Some problems with browser\n{e}"


    def __find_element_located(self, selector, name):
        try:
            element = WebDriverWait(self.driver, BasePage.timeout).until(EC.presence_of_element_located(selector))
            return element
        except (TimeoutException, NoSuchElementException):
            self.__timeout_element_error(selector, name)
        except Exception as e:
            assert False, f"Some problems with browser or element: \n {e}"


    def __find_element_clickable(self, selector, name):
        try:
            element = WebDriverWait(self.driver, BasePage.timeout).until(EC.element_to_be_clickable(selector))
            return element
        except (TimeoutException, NoSuchElementException):
            self.__timeout_element_error(selector, name)
        except ElementClickInterceptedException:
            self.__cant_click_on_the_element_error(selector, name)
        except Exception as e:
            logging.error( f"Some problems with browser or element: \n {e}")
            assert False, f"Some problems with browser or element: \n {e}"

    def __find_elements_visibility(self, selector, name):
        logging.info("Find elements < {} > ".format(name))
        try:
            elements = WebDriverWait(self.driver, BasePage.timeout).until(EC.visibility_of_all_elements_located(selector))
            return elements
        except (TimeoutException, NoSuchElementException):
            self.__timeout_element_error(selector, name)
        except Exception as e:
            assert False, f"Some problems with browser or element: \n {e}"

    def _element_displayed(self, *selector):
        selector, name = format_selector(*selector)
        with allure.step(f"Check  {name} element is visible"):
            try:
                logging.info(f"Element {name} is visible")
                element = WebDriverWait(self.driver, BasePage.timeout).until(EC.visibility_of_element_located(selector))
                return element
            except (NoSuchElementException, TimeoutException):
                self.__timeout_element_error(self, name)
            except Exception as e:
                self.__browser_system_error(e)


    def _click(self, *selector):
        selector, name = format_selector(*selector)
        with allure.step(f"Click on element {name}"):
            element = self.__find_element_clickable(selector, name)
            try:
                logging.info(f"Click {name} element")
                element.click()
                return element
            except ElementClickInterceptedException:
                self.__cant_click_on_the_element_error(selector, name)
            except (NoSuchElementException, TimeoutException):
                self.__timeout_element_error(self, name)
            except Exception as e:
                self.__browser_system_error(e)

    def _input_text(self, text, *selector):
        selector, name = format_selector(*selector)
        with allure.step(f"Input text to element {name}"):
            element = self.__find_element_located(selector, name)
            try:
                logging.info(f"Input text to {name} element")
                element.send_keys(text)
                return element
            except (NoSuchElementException, TimeoutException):
                self.__timeout_element_error(self, name)
            except Exception as e:
                self.__browser_system_error(e)

    def _check_text_in_element(self, text, *selector):
        selector, name = format_selector(*selector)
        with allure.step(f"Check text in element {name}"):
            element = self.__find_element_located(selector, name)
            try:
                logging.info(f"Check value: *{text}* in < {name} > element")
                result = element.text
                assert text == result
            except AssertionError:
                self.__element_doesnt_contain_expected_value_error(name, text, result)
            except (NoSuchElementException, TimeoutException):
                self.__timeout_element_error(self, name)
            except Exception as e:
                self.__browser_system_error(e)

    def _count_of_elements_on_page(self, count, *selector):
        selector, name = format_selector(*selector)
        with allure.step(f"Check count of elements {name}"):
            elements = self.__find_elements_visibility(selector, name)
            logging.info(f"Check count *{count}* of elements {name}")
            try:
                assert len(elements) == int(count)
            except AssertionError:
                allure.attach(self.driver.get_screenshot_as_png(),
                              name=f"Incorrect count of {name} elements",
                              attachment_type=allure.attachment_type.PNG)
                logging.info(f"Count value doesn't match with test in element < {name} >.\nActual result: {elements}\nExpected result: {count}")
                assert False, f"Count value doesn't match with test in element < {name} >.\nActual result: {elements}\nExpected result: {count}"
            except Exception as e:
                self.__browser_system_error(e)

    def _title_page_check(self, page_title):
        with allure.step(f"Test in *{page_title}*"):
            current_page = self.driver.title
            try:
                logging.info(f"Check TITLE of page < {page_title} > ")
                current_page = WebDriverWait(self.driver, BasePage.timeout).until(EC.title_contains(page_title))
                logging.info(f"------< {page_title} > page------")
            except AssertionError:
                allure.attach(self.driver.get_screenshot_as_png(),
                              name=f"Title page assertion error",
                              attachment_type=allure.attachment_type.PNG)
                logging.info("\nCurrent title of page doesn't compare with expected title.\nExpected title: {page_title}\nActual title: {current_page}")
                raise AssertionError(f"\nCurrent title of page doesn't compare with expected title.\nExpected title: {page_title}\nActual title: {current_page}")
            except TimeoutException:
                allure.attach(self.driver.get_screenshot_as_png(),
                              name=f"Title timeout exception",
                              attachment_type=allure.attachment_type.PNG)
                logging.info(f"\nCurrent title of page doesn't compare with expected title.\nExpected title: {page_title}\nActual title: {current_page}")
                raise AssertionError(f"\nCurrent title of page doesn't compare with expected title.\nExpected title: {page_title}\nActual title: {current_page}")
            except Exception as e:
                self.__browser_system_error(e)

    def _move_to_element(self, *selector):
        selector, name = format_selector(*selector)
        with allure.step(f"Check count of elements {name}"):
            logging.info(f"Move to element {name}")
            element = self.__find_element_located(selector, name)
            try:
                ActionChains(self.driver).move_to_element(element).pause(0.5).perform()
            except:
                raise AssertionError

    def _delete_all_cookies_in_local_storage(self):
        with allure.step(f"Delete all cookies in local storage"):
            try:
                logging.info("Delete all cookies in local storage")
                self.driver.execute_script("localStorage.removeItem('some:access_token');")
            except (JavascriptException, WebDriverException):
                return True

    def _get_text(self, *selector):
        selector, name = format_selector(*selector)
        with allure.step(f"Get text from element {name}"):
            element = self.__find_element_located(selector, name)
            try:
                logging.info(f"Get text from element {name}")
                text_value= element.text
                return  text_value
            except Exception as e:
                self.__browser_system_error(e)


    def _count_of_elements(self, count, *selector):
        selector, name = format_selector(*selector)
        with allure.step(f"Check count of < {name} > elements"):
            elements = self.__find_elements_visibility(selector, name)
            try:
                logging.info(f"Check count of < {name} > elements")
                assert len(elements) == int(count)
            except AssertionError:
                logging.info(f"Count value doesn't match with test in element < {name} >.\nActual result: {len(elements)}\nExpected result: {count}")
                raise AssertionError(f"Count value doesn't match with test in element < {name} >.\nActual result: {len(elements)}\nExpected result: {count}")

    def _get_list_elements(self, *selector):
        selector, name = format_selector(*selector)
        with allure.step(f"Get list {name} elements"):
            logging.info(f"Get list {name} elements")
            elements = self.__find_elements_visibility(selector, name)
            return elements

    def _check_attribute_value_in_element(self, text, *selector):
        selector, name = format_selector(*selector)
        with allure.step(f"Check value * {text} * is present in attribute of element < {name} >"):
            element = self.__find_element_located(selector, name)
            try:
                logging.info(f"Check value * {text} * is present in attribute of element < {name} >")
                result = element.get_attribute("value")
                assert text == result
            except TimeoutException:
                self.__timeout_element_error(selector, name)
            except AssertionError:
                self.__element_doesnt_contain_expected_value_error(name, text, result)

    def _table_check_value(self, value, column_name, row_number, column_number):
        TABLE_COLUMN = (By.CSS_SELECTOR, f"div.table-responsive tbody>tr:nth-child({row_number})>td:nth-child({column_number})", f"COLUMN NAME: {column_name}")
        self._check_text_in_element(value, *TABLE_COLUMN)
        return self

    def get_cookies(self):
        logging.info("Get cookies from browser")
        return self.driver.get_cookie()

    def delete_cookies(self):
        logging.info("Delete cookies from browser")
        self.driver.delete_all_cookies()

    def _check_url_of_page(self, expected_url):
        try:
            logging.info(f"Check URL of < {expected_url} > page")
            current_url = WebDriverWait(self.driver, BasePage.timeout).until(EC.url_to_be(expected_url))
        except (AssertionError, TimeoutException) as e:
            logging.error(f"\nYou ARE NOT on expected page: {expected_url}, \nYou are on the page: {current_url}\n {e}")
            raise AssertionError(f"\nYou ARE NOT on expected page: {expected_url}, \nYou are on the page: {current_url}\n {e}")
        except Exception as e:
            self.__browser_system_error(e)

    def _clear_and_input_text(self, text, *selector):
        selector, name = format_selector(*selector)
        with allure.step(f"Input text to element {name}"):
            element = self.__find_element_located(selector, name)
            try:
                logging.info(f"Input text to {name} element")
                element.clear()
                element.send_keys(text)
                return element
            except (NoSuchElementException, TimeoutException):
                self.__timeout_element_error(self, name)
            except Exception as e:
                self.__browser_system_error(e)