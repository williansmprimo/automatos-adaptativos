class State:
	def __init__(self, id, simble):
		self.id = id
		self.simble = simble

class Transition:
	def __init__(self, origin, destination, simble):
		self.origin = origin
		self.destination = destination
		self.simble = simble
		
class AASO:
	def __init__(self, dados):
		# self.vocabulary = list(set([w for w in [s.split() for s in dados]]))
		vocabulary = set()
		for s in dados:
			for w in s.split():
				vocabulary.add(w);
			
		self.vocabulary = list(vocabulary);
		self.vocabulary.insert(0, "")
		
		self.states = []
		id = 0
		for word in self.vocabulary:
			state = State(id, word)
			self.states.append(state)
			id += 1
			
		self.transitions = []
		self.state = self.states[0]
		for sentence in dados:
			lastWord = ""
			lastState = self.state
			for word in sentence.split():
				state = self.findStates(lambda x: x.simble == word)[0]
				transition = Transition(lastState, state, lastWord)
				self.transitions.append(transition)
				lastWord = word
				lastState = state
		
		print("states:")
		for s in self.states:
			print(s.id, "-", s.simble)
			
		print("transitions:")
		for t in self.transitions:
			print(t.origin.id, "-", t.destination.id, "-", t.simble)
				
	def findStates(self, search):
		return list(filter(search, self.states))
		
	def findTransitions(self, search):
		return list(filter(search, self.transitions))
		
	def train(self):
		print("Train")
				
		
	def next(self, simble):
		transitions = self.findTransitions(lambda x: x.simble == simble and x.origin.id == self.state.id);
		self.state = transitions[0].destination;
		return self.state.simble;
		
def load_data():
	return ["A B C D E F G", "F G H I J K L"]

def main():
	dados = load_data()
	model = AASO(dados);
	model.train();
	
	start = input('Type the begining of text: ');
	numberOfSteps = int(input('The size of the text to be generate: '));
	for step in range(0, numberOfSteps):
		next = model.next(start)
		#start = start + " " + next
		start = next
		print(step, ": ", start)
		
main()