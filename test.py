import unittest
import passwd

# Len config
rule_len_equals = [('LEN', '=', 10)]
rule_len_lower = "[('LEN', '<', 10)]"
rule_len_upper = "[('LEN', '>', 10)]"
pass_len_equals = "CadenceDev"
pass_len_lower = "Cadence"
pass_len_upper = "CadenceDevOps21*"

# Letters config
rule_letter_equals = "[('LETTERS', '=', 10)]"
rule_letter_lower = "[('LETTERS', '<', 10)]"
rule_letter_upper = "[('LETTERS', '>', 10)]"
pass_letter_equals = "CadenceDev321654*="
pass_letter_lower = "Cadence2156156**"
pass_letter_upper = "CadenceDevOps21*"

# Numbers config
rule_numbers_equals = "[('NUMBERS', '=', 8)]"
rule_numbers_lower = "[('NUMBERS', '<', 8)]"
rule_numbers_upper = "[('NUMBERS', '>', 8)]"
pass_numbers_equals = "12345678asdf*="
pass_numbers_lower = "cadence123456**/dsf"
pass_numbers_upper = "12345678910*"

# Specials config
rule_specials_equals = "[('SPECIALS', '=', 3)]"
rule_specials_lower = "[('SPECIALS', '<', 3)]"
rule_specials_upper = "[('SPECIALS', '>', 3)]"
pass_specials_equals = "1234DAS5678asdf*=@"
pass_specials_lower = "cadence123456*dsf"
pass_specials_upper = "12345678910*&$#_"

# all config
rule_all_equals = "[('LEN', '=', 15),('LETTERS', '=', 7),('NUMBERS', '=', 5),('SPECIALS', '=', 3)]"
rule_all_lower = "[('LEN', '<', 15),('LETTERS', '<', 7),('NUMBERS', '<', 5),('SPECIALS', '<', 3)]"
rule_all_upper = "[('LEN', '>', 15),('LETTERS', '>', 7),('NUMBERS', '>', 5),('SPECIALS', '>', 3)]"
pass_all_equals = "AbCde123$Fg@12*"
pass_all_lower = "ACde12Fg@12*"
pass_all_upper = "AbCde123$FgH@123*_"


class TestPwd(unittest.TestCase):

    def test_len(self):
        # Len equals
        self.assertEqual(passwd.main(pass_len_equals, rule_len_equals), True, "Len equals failed")
        self.assertEqual(passwd.main(pass_len_lower, rule_len_equals), False, "Len equals failed")
        self.assertEqual(passwd.main(pass_len_upper, rule_len_equals), False, "Len equals failed")

        # Len lower
        self.assertEqual(passwd.main(pass_len_equals, rule_len_lower), False, "Len lower failed")
        self.assertEqual(passwd.main(pass_len_lower, rule_len_lower), True, "Len lower failed")
        self.assertEqual(passwd.main(pass_len_upper, rule_len_lower), False, "Len lower failed")

        # Len Upper
        self.assertEqual(passwd.main(pass_len_equals, rule_len_upper), False, "Len upper failed")
        self.assertEqual(passwd.main(pass_len_lower, rule_len_upper), False, "Len upper failed")
        self.assertEqual(passwd.main(pass_len_upper, rule_len_upper), True, "Len upper failed")

    def test_letters(self):
        # letter equals
        self.assertEqual(passwd.main(pass_letter_equals, rule_letter_equals), True, "letter equals failed")
        self.assertEqual(passwd.main(pass_letter_lower, rule_letter_equals), False, "letter equals failed")
        self.assertEqual(passwd.main(pass_letter_upper, rule_letter_equals), False, "letter equals failed")

        # letter lower
        self.assertEqual(passwd.main(pass_letter_equals, rule_letter_lower), False, "letter lower failed")
        self.assertEqual(passwd.main(pass_letter_lower, rule_letter_lower), True, "letter lower failed")
        self.assertEqual(passwd.main(pass_letter_upper, rule_letter_lower), False, "letter lower failed")

        # letter Upper
        self.assertEqual(passwd.main(pass_letter_equals, rule_letter_upper), False, "letter upper failed")
        self.assertEqual(passwd.main(pass_letter_lower, rule_letter_upper), False, "letter upper failed")
        self.assertEqual(passwd.main(pass_letter_upper, rule_letter_upper), True, "letter upper failed")

    def test_numbers(self):
        # numbers equals
        self.assertEqual(passwd.main(pass_numbers_equals, rule_numbers_equals), True, "numbers equals failed")
        self.assertEqual(passwd.main(pass_numbers_lower, rule_numbers_equals), False, "numbers equals failed")
        self.assertEqual(passwd.main(pass_numbers_upper, rule_numbers_equals), False, "numbers equals failed")

        # numbers lower
        self.assertEqual(passwd.main(pass_numbers_equals, rule_numbers_lower), False, "numbers lower failed")
        self.assertEqual(passwd.main(pass_numbers_lower, rule_numbers_lower), True, "numbers lower failed")
        self.assertEqual(passwd.main(pass_numbers_upper, rule_numbers_lower), False, "numbers lower failed")

        # numbers Upper
        self.assertEqual(passwd.main(pass_numbers_equals, rule_numbers_upper), False, "numbers upper failed")
        self.assertEqual(passwd.main(pass_numbers_lower, rule_numbers_upper), False, "numbers upper failed")
        self.assertEqual(passwd.main(pass_numbers_upper, rule_numbers_upper), True, "numbers upper failed")

    def test_specials(self):
        # specials equals
        self.assertEqual(passwd.main(pass_specials_equals, rule_specials_equals), True, "specials equals failed")
        self.assertEqual(passwd.main(pass_specials_lower, rule_specials_equals), False, "specials equals failed")
        self.assertEqual(passwd.main(pass_specials_upper, rule_specials_equals), False, "specials equals failed")

        # specials lower
        self.assertEqual(passwd.main(pass_specials_equals, rule_specials_lower), False, "specials lower failed")
        self.assertEqual(passwd.main(pass_specials_lower, rule_specials_lower), True, "specials lower failed")
        self.assertEqual(passwd.main(pass_specials_upper, rule_specials_lower), False, "specials lower failed")

        # specials Upper
        self.assertEqual(passwd.main(pass_specials_equals, rule_specials_upper), False, "specials upper failed")
        self.assertEqual(passwd.main(pass_specials_lower, rule_specials_upper), False, "specials upper failed")
        self.assertEqual(passwd.main(pass_specials_upper, rule_specials_upper), True, "specials upper failed")

    def test_all(self):
        # all equals
        self.assertEqual(passwd.main(pass_all_equals, rule_all_equals), True, "all equals failed")
        self.assertEqual(passwd.main(pass_all_lower, rule_all_equals), False, "all equals failed")
        self.assertEqual(passwd.main(pass_all_upper, rule_all_equals), False, "all equals failed")

        # all lower
        self.assertEqual(passwd.main(pass_all_equals, rule_all_lower), False, "all lower failed")
        self.assertEqual(passwd.main(pass_all_lower, rule_all_lower), True, "all lower failed")
        self.assertEqual(passwd.main(pass_all_upper, rule_all_lower), False, "all lower failed")

        # all Upper
        self.assertEqual(passwd.main(pass_all_equals, rule_all_upper), False, "all upper failed")
        self.assertEqual(passwd.main(pass_all_lower, rule_all_upper), False, "all upper failed")
        self.assertEqual(passwd.main(pass_all_upper, rule_all_upper), True, "all upper failed")


if __name__ == '__main__':
    unittest.main()
