from selene import browser, be, have



def test_find_selene():
    browser.open("https://google.com")
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_find_wrong():
    browser.open("https://google.com")
    browser.element('[name="q"]').should(be.blank).type('fghfghdjkghkdujh').press_enter()
    browser.element('[id="search"]').should(have.text('Похоже, по вашему запросу нет полезных результатов'))
