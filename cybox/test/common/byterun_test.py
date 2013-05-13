import unittest

from cybox.common import Hash
from cybox.common.byterun import ByteRun, ByteRuns
import cybox.test


class TestByteRun(unittest.TestCase):

    def test_round_trip(self):
        byterun_dict = {
                        'offset': 1000,
                        'file_system_offset': 1024,
                        'image_offset': 512,
                        'length': 10,
                        'hashes': [{'type': Hash.TYPE_MD5,
                                    'simple_hash_value':
                                        '0123456789abcdef0123456789abcdef'}],
                        'byte_run_data': "helloworld",
                       }
        byterun_dict2 = cybox.test.round_trip_dict(ByteRun, byterun_dict)
        self.assertEqual(byterun_dict, byterun_dict2)


class TestByteRuns(unittest.TestCase):

    def test_round_trip(self):
        byteruns_list = [
                        {'byte_run_data': "a",
                         'length': 1},
                        {'byte_run_data': "blahblah",
                         'length': 8},
                        {'byte_run_data': "aeiou",
                         'length': 5},
                      ]
        byteruns_list2 = cybox.test.round_trip_list(ByteRuns, byteruns_list)
        self.assertEqual(byteruns_list, byteruns_list2)

if __name__ == "__main__":
    unittest.main()
