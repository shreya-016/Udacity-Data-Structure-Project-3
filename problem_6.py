from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.isWord = False

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        listOfWords = []
        self.suffixesRecursive(suffix, listOfWords)
        return listOfWords
    
    def suffixesRecursive(self, suffix, listOfWords):
        for char in self.children:
            suffix += char
            if self.children[char].isWord:
                #listOfWords.append(suffix+char)
                listOfWords.append(suffix)
                if len(self.children[char].children) > 0:
                    self.children[char].suffixesRecursive(suffix, listOfWords)
                    #self.children[char].suffixesRecursive(suffix+char, listOfWords)
            else:
                #self.children[char].suffixesRecursive(suffix+char, listOfWords)
                self.children[char].suffixesRecursive(suffix, listOfWords)
                
class Trie:
    def __init__(self):
        self.root = TrieNode()
       
    def insert(self, word):
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
                continue
            else:
                curr.children[char] = TrieNode()
                curr = curr.children[char]
        curr.isWord = True
        
    def find(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return curr
    
MyTrie = Trie()
listOfWords = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in listOfWords:
    MyTrie.insert(word)
    

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='tri');
