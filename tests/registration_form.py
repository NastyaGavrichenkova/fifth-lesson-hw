import os
from selene.support.shared import browser
from selene import be, have


def test_successful_registration():
    browser.open("/automation-practice-form")
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')

    browser.element('#firstName').should(be.blank).type("leia")
    browser.element('#lastName').should(be.blank).type("organa")
    browser.element('#userEmail').should(be.blank).type("leia@gmail.com")
    browser.element('[for=gender-radio-2]').click()
    browser.element('#userNumber').should(be.blank).type("0123456789")

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select [value = "4"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element(".react-datepicker__year-select>option[value='1977']").click()
    browser.element('.react-datepicker__day--025').click()

    browser.element('#subjectsInput').should(be.blank).type("english").press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element("#uploadPicture").send_keys(os.path.abspath("resources/image_test.JPG"))
    browser.element('#currentAddress').should(be.blank).type("1 RIDGE AVE SUFFERN NY 10901-5807 USA")
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    browser.element('#submit').click()

    browser.element('.table-responsive').should(have.text('leia organa' and
                                                          'leia@gmail.com' and
                                                          'Female' and
                                                          '0123456789' and
                                                          '25 May 1977' and
                                                          'English' and
                                                          'Reading' and
                                                          'image_test.JPG' and
                                                          '1 RIDGE AVE SUFFERN NY 10901-5807 USA' and
                                                          'NCR' and
                                                          'Delhi'
                                                          ))
