import io
import unittest
import time
import typedbytes



class TestSpeed(unittest.TestCase):

    def testints(self):
        file = io.BytesIO()

        output = typedbytes.Output(file)
        t = time.time()
        output.writes(range(100000))
        print(time.time() - t)

        file.seek(0)

        input = typedbytes.Input(file)
        t = time.time()
        for record in input:
            pass
        print(time.time() -t)

        file.close()

    def teststrings(self):
        file = io.BytesIO()

        output = typedbytes.Output(file)
        t = time.time()
        output.writes(map(str, range(100000)))
        print(time.time() - t)

        file.seek(0)

        input = typedbytes.Input(file)
        t = time.time()
        for record in input:
            pass
        print(time.time() -t)

        file.close()

    def testunicodes(self):
        file = io.BytesIO()

        output = typedbytes.Output(file)
        t = time.time()
        output.writes(map(str, range(100000)))
        print(time.time() - t)

        file.seek(0)

        input = typedbytes.Input(file)
        t = time.time()
        for record in input:
            pass
        print(time.time() -t)

        file.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSpeed)
    unittest.TextTestRunner(verbosity=2).run(suite)
