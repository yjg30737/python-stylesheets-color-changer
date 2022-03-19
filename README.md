# python-stylesheets-color-changer
Python CSS style sheets color changer

Currently the only feature of this is changing the brightness of color of CSS style sheets.

## Setup
```pip3 install git+https://github.com/yjg30737/python-stylesheets-color-changer.git --upgrade```

## Included Packages
* <a href="https://github.com/yjg30737/python-color-getter.git">python-color-getter</a>

## Class/Method Overview
* ```StyleSheetsColorChanger(stylesheets: str)``` - Constructor. ```stylesheets``` argument accepts the raw css code.
* ```lighter() -> str``` - Make colors lighter. #DDD -> #EEE. Return the raw css code which is lighter than the original.
* ```darker() -> str``` - Make colors darker. #EEE -> #DDD. Return the raw css code which is darker than the original.

## Example
Example application is <a href="https://github.com/yjg30737/pyqt-dark-calculator.git">pyqt-dark-calculator</a>.

Original

![image](https://user-images.githubusercontent.com/55078043/159101467-1698eeca-5e8f-4a1e-90ff-1aa529fa5200.png)

I'll make this darker.

Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_dark_calculator import Calculator
from python_stylesheets_color_changer import StyleSheetsColorChanger


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    calculator = Calculator()
    changer = StyleSheetsColorChanger('darkGrayTheme.css')
    css_code = changer.darker()
    calculator.setStyleSheet(css_code)
    calculator.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/159101495-21db5f75-275e-4d0c-86e4-a22a6b2fe7ff.png)

How about make it lighter?

![image](https://user-images.githubusercontent.com/55078043/159101542-14cb81c8-93b8-4777-88ce-ace894179561.png)









