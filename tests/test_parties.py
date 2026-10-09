import json
import unittest
from pathlib import Path

from party_extract.engine import find_parties, render

TEXT = Path("samples/recital.txt").read_text()


class PartyTests(unittest.TestCase):
    def test_two_parties(self):
        parties = find_parties(TEXT)
        self.assertEqual(parties[0]["name"], "Harbour Street Limited")
        self.assertEqual(parties[0]["role"], "Customer")
        self.assertEqual(parties[1]["name"], "Northline Data Limited")
        self.assertEqual(parties[1]["role"], "Supplier")

    def test_no_parties_without_the_pattern(self):
        self.assertEqual(find_parties("The Planning Board met on Tuesday."), [])

    def test_committed_json(self):
        self.assertEqual(json.loads(render(find_parties(TEXT))), json.loads(Path("samples/parties.json").read_text()))


if __name__ == "__main__":
    unittest.main()
