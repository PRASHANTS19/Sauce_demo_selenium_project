from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser_name = "chrome"
def browser():
    if browser_name.lower() == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")  # Maximize window
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    elif browser_name.lower() == "ie":
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument("--start-maximized")
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")  # Maximize window
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
