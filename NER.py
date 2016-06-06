"""
Programming task
================

The following is an implementation of a simple Named Entity Recognition (NER).
NER is concerned with identifying place names, people names or other special
identifiers in text.

Here we make a very simple definition of a named entity: A sequence of
at least two consecutive capitalized words. E.g. "Los Angeles" is a named
entity, "our hotel" is not.

While the implementation passes the Unit test, it suffers from bad structure and
readability. It is your task to rework *both* the implementation and the Unit
test. You are expected to come up with a better interface than the one presented
here.

Your code will be evaluated on:
- Readability: Is naming intuitive? Are there comments where necessary?
- Structure: Is functionality grouped into functions or classes in a way that
enables reusability?
- Testability: Is it easy to test individual components of your algorithm? This
is a good indicator of good interface design.
- Bonus: Functional programming. Demonstrate how you have applied principles of
functional programming to improve this code.

If you want, explain reasons for changes you've made in comments.

Note that you don't have to improve the actual Named Entity Recognition
algorithm itself - the focus is on code quality.
"""

import re
import unittest

# Buffer to store current named entity
word_buffer = []
# Regular expression for matching a token at the beginning of a sentence
token_re = re.compile(r"([a-z]+)\s*(.*)$", re.I)
# Regular expression to recognize an uppercase token
uppercase_re = re.compile(r"[A-Z][a-z]*$")

def pop_token(text):
	"""
	Take the first token off the beginning of text. If its first letter is
	capitalized, remember it in word buffer - we may have a named entity on our
	hands!!

	@return: Tuple (token, remaining_text). Token is None in case text is empty
	"""
	global word_buffer
	token_match = token_re.match(text)
	if token_match:
		token = token_match.group(1)
		if uppercase_re.match(token):
			word_buffer.append(token)
		else:
			word_buffer = []
		return token, token_match.group(2)
	return None, text

def has_named_entity():
	"""
	Return a named entity, if we have assembled one in the current buffer.
	Returns None if we have to keep searching.
	"""
	global word_buffer
	if len(word_buffer) >= 2:
		named_entity = " ".join(word_buffer)
		word_buffer = []
		return named_entity

class NamedEntityTestCase(unittest.TestCase):

	def test_ner_extraction(self):

		# Remember to change this Unit test as well to follow the interface
		# changes you propose above
		
		text = "When we went to Los Angeles last year we visited the Hollywood Sign"

		entities = set()
		while True:
			token, text = pop_token(text)
			if not token:
				entity = has_named_entity()
				if entity:
					entities.add(entity)
				break

			entity = has_named_entity()
			if entity:
				entities.add(entity)

		self.assertEqual(set(["Los Angeles", "Hollywood Sign"]), entities)

if __name__ == "__main__":
    unittest.main()
