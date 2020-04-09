
class TrieNode:
    def __init__(self):
        self.children = [None] * 127
        self.score =None
        self.restaurant_id=None
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def to_index(self, ch):
        return ord(ch) #- ord('a')

    def insert(self, key, score, restaurant_id):
        p = self.root
        length = len(key)
        for level in range(length):
            index = self.to_index(key[level])
            if not p.children[index]:
                p.children[index] = self.getNode()
            if(p.score == None):
                p.score=0
            if(p.restaurant_id == None):
                p.restaurant_id=0
            p = p.children[index]
        p.end_of_word = True
        p.score = score
        p.restaurant_id= restaurant_id

    def search(self, key):
        p = self.root
        length = len(key)
        for level in range(length):
            index = self.to_index(key[level])
            if not p.children[index]:
                return False
            p = p.children[index]
        if p != None and p.end_of_word:
            return 1
        return 0

    def get_max_from_subtree(self, p):
        answer=dict({
            "score": p.score,
            "restaurant_id": p.restaurant_id
        })
        for index in range(0 , 127):
            if p.children[index]:
                child_answer=self.get_max_from_subtree(p.children[index])
                child_score= child_answer["score"]
                if(answer["score"] <  child_score):
                    answer=child_answer

        return answer

    def special_search(self, key): # key=prefix restaurant

        p = self.root
        length = len(key)
        for level in range(length):
            index = self.to_index(key[level])
            if not p.children[index]:
                return False
            p = p.children[index]

        if p != None:
            return self.get_max_from_subtree(p)

        return ""

