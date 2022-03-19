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
