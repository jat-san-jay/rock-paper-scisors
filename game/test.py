import unittest


class TestRockPaperScissor(unittest.TestCase):
    choices = {
        "1": "The Rock",
        "2": "Paper",
        "3": "Scissor"
    }

    def test_paper_win(self):
        choice = 1
        my_choice = self.choices.get(str(choice))
        random_comp_turn = 2
        comp_choice = self.choices.get(str(random_comp_turn))

        xa = self.assertEqual(self.choices.get("1"), my_choice)
        xb = self.assertEqual(comp_choice, self.choices.get("2"))
        self.assertEqual(xa, xb)

        ya = self.assertEqual(self.choices.get("2"), my_choice)
        yb = self.assertEqual(comp_choice, self.choices.get("1"))
        self.assertEqual(ya, yb)


if __name__ == '__main__':
    unittest.main()
