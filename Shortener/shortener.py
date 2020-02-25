import random
import string
from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)
code_char=string.ascii_lowercase + string.digits

class Shortener:

    def code_generator():

        new_code = ''
        for i in range(SHORTCODE_MIN):
            new_code += random.choice(code_char)
        return  new_code