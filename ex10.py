class TestPhrase:
    def test_check_phrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) <=15, f"Длина строки должна быть не более 15 символов"

