
import os
import types
from datetime import datetime

from .agents import *
from openai import OpenAI


def start_new_client(api_key=None):
	"""Initialize a new instance of the OpenAI client"""

    # Confirm environment API key
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise EnvironmentError("OPENAI_API_KEY environment variable not found!")

    # Initialize OpenAI client and conversation thread
    client = OpenAI(api_key=api_key)
    client.thread_ids = []
    client.session_cost = 0.0
    client.token_usage = {}

    def start_new_thread(self, message_limit=30, context=False):
        """Start a new thread with only the current agent and adds previous context if needed."""
        thread = self.beta.threads.create()
        thread.time_started = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        thread.current_thread_calls = 0
        thread.message_limit = message_limit

        # Add previous context
        if context == True and len(self.thread_ids) >= 1:
            thread_messages = self.beta.threads.messages.list(self.thread_ids[-1])
            previous_context = self.beta.threads.messages.create(
                thread_id=thread.id, role="user", content=thread_messages.data)

        self.thread_ids.append(thread.id)

    client.start_new_thread = types.MethodType(start_new_thread, client)
    client.start_new_thread()

    return client

