from playwright.sync_api import Page, expect
import logging


def test_store(page: Page):
    urls = ['https://www.ferittyshop.com/']
    error_urls = []
    for url in urls:
        try:
            # 打开页面
            page.goto(url)
            # 判断判断是否是shopline店铺
            if not is_shopline_store(page):  # 作为shopify店铺处理
                shopify_store_test(page)
            # TODO shopline店铺处理
        except Exception as e:
            logging.error(e)
            error_urls.append(url)
            continue


def shopify_store_test(page):
    """
    测试shopify店铺
    :param page:
    :return:
    """
    # 定位商品标题
    locate_title(page)
    # 跳转详情页点击购买
    locate_buy_button(page)
    # 定位三个必填表单
    information_form, shipping_form, payment_form = locate_forms(page)
    # 填写表单并提交
    filling_forms(information_form, shipping_form, payment_form)


def is_shopline_store(page):
    shopline_header = page.locator('shopline-section-header')
    return shopline_header.count() > 0


def locate_title(page):
    """
    打开店铺首页
    """
    try:
        # 定位商品标题
        title = page.locator('[data-product-item-title]').first
        expect(title).not_to_be_empty(3000)
        # 点击商品标题
        title.click()
    except AssertionError as e:
        logging.error(f"{page.url}  没有定位到商品标题")
        raise AssertionError(e)


def locate_buy_button(page):
    """
    跳转详情页购买
    """
    try:
        # 定位商品详情页的购买按钮
        buy_button = page.locator('[data-product-bn]')
        expect(buy_button).not_to_be_empty(3000)
        # 点击购买按钮
        buy_button.click()
    except AssertionError as e:
        logging.error(f"{page.url} 没有定位到购买按钮")
        raise AssertionError(e)


def add_to_cart(page):
    """
    跳转详情页添加购物车
    """
    try:
        # 定位商品详情页的加入购物车按钮
        cart = page.locator('[data-product-atc]')
        expect(cart).not_to_be_empty(3000)
        # 点击加入购物车按钮
        cart.click()
    except AssertionError as e:
        logging.error(f"{page.url} 没有定位到购物车按钮")
        raise AssertionError(e)


def locate_forms(page):
    """
        填写个人信息
    """
    try:
        forms = page.locator('.information-edit')
        expect(forms).not_to_be_empty(timeout=3000)

        information_form = None
        shipping_form = None
        payment_form = None
        if len(forms) == 3:
            information_form = forms[0]
            shipping_form = forms[1]
            payment_form = forms[2]
        elif len(forms) == 4:
            information_form = forms[0]
            shipping_form = forms[1]
            payment_form = forms[3]
        return information_form, shipping_form, payment_form
    except AssertionError as e:
        logging.error(f"{page.url} 没有定位到表单, 可能不是shopify店铺")
        raise AssertionError(e)


def filling_forms(information_form, shipping_form, payment_form):
    """
    填写表单

    :param information_form: 个人信息表单
    :param shipping_form: 快递表单
    :param payment_form: 支付表单
    :return:
    """
    # 根据Button是否可见以区分是否是分步表单
    continue_to_shipping_button = information_form.locator('button')
    continue_to_payment_button = shipping_form.locator('button')
    complete_order_button = payment_form.locator('button')
    # 开始填表单
    filling_information_form(information_form)
    if continue_to_shipping_button.is_visible():
        continue_to_shipping_button.click()
    filling_shipping_form(shipping_form)
    if continue_to_payment_button.is_visible():
        continue_to_payment_button.click()
    filling_payment_form(payment_form)
    # 提交订单
    complete_order_button.click()


def filling_information_form(information_form):
    """
    填写个人信息表单
    :param information_form:
    :return:
    """


def filling_shipping_form(shipping_form):
    """
    选择运输方式
    :param shipping_form:
    :return:
    """


def filling_payment_form(payment_form):
    """
    选择Pacypay支付
    :param payment_form:
    :return:
    """
