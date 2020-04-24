import spacy
import random
import sys

try:
	with open("input.txt") as fin:
		lines = fin.read().splitlines()
		input_line = random.choice(lines)
except FileNotFoundError:
	print("input.txt doesn't exist")
	sys.exit()

nlp = spacy.load("en_core_web_sm")
doc = nlp(input_line)

names = []
for ent in doc.ents:
	if ent.label_ == "PERSON":
		name = ent.text.replace("'s","")
		names.append(name)

print(f'I: {input_line}\nO: {names}')
