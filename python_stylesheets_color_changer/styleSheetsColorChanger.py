import os.path
import re

from python_color_getter import PythonColorGetter


class StyleSheetsColorChanger:
    def __init__(self, css: str):
        self.__css_code = ''
        if os.path.isfile(css):
            f = open(css, 'r')
            self.__css_code = f.read()
            f.close()
        else:
            self.__css_code = css

    def lighter(self):
        original_color_lst, original_color_span_lst, replaced_color_lst = self.__change_brightness()
        self.__replace_color(replaced_color_lst, original_color_span_lst)

        return self.__css_code

    def darker(self):
        original_color_lst, original_color_span_lst, replaced_color_lst = self.__change_brightness(lighter=False)
        self.__replace_color(replaced_color_lst, original_color_span_lst)

        return self.__css_code

    def __change_brightness(self, lighter: bool = True):
        original_color_lst = []
        original_color_span_lst = []
        replaced_color_lst = []

        color_iter = re.finditer(r'#\w+', self.__css_code)
        for color_match_obj in color_iter:
            original_color_text = color_match_obj.group(0)
            original_color_lst.append(original_color_text)
            original_color_span_lst.append(color_match_obj.span(0))
            r, g, b = PythonColorGetter.hex_to_rgb(original_color_text)
            if lighter:
                r, g, b = PythonColorGetter.lighter(r, g, b)
            else:
                r, g, b = PythonColorGetter.darker(r, g, b)
            replaced_color_text = PythonColorGetter.rgb_to_hex(r, g, b, len(original_color_text)-1)
            replaced_color_lst.append(replaced_color_text)
        return original_color_lst, original_color_span_lst, replaced_color_lst

    def __replace_color(self, replaced_color_lst, original_color_span_lst):
        for i in range(len(replaced_color_lst)):
            start_idx, end_idx = original_color_span_lst[i]
            self.__css_code = self.__css_code[:start_idx] + replaced_color_lst[i] + self.__css_code[end_idx:]

