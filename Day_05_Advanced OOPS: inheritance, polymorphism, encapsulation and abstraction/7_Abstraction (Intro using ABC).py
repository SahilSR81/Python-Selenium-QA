# Abstraction using abstract base class

from abc import ABC, abstractmethod


class Browser(ABC):

    @abstractmethod
    def launch(self):
        pass


class ChromeBrowser(Browser):
    def launch(self):
        print("Launching Chrome browser")


chrome = ChromeBrowser()
chrome.launch()

# Output:
# Launching Chrome browser

