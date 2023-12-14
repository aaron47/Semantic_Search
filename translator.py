class TunisianTranslator:
    __translation_dict = {
        "tawla": "table",
        "korsi": "chaise",
        "telifoun": "telephone",
        "mta3": "de",
        "taa": "de",
        "kartabla": "cartable",
        "cartabla": "cartable",
        "9raya": "scolarite",
        "9aleya": "poêle",
        "mekina": "machine",
        "makina": "machine",
        "9ahwa": "cafe",
        "5obz": "pain",
        "mizen": "balance",
        "koujina": "cuisine",
        "s8ar": "enfant",
        "8ta": "couverture",
        "ghta": "couverture",
        "stilou": "stylo",
        "saboura": "tableau",
        "tey": "the",
    }

    def translate(self, tunisian_text: str) -> str:
        words: list[str] = tunisian_text.split()

        return ' '.join([self.__translation_dict[
                             self.__check_first_three_letters(word)] if self.__check_first_three_letters(word) else word
                         for word in words])

        # translated_words: list[str] = []
        #
        # for word in words:
        #     key = self.__check_first_three_letters(word)
        #     if key:
        #         translated_words.append(self.__translation_dict[key])
        #     else:
        #         translated_words.append(word)
        #
        # return ' '.join(translated_words)

    def __check_first_three_letters(self, word: str) -> str | None:
        if word.__len__() < 3:
            return None

        first_three_letters = word[:3]

        for key in self.__translation_dict.keys():
            if key.startswith(first_three_letters):
                return key

        return None


if __name__ == "__main__":
    translated_string = TunisianTranslator().translate("cartabla taa 9raya")
    print(translated_string)
