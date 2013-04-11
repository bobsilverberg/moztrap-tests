#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from unittestzero import Assert

from pages.home_page import MozTrapHomePage
from pages.base_test import BaseTest


class TestHomepage(BaseTest):

    @pytest.mark.moztrap([3385, 3386])
    @pytest.mark.nondestructive
    def test_that_user_can_login_and_logout(self, mozwebqa):
        from pages.login_page import MozTrapLoginPage
        login_pg = MozTrapLoginPage(mozwebqa)
        home_pg = MozTrapHomePage(mozwebqa)

        home_pg.get_relative_path('/')

        Assert.false(home_pg.header.is_user_logged_in)

        login_pg.go_to_login_page()
        login_pg.login()

        user = home_pg.testsetup.credentials['default']
        users_name = user['name']

        Assert.true(home_pg.header.is_user_logged_in)
        Assert.equal(home_pg.header.username_text, users_name)

        home_pg.header.click_logout()
        home_pg.get_relative_path('/')

        Assert.false(home_pg.header.is_user_logged_in)

    @pytest.mark.moztrap(3387)
    def test_that_user_can_select_product(self, mozwebqa_logged_in, product):
        home_pg = MozTrapHomePage(mozwebqa_logged_in)

        home_pg.go_to_home_page()

        Assert.false(home_pg.is_product_version_visible(product))

        home_pg.select_item(product['name'])

        Assert.true(home_pg.is_product_version_visible(product))

    @pytest.mark.moztrap(3388)
    def test_that_user_can_select_version(self, mozwebqa_logged_in, product):
        home_pg = MozTrapHomePage(mozwebqa_logged_in)

        run = self.create_run(mozwebqa_logged_in, product=product, activate=True)

        home_pg.go_to_home_page()
        home_pg.select_item(run['version']['product']['name'])

        Assert.false(home_pg.is_element_visible(*run['homepage_locator']))

        home_pg.select_item(run['version']['name'])

        Assert.true(home_pg.is_element_visible(*run['homepage_locator']))

    @pytest.mark.moztrap(3414)
    def test_that_user_can_select_run(self, mozwebqa_logged_in, product):
        home_pg = MozTrapHomePage(mozwebqa_logged_in)

        run = self.create_run(mozwebqa_logged_in, product=product, activate=True)

        home_pg.go_to_home_page()
        home_pg.select_item(run['version']['product']['name'])
        home_pg.select_item(run['version']['name'])

        Assert.false(home_pg.is_element_visible(*run['run_tests_locator']))

        home_pg.select_item(run['name'])

        Assert.true(home_pg.is_element_visible(*run['run_tests_locator']))
