import re

class Token(object):
	""" A simple Token structure. Token type, value and position.
	"""
	def __init__(self, type, pos):
		self.type = type
		self.pos = pos

	def __str__(self):
		return '%s' % (self.type)


class LexerError(Exception):
	def __init__(self, pos):
		self.pos = pos

		
class Lexer(object):
	""" A simple regex-based lexer/tokenizer.
	"""
	def __init__(self, rules):
		""" Create a lexer.

			rules:
				A list of rules. Each rule is a `regex, type`
				pair, where `regex` is the regular expression used
				to recognize the token and `type` is the type
				of the token to return when it's recognized.

		"""
		self.rules = []
		for regex, type in rules:
			self.rules.append((re.compile(regex), type))
		self.re_ws_skip = re.compile('\S')

	def input(self, buf):
		""" Initialize the lexer with a buffer as input.
		"""
		self.buf = buf
		self.pos = 0

	def nextToken(self):
		""" Return the next token (a Token object) found in the
			input buffer. None is returned if the end of the
			buffer was reached.
			In case of a lexing error (the current chunk of the
			buffer matches no rule), a LexerError is raised with
			the position of the error.
		"""
		if self.pos >= len(self.buf):
			return None
		m = self.re_ws_skip.search(self.buf, self.pos)
		if m:
			self.pos = m.start()
		else:
			return None

		for regex, type in self.rules:
			m = regex.match(self.buf, self.pos)
			if m:
				tok = Token(type, self.pos)
				self.pos = m.end()
				return tok

		# if we're here, no rule matched
		raise LexerError(self.pos)

	def tokens(self):
		""" Returns an iterator to the tokens found in the buffer.
		"""
		while 1:
			tok = self.nextToken()
			if tok is None: break
			yield tok


