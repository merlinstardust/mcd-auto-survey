import sys
from time import sleep
from selenium import webdriver

ff = webdriver.Firefox()
ff.get('http://www.mcdvoice.com/')

def css(selector, element=ff):
    elements = element.find_elements_by_css_selector(selector)
    if len(elements) == 1:
        elements = elements[0]
    return elements

def click(elements):
    if type(elements) != list:
        elements = [elements]
    for element in elements:
        element.click()

def nxt():
    next_button = css('#NextButton')
    sleep(1)
    next_button.click()

def start():
    store_input = css('#InputStoreID')
    ks_input = css('#InputRegisterNum')
    date_input = css('.ui-datepicker-trigger')
    date_picker = css('#ui-datepicker-div')
    hour_input = css('#InputHour')
    minute_input = css('#InputMinute')
    order_input = css('#InputTransactionNum')
    dollar_input = css('#AmountSpent1')
    cents_input = css('#AmountSpent2')
    age_input = css('#Index_AgeVerification')

    store = sys.argv[1]
    ks = sys.argv[2]
    day = sys.argv[3]
    hour = sys.argv[4]
    minute = sys.argv[5]
    order = sys.argv[6]
    dollar = sys.argv[7]
    cents = sys.argv[8]

    store_input.send_keys(store)
    ks_input.send_keys(ks)
    date_input.click()
    date_picker.find_element_by_link_text(day).click()
    css('[value="' + hour + '"]', hour_input).click()
    css('[value="' + minute + '"]', minute_input).click()
    order_input.send_keys(order)
    dollar_input.send_keys(dollar)
    cents_input.send_keys(cents)
    css('[value="1"]', age_input).click()
    nxt()

def confirm():
    css('.Opt1 span').click()
    nxt()

def order_type():
    css('.Opt3 span span').click()
    nxt()

def satisfactions():
    click(css('.Opt3 span'))
    nxt()

def problem():
    css('.Opt2 span').click()
    nxt()

def explain():
    nxt()

def special_request():
    css('.Opt2 span span').click()
    nxt()

def specific_food():
    left_column = css('.LeftColumn')
    if left_column:
        css('.Opt2 span').click()
        nxt()

def food_type():
    css('.Opt2 span span').click()
    nxt()

def people_and_visits():
    click(css('.Opt1 span span'))
    nxt()

def learn_about():
    css('.Opt3 span span').click()
    nxt()

def primary_reason():
    css('.Opt6 span span').click()
    nxt()

def where_from():
    css('.Opt1 span span').click()
    nxt()

def where_to():
    css('.Opt1 span span').click()
    nxt()

if __name__ == '__main__':
    start()
    confirm()
    order_type()
    satisfactions()
    satisfactions()
    satisfactions()
    satisfactions()
    problem()
    satisfactions()
    explain()
    special_request()
    specific_food()
    food_type()
    people_and_visits()
    if len(sys.argv) == 10:
        primary_reason()
        where_from()
        where_to()
    learn_about()
    satisfactions()

# Arguments
#    store = sys.argv[1]
#    ks = sys.argv[2]
#    day = sys.argv[3]
#    hour = sys.argv[4]
#    minute = sys.argv[5]
#    order = sys.argv[6]
#    dollar = sys.argv[7]
#    cents = sys.argv[8]
