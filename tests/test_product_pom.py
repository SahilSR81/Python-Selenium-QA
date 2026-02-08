def test_add_product_to_cart(driver):
    from pages.login_page import LoginPage
    from pages.product_page import ProductPage

    login = LoginPage(driver)
    product = ProductPage(driver)

    login.login("standard_user", "secret_sauce")

    product.add_first_product_to_cart()
    assert product.is_product_added_to_cart()
