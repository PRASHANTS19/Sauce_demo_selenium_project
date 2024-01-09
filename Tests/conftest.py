import os
from datetime import datetime
import pyautogui
import pytest
import pytest_html
from Tests.cross_browser import browser

path = None
@pytest.fixture(scope="session")
def driver():
    driver = browser()
    now = datetime.now()
    os.chdir(os.path.join(os.getcwd(), '..'))
    os.chdir(os.path.join(os.getcwd(), 'Resource'))
    directory = now.strftime("%d%m%Y%H%M%S") + "_" + "folder"
    path = os.path.join(os.getcwd(), directory)
    os.mkdir(path)
    yield driver, path
    driver.quit()

@pytest.fixture()
def setup(driver):
    driver_instance, path = driver  # Unpack the tuple returned by the 'driver' fixture
    driver_instance.get("https://www.saucedemo.com/")
    return driver_instance, path

def pytest_html_report_title(report):
    report.title = "Automation_report"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("https://www.saucedemo.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            # file_name = os.path.join(os.getcwd(), datetime.now().strftime("%d%m%Y%H%M%S") + "_" +file_name)
            file_name = os.path.join(os.getcwd(),"_" +file_name)
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(f"{file_name}")
            # _capture_screenshot(file_name, item.funcargs['driver'])
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extras.append(pytest_html.extras.html(html))
        report.extras = extras


# def _capture_screenshot(name,driver):
#     driver.save_screenshot(name)