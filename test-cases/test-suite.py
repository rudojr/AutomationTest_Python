import unittest
import HtmlTestRunner
from test_login import TestLogin
from test_register import TestRegister

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLogin))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestRegister))
    return test_suite

if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(output="reports", report_name="test_suite_report", verbosity=2)
    runner.run(suite())
