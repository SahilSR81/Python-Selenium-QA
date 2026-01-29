from utils.browser_runner import run_on_all_browsers
from utils.wait_utils import wait_visible
from selenium.webdriver.common.by import By


def drag_drop_test(driver):
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")

    source = wait_visible(driver, (By.ID, "column-a"))
    target = wait_visible(driver, (By.ID, "column-b"))

    driver.execute_script(
        """
        function dragAndDrop(source, target) {
            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', {
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('drop', {
                dataTransfer: dataTransfer
            }));

            source.dispatchEvent(new DragEvent('dragend', {
                dataTransfer: dataTransfer
            }));
        }
        dragAndDrop(arguments[0], arguments[1]);
    """,
        source,
        target,
    )

    assert source.text == "B", "Drag and drop failed"


def test_drag_drop():
    run_on_all_browsers(drag_drop_test)


if __name__ == "__main__":
    test_drag_drop()
    print("All tests passed.")
