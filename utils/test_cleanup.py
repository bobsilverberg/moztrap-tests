#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from unittestzero import Assert

from pages.utils.product_listing_page import MozTrapAdminProductListingPage
from pages.base_test import BaseTest


class TestCleanup(BaseTest):

    def test_that_is_not_really_a_test_but_instead_cleans_up_the_database(self, mozwebqa_logged_in):
        product_listing_pg = MozTrapAdminProductListingPage(mozwebqa_logged_in)
        product_listing_pg.go_to_product_listing_page()

        products_to_delete = True
        while products_to_delete:
            product_rows = product_listing_pg.product_rows
            for product in product_rows:
                if product.is_testing_product:
                    product.select_checkbox()

            if product_listing_pg.are_products_selected:
                product_listing_pg.select_delete_action()
                product_listing_pg.click_go_button()
                product_listing_pg.click_i_am_sure_button()
                Assert.true(product_listing_pg.was_deletion_successful)
            else:
                products_to_delete = False
