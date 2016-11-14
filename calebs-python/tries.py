## DONE, (theoretically would work for any letters in as string) could be made to work only for a subset like lowercase letters
## Caleb Gates 11-14-16
## Trie and Trie Nodes

class Trie_Node:
	def __init__(self,word=None):
		self.dict = {}
		self.word = word
		
	def is_word(self):
		if(self.word != None):
			return True
		return False

	def remove_word(self):
		self.word = None
	
	def remove_pointer(self,p):
		self.dict.pop(p,None)

class Trie:
	def __init__(self):
		self.root = Trie_Node()

	def insert(self,word):
		if(word[0] in self.root.dict):
			self._insert_recursive(word,1,self.root.dict[word[0]])
		else:
			self._insert_rest(word,0,self.root)#should this be 1 or 0

	def _insert_recursive(self,word,position,node):
		if len(word) >= position + 1:#not last character #fixed works
			if word[position] in node.dict:
				self._insert_recursive(word,position +1, node.dict[word[position]])
			else: #insert new nodes
				self._insert_rest(word,position,node)
		else:
			node.word = word
			
	def _insert_rest(self,word,position,node):
		while position < len(word):#am i off by -1?
			new_node = Trie_Node()
			node.dict[word[position]] = new_node
			node = new_node
			position += 1
		node.word = word
	
	#def __str__(self): #(TO DO)
	#	return str(self.root.dict.keys())
	
	def search(self,word):
		if word[0] in self.root.dict:
			return self._search_recursive(word,1,self.root.dict[word[0]])
		else:
			return False

	def _search_recursive(self,word,position,node):
		print(position)
		print(node.word)
		if len(word) == position:
			if node.word == word:
				return True
			return False
		elif word[position] in node.dict:
			return self._search_recursive(word,position+1,node.dict[word[position]])
		return False
	
	def delete(self,word):
		if(self.search(word)):#word in trie
			if self._delete_recursive(word,0,self.root):
				self.root.dict.pop(word[0])

	def _delete_recursive(self,word,position,node):
		if(len(word) == position):
			node.word = None #get rid of word incase node remains
			if len(node.dict) == 0:
				return True
			return False
		if self._delete_recursive(word,position+1,node.dict[word[position]]):
			node.dict.pop(word[position], None)#remove node
			if len(node.dict) == 0 and node.word == None:
				return True
			return False #unnecesary bc of next line but leave incase of modification
		return False
			
	def dfs_words(self):#Not in alphabetical order becasue Hash table (dict) is not sorted
		for d in self.root.dict.keys():
			self._dfs_words(self.root.dict[d])
	def _dfs_words(self,node):
		if node.word != None:
			print(node.word)
		for d in node.dict.keys():
			self._dfs_words(node.dict[d])
			

	def bfs_words(self):#returns by length of words, level by level
		nodes = []
		for d in self.root.dict.keys():
			nodes.append(self.root.dict[d])
		
		while(len(nodes) != 0):
			for i in range(0,len(nodes)):
				if nodes[i].word != None:
					print(nodes[i].word)
			
			next_nodes = []
			for n in nodes:
				for d in n.dict.keys():
					next_nodes.append(n.dict[d])

			nodes = next_nodes

#from tries import Trie_Node, Trie

AA = Trie()
AA.insert('cat')
AA.insert('cabs')
AA.insert('cab')
AA.insert('ca')

AA.search('cabs')
AA.search('hello')

AA.delete('cab')
AA.search('cabs')

AA.dfs_words()
AA.bfs_words()
