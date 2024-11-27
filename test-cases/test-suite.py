import unittest
import HtmlTestRunner
from test_login import TestLogin
from test_register import TestRegister
from test_admin import TestAdmin
import os
from datetime import datetime

def suite():
    test_suite = unittest.TestSuite()
    ##
    test_suite.addTest(TestRegister('test_elements_present_on_register_page'))
    test_suite.addTest(TestRegister('test_missing_required_fields'))
    test_suite.addTest(TestRegister('test_invalid_email'))
    test_suite.addTest(TestRegister('test_password_mismatch'))
    test_suite.addTest(TestRegister('test_weak_password'))
    test_suite.addTest(TestRegister('test_valid_registration'))
    ##
    test_suite.addTest(TestLogin('test_elements_present_on_login_page'))
    test_suite.addTest(TestLogin('test_missing_required_fields'))
    test_suite.addTest(TestLogin('test_missing_password_fields'))
    test_suite.addTest(TestLogin('test_login_incorrect_password'))
    test_suite.addTest(TestLogin('test_login_successfully'))
    ##
    test_suite.addTest(TestAdmin('test_add_danhmuc_with_exist_name'))
    test_suite.addTest(TestAdmin('test_add_danhmuc_with_not_exist_name'))
    test_suite.addTest(TestAdmin('test_edit_danh_muc'))
    test_suite.addTest(TestAdmin('test_delete_danh_muc'))
    ##
    return test_suite

if __name__ == "__main__":
    current_time = datetime.now().strftime("%d-%m-%Y %H-%M")
    report_folder = f"reports_{current_time}"
    if not os.path.exists(report_folder):
        os.makedirs(report_folder)

    runner = HtmlTestRunner.HTMLTestRunner(output=report_folder, report_name="test_suite_report", verbosity=2)
    runner.run(suite())
