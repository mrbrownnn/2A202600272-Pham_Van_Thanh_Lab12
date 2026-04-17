"""Simple mock LLM used for local and cloud deployment demos."""

import random
import time


MOCK_RESPONSES = {
	"default": [
		"This is a mock AI answer. In production this would come from a real model.",
		"Agent is running correctly. Ask another question.",
		"Your question was received successfully by the deployed service.",
	],
	"docker": ["Containers package an app so it can run consistently anywhere."],
	"deploy": ["Deployment is the process of publishing your app to a server."],
	"health": ["Service health is good. All systems operational."],
}


def ask(question: str, delay: float = 0.1) -> str:
	"""Return a mock answer with a small artificial latency."""
	time.sleep(delay + random.uniform(0, 0.05))

	lower_question = question.lower()
	for keyword, responses in MOCK_RESPONSES.items():
		if keyword in lower_question:
			return random.choice(responses)

	return random.choice(MOCK_RESPONSES["default"])


def ask_stream(question: str):
	"""Yield a mock response token-by-token to simulate streaming."""
	response = ask(question)
	for word in response.split():
		time.sleep(0.05)
		yield word + " "
