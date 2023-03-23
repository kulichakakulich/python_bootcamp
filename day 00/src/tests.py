import io
import os
import sys
import unittest
import decypher
import mfinder


class TestBlocks(unittest.TestCase):
    def test_valid_blocks_lines(self):
        input_data = "00000254b208c0f43409d8dc00439896\n0000085a34260d1c84e89865c210ceb4\n"
        expected_output = "00000254b208c0f43409d8dc00439896\n0000085a34260d1c84e89865c210ceb4\n"
        sys.stdin = io.StringIO(input_data)
        output = io.StringIO()
        sys.stdout = output
        with open("blocks.py") as f:
            exec(f.read())
        self.assertEqual(output.getvalue(), expected_output)

    def test_invalid_blocks_lines(self):
        input_data = "00000254b208c0f43409d8dc00439896\n0000085a34260d1c84e89865c210ceb4\n00000000001234567890123456789012\n00000678\n0000000\n12345678901234567890123456789012\n"
        expected_output = "00000254b208c0f43409d8dc00439896\n0000085a34260d1c84e89865c210ceb4\n"
        sys.stdin = io.StringIO(input_data)
        output = io.StringIO()
        sys.stdout = output
        with open("blocks.py") as f:
            exec(f.read())
        self.assertEqual(output.getvalue(), expected_output)

    def test_argument_blocks(self):
        input_data = "00000254b208c0f43409d8dc00439896\n0000085a34260d1c84e89865c210ceb4\n0000071f49cffeaea4184be3d507086v\n"
        expected_output = "00000254b208c0f43409d8dc00439896\n0000085a34260d1c84e89865c210ceb4\n"
        sys.stdin = io.StringIO(input_data)
        output = io.StringIO()
        sys.stdout = output
        sys.argv = ["blocks.py", "2"]
        with open("blocks.py") as f:
            exec(f.read())
        self.assertEqual(output.getvalue(), expected_output)

    def test_valid_decypher_1(self):
        input_data = "The only way everyone reaches Brenda rapidly is delivering groceries explicitly"
        expected_output = "TowerBridge"
        result = decypher.decypher(input_data)
        self.assertEqual(result, expected_output)

    def test_valid_decypher_2(self):
        input_data = "Britain is Great because everyone necessitates"
        expected_output = "BiGben"
        result = decypher.decypher(input_data)
        self.assertEqual(result, expected_output)

    def test_valid_decypher_3(self):
        input_data = "Have you delivered eggplant pizza at restored keep?"
        expected_output = "Hydepark"
        result = decypher.decypher(input_data)
        self.assertEqual(result, expected_output)

    def test_valid_image(self):
        with open('valid_image.txt', 'w') as f:
            f.write('*gxa*\n**w**\n*s*m*')
        result = mfinder.read_input('valid_image.txt')
        self.assertTrue(mfinder.check_pattern(result))
        os.remove('valid_image.txt')

    def test_invalid_image(self):
        with open('invalid_image.txt', 'w') as f:
            f.write('*****\n*****\n*****')
        result = mfinder.read_input('invalid_image.txt')
        self.assertFalse(mfinder.check_pattern(result))
        os.remove('invalid_image.txt')

    def test_partial_asterisks(self):
        with open('partial_asterisks.txt', 'w') as f:
            f.write('*s*f*\n**f**\n*a***')
        result = mfinder.read_input('partial_asterisks.txt')
        self.assertFalse(mfinder.check_pattern(result))
        os.remove('partial_asterisks.txt')

    def test_incorrect_size(self):
        with open('incorrect_size.txt', 'w') as f:
            f.write('*gxa*\n**w**\n*s*\n*m*')
        self.assertEqual(mfinder.read_input(
            'incorrect_size.txt'), None)
        os.remove('incorrect_size.txt')


if __name__ == '__main__':
    unittest.main()
