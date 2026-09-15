class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for word in strs:
            # 1. build the key from word (sort the letters, then make it a string or tuple)
            key = tuple(sorted(word))

            # 2. is this the first word with this key?
            if key not in ana :
                ana[key] = [word]
                
            else:
                # group already exists: add word to the list stored under key
                ana[key].append(word)
        # 3. return only the groups, as a list
        return list(ana.values())