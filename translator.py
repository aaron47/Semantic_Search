from difflib import get_close_matches


class TunisianTranslator:
    __translation_dict = {
        "tawla": "table",
        "korsi": "chaise",
        "telifoun": "telephone",
        "mtaa": "de",
        "kartabla": "cartable",
        "9raya": "scolarite",
        "9aleya": "poêle",
        "mekina": "machine",
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
        "souria": "chemise",
        "azra9": "bleu",
        "zar9a": "bleu",
        "a7mer": "rouge",
        "7amra": "rouge",
        "ak7al": "noir",
        "ka7la": "noir",
        "serwel": "pantalon"
    }

    def translate(self, tunisian_text: str) -> str:
        words: list[str] = tunisian_text.split()

        # return ' '.join([self.__translation_dict[
        #                      self.__find_best_match(word)] if self.__find_best_match(word) else word
        #                  for word in words])

        translated_words: list[str] = []

        for word in words:
            key = self.__find_best_match(word)
            if key:
                translated_words.append(self.__translation_dict[key])
            else:
                translated_words.append(word)

        return ' '.join(translated_words)

    def __find_best_match(self, tunisian_text: str) -> str | None:
        matches: list = get_close_matches(tunisian_text, self.__translation_dict.keys(), n=1, cutoff=0.7)
        return matches[0] if matches else None

    # Might be useful later

    # def __check_first_three_letters(self, word: str) -> str | None:
    #     if word.__len__() < 3:
    #         return None
    #
    #     first_three_letters = word[:3]
    #
    #     for key in self.__translation_dict.keys():
    #         if key.startswith(first_three_letters):
    #             return key
    #
    #     return None


if __name__ == "__main__":
    translated_string = TunisianTranslator().translate("souria zar9a")
    print(translated_string)
