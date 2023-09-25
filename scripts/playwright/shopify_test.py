from playwright.sync_api import Page, expect
import logging


class SiteUtils(object):
    # email, first_name, last_name, address, city, country, state, zip_code, phone
    information_dict = {
        "US": ("abel.wang@onerway.com", "Abel", "Xx", "test address", "test city", "US", "AL", "36003",
               "17771441003"),
    }

    credit_card_dict = {
        "Visa": ("4711100000000000", "05/25", "123", "Abel", "Xxx")
    }

    @staticmethod
    def get_information(country):
        return SiteUtils.information_dict[country]


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
    filling_forms(page, information_form, shipping_form, payment_form)


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
        expect(title).not_to_be_empty(timeout=10000)
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
        expect(buy_button).not_to_be_empty(timeout=10000)
        # 点击购买按钮
        buy_button.click().wait_for_page_load()
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
        expect(cart).not_to_be_empty(timeout=10000)
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

        forms = page.query_selector('.information-edit')
        expect(forms).not_to_be_empty()

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


def filling_forms(page, information_form, shipping_form, payment_form):
    """
    填写表单

    :param page: 当前页面
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
    filling_information_form(page, information_form)
    if continue_to_shipping_button.is_visible():
        continue_to_shipping_button.click()
    filling_shipping_form(shipping_form)
    if continue_to_payment_button.is_visible():
        continue_to_payment_button.click()
    filling_payment_form(payment_form)
    # 提交订单
    complete_order_button.click()


def contains_optional_string(element):
    """
    校验必填字段
    """
    field_placeholder = element.get_attribute('placeholder').lower().strip()
    # 如果field_placeholder包含optional
    if 'optional' in field_placeholder:
        return False
    return True


def filling_information_form(page, information_form):
    """
    填写个人信息表单

    :param page:
    :param information_form:
    :return:
    """

    # 国家key， 根据key选择个人信息
    country_key = "US"
    email, first_name, last_name, address, city, country, state, zip_code, phone = SiteUtils.get_information(
        country_key)

    email_val = 'e-mail'
    first_name_val = 'firstname'
    last_name_val = 'lastname'
    address_val = 'Address'
    city_val = 'city'
    country_val = 'country'
    state_val = 'administrative_area_level_1'
    zip_code_val = 'postal_code'
    phone_val = 'phone'

    # 填写邮箱
    email_field = information_form.locator(f'[name="{email_val}"]')
    if contains_optional_string(email_field):
        logging.error(f"{page.url}  邮箱不是必填")
    email_field.fill(email)

    # 填写first name
    first_name_field = information_form.locator(f'[name="{first_name_val}"]')
    if contains_optional_string(first_name_field):
        logging.error(f"{page.url}  first name不是必填")
    first_name_field.fill(first_name)

    # 填写last name
    last_name_field = information_form.locator(f'[name="{last_name_val}"]')
    if contains_optional_string(last_name_field):
        logging.error(f"{page.url}  last name不是必填")
    last_name_field.fill(last_name)

    # 填写地址
    address_field = information_form.locator(f'[name="{address_val}"]')
    if contains_optional_string(address_field):
        logging.error(f"{page.url}  地址不是必填")
    address_field.fill(address)

    # 填写城市
    city_field = information_form.locator(f'[name="{city_val}"]')
    if contains_optional_string(city_field):
        logging.error(f"{page.url}  城市不是必填")
    city_field.fill(city)

    # 选择国家
    country_field = information_form.locator(f'[name="{country_val}"]')
    if contains_optional_string(country_field):
        logging.error(f"{page.url}  国家不是必填")
    country_field.select_option(value=country)

    # 选择州
    state_field = information_form.locator(f'[name="{state_val}"]')
    if contains_optional_string(state_field):
        logging.error(f"{page.url}  州不是必填")
    state_field.select_option(value=state)

    # 填写邮编
    zip_code_field = information_form.locator(f'[id="{zip_code_val}"]')
    zip_code_field.fill(zip_code)

    # 填写电话
    phone_field = information_form.locator(f'[name="{phone_val}"]')
    if contains_optional_string(phone_field):
        logging.error(f"{page.url}  电话不是必填")
    phone_field.fill(phone)


def fill_in_field(page, information_form):
    # 国家key， 根据key选择个人信息
    country_key = "US"
    email, first_name, last_name, address, city, country, state, zip_code, phone = SiteUtils.get_information(
        country_key)

    # field常量，根据后缀区分定位元素的方式
    field_dict = {
        "email_by_name": "e-mail",
        "first_name_by_name": "firstname",
        "last_name_by_name": "lastname",
        "address_by_name": "Address",
        "city_by_name": "city",
        "country_by_name": "country",
        "state_by_name": "administrative_area_level_1",
        "zip_code_by_id": "postal_code",
        "phone_by_name": "phone"
    }

    # 对应中文
    field_dict_cn = {
        "email_by_name": "邮箱",
        "first_name_by_name": "first name",
        "last_name_by_name": "last name",
        "address_by_name": "地址",
        "city_by_name": "城市",
        "country_by_name": "国家",
        "state_by_name": "州",
        "zip_code_by_id": "邮编",
        "phone_by_name": "电话"
    }

    # 必填字段
    required_field = ['e-mail', 'firstname', 'lastname', 'Address', 'phone']

    for key in field_dict:
        # 根据name定位元素
        if key.endswith('name'):
            element = information_form.locator(f'[name="{field_dict[key]}"]')
            # 如果是国家和次级行政区域，需要选择对应的值
            if key == 'country_by_name':
                element.select_option(label=country)
            elif key == 'state_by_name':
                element.select_option(label=state)
                # 其他字段需要填充
            if contains_optional_string(element):
                logging.error(f"{page.url}  {field_dict_cn[key]}不是必填")
                element.fill()
        # 根据id定位元素
        elif key.endswith('id'):
            element = information_form.locator(f'[id="{field_dict[key]}"]')
            if contains_optional_string(element):
                logging.error(f"{page.url}  {field_dict_cn[key]}不是必填")


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
