#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.page import Page
from pages.page import PageRegion


class MozTrapAdminProductListingPage(Page):

    _page_title = 'Select product to change'

    _product_row_locator = (By.CSS_SELECTOR, 'tr[class^="row"]')
    _action_select_delete_locator = (By.CSS_SELECTOR, '#changelist-form option[value="delete_selected"]')
    _go_button_locator = (By.CSS_SELECTOR, '#changelist-form button[type="submit"]')
    _i_am_sure_button_locator = (By.CSS_SELECTOR, 'input[value="Yes, I\'m sure"]')
    _action_counter_locator = (By.CSS_SELECTOR, 'span.action-counter')
    _success_message_locator = (By.CSS_SELECTOR, 'ul.messagelist li.info')

    def go_to_product_listing_page(self):
        self.selenium.get(self.base_url + '/admin/core/product/?o=2')
        self.is_the_current_page

    @property
    def product_rows(self):
        return [self.Product(self.testsetup, web_el) for web_el
                in self.selenium.find_elements(*self._product_row_locator)]

    def select_delete_action(self):
        self.selenium.find_element(*self._action_select_delete_locator).click()

    def click_go_button(self):
        self.selenium.find_element(*self._go_button_locator).click()

    def click_i_am_sure_button(self):
        self.selenium.find_element(*self._i_am_sure_button_locator).click()

    @property
    def are_products_selected(self):
        return '0 of ' not in self.selenium.find_element(*self._action_counter_locator).text

    @property
    def was_deletion_successful(self):
        return 'Successfully' in self.selenium.find_element(*self._success_message_locator).text

    class Product(PageRegion):

        _checkbox_locator = (By.CSS_SELECTOR, 'input')
        _product_name_locator = (By.CSS_SELECTOR, 'a')

        def select_checkbox(self):
            self.find_element(*self._checkbox_locator).click()

        @property
        def is_testing_product(self):
            return 'Test Product ' in self.find_element(*self._product_name_locator).text
