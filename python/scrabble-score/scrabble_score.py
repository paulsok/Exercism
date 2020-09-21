letters = ['aeioulnrst', 'dg', 'bcmp', 'fhvwy', 'k', 'jx', 'qz']

scores = [1, 2, 3, 4, 5, 8, 10]

lett_weights = {}

for i, j in zip(letters, scores):
    for l in i:
        lett_weights[l] = j

def score(word): 
    if word:
        return sum(lett_weights[x] for x in word.lower())
        
    return 0