"""
Test Suite for anagrams module. 
Students should only modify only the `test_long` method.
"""
__author__ = "madarp"

import sys
import unittest
import importlib
import timeit
import json
import functools
import subprocess

# suppress __pycache__ and .pyc files
sys.dont_write_bytecode = True

# Kenzie devs: change this to 'soln.anagrams' to test solution
PKG_NAME = 'anagrams'


class TestAnagrams(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime"""
        cls.assertGreaterEqual(cls, sys.version_info[0], 3)
        cls.module = importlib.import_module(PKG_NAME)

    def run_find_anagrams(self, word_list, benchmark):
        """Helper func to time the find_anagrams() func"""
        f = functools.partial(self.module.find_anagrams, word_list)
        t = timeit.Timer(f)
        actual_time = round(t.timeit(number=1), 3)
        failure_text = (
            f'\nfind_anagrams() took {actual_time:.03f} seconds, which exceeds the '
            f'benchmark of {benchmark:.03f} seconds'
            )
        self.assertLessEqual(actual_time, benchmark, failure_text)

    def test_correct_result(self):
        """Check the anagram dict result for correctness"""
        with open("words/short.txt") as f:
            short_list = f.read().split()
        actual_dict = self.module.find_anagrams(short_list)
        self.assertIsInstance(actual_dict, dict)
        with open('tests/short_list.json') as f:
            expected_dict = json.loads(f.read())
        self.assertDictEqual(actual_dict, expected_dict)

    def test_short(self):
        """Check find_anagrams() func timing with short word list."""
        with open("words/short.txt") as f:
            short_list = f.read().split()
        self.run_find_anagrams(short_list, 0.030)

    #
    # Students:  Comment out the line below to enable the long test.
    #
    @unittest.skip("Remove this line once short test passes")
    def test_long(self):
        """Check find_anagrams() with long word list."""
        with open("words/long.txt") as f:
            long_list = f.read().split()
        self.run_find_anagrams(long_list, 0.500)

    def test_flake8(self):
        """Checking for PEP8/flake8 compliance"""
        result = subprocess.run(['flake8', self.module.__file__])
        self.assertEqual(result.returncode, 0)

    def test_author_string(self):
        """Checking for author string"""
        self.assertIsNotNone(self.module.__author__)
        self.assertNotEqual(
            self.module.__author__, "???",
            "Author string is not completed"
            )


if __name__ == '__main__':
    unittest.main()
