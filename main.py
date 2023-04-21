import time


def test_dynamic_id(page):
    page.goto("http://uitestingplayground.com/")
    page.click("text=Dynamic ID")
    dynamic_button = page.query_selector('.btn-primary')
    button_id = dynamic_button.get_attribute('id')
    page.reload()
    dynamic_button_reload = page.query_selector('.btn-primary')
    button_reload_id = dynamic_button_reload.get_attribute('id')
    assert button_reload_id != button_id


def test_hidden_layers(page):
    page.goto("http://uitestingplayground.com/")
    page.click("text=Hidden Layers")
    green_button = page.wait_for_selector(".btn-success")
    green_button.click()
    page.click('.btn-primary')
    assert True


def test_text_input(page):
    page.goto("http://uitestingplayground.com/")
    page.click("text=Text Input")
    text = page.query_selector("#newButtonName")
    text.type('test123', delay=100)
    button = page.locator('#updatingButton')
    button.click()
    button_text = button.text_content()
    assert button_text == 'test123'


def test_load_delay(page):
    page.goto("http://uitestingplayground.com/")
    page.click("text=Load Delay")
    page.wait_for_url("http://uitestingplayground.com/loaddelay")
    assert page.url == 'http://uitestingplayground.com/loaddelay'


def test_ajax_data(page):
    page.goto("http://uitestingplayground.com/")
    page.click("text=Ajax Data")
    button = page.wait_for_selector(".btn-primary")
    button.click()
    element = page.wait_for_selector(".bg-success")
    assert element.text_content() == 'Data loaded with AJAX get request.'


def test_client_side_delay(page):
    page.goto("http://uitestingplayground.com/")
    page.click("text=Client Side Delay")
    button = page.wait_for_selector(".btn-primary")
    button.click()
    element = page.wait_for_selector(".bg-success")
    assert element.text_content() == 'Data calculated on the client side.'