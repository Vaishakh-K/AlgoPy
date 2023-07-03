from typing import Dict, List


class SortAnagrams:
    def __init__(self, strs: List[str]) -> str:
        self.strs = strs

    def get_encoding(self, string: str):
        encoding: str = ""
        count: list = [0 for i in range(26)]
        for c in string:
            count[ord(c) - 97] += 1

        for ct in count:
            encoding += f"{ct}#"

        return encoding

    def get_sorted_anagrams(self) -> List[List[str]]:
        anagram_dict: Dict[str, List[str]] = dict()
        anagrams_list: List[List[str]] = []

        for string in self.strs:
            encoding = self.get_encoding(string)
            if encoding in anagram_dict:
                anagram_dict.get(encoding).append(string)
            else:
                anagram_dict[encoding] = []
                anagram_dict[encoding].append(string)

        for encoding in anagram_dict:
            anagrams_list.append(anagram_dict[encoding])

        return anagrams_list


sorted_anagrams = SortAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
anagrams = sorted_anagrams.get_sorted_anagrams()
print(anagrams)

sorted_anagrams = SortAnagrams(["", ""])
anagrams = sorted_anagrams.get_sorted_anagrams()
print(anagrams)
