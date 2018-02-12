from unittest import TestCase
import camel.camel as camel


class TestCamelCase(TestCase):

    def test_a_normal_string(self):
        self.assertEqual("thisIsCamelCase", camel.ify("This is Camel case"))

    def test_a_string_with_punctuation(self):
        self.assertEqual("lo!ThisIsCamelCase,Yo.", camel.ify("Lo! This is Camel case, Yo."))

    def test_a_string_with_weird_spacing(self):
        self.assertEqual("twasBrilligAndTheSlithyToves", camel.ify("Twas brillig  and   the    slithy     toves"))


