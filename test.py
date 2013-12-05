#!/usr/bin/env python
# encoding: utf-8
#
# Copyright © 2013 deanishe@deanishe.net.
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2013-12-05
#

"""
"""

from __future__ import print_function

import sys
import os
import unittest
import unicodedata

import alfred

class AlfredTests(unittest.TestCase):

    _test_filename = 'üöäéøØÜÄÖÉàÀ.l11n'
    _unicode_test_filename = unicode(_test_filename, 'utf-8')

    def setUp(self):
        with open(self._test_filename, u'wb') as file:
            file.write(u'Testing!')

    def tearDown(self):
        if os.path.exists(self._test_filename):
            os.unlink(self._test_filename)

    def test_unicode_normalisation(self):
        """Ensure args are normalised in line with filesystem names"""
        self.assert_(os.path.exists(self._test_filename))
        filenames = [f for f in os.listdir(u'.') if f.endswith('.l11n')]
        self.assert_(len(filenames) == 1)
        print(u'{!r}'.format(filenames))
        fs_filename = filenames[0]
        self.assert_(fs_filename != self._test_filename)  # path has been NFD normalised by filesystem
        alfred_filename = alfred.decode(self._test_filename)
        self.assert_(alfred_filename == fs_filename)


if __name__ == u'__main__':
    unittest.main()
