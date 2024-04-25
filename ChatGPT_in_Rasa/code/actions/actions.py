# This files contains your custom actions which can be used to run custom Python code
# See this guide on how to implement these action: https://rasa.com/docs/rasa/custom-actions

import openai
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Tracker
from typing import Any, Text, Dict, List

openai.api_key = 'sk-proj-u2vEUUuWz8NZyL7aougJT3BlbkFJGFRG5oYSDDNfyMOuTQOa'


class ChatGPTAction(Action):
    def name(self) -> Text:
        return 'action_generate_Pet'

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        prompt = ('Dear ChatGPT, I recently lost my beloved puppy, Milo. He was an incredibly lively and affectionate golden retriever who always greeted me with boundless energy and wagging tail as soon as I walked through the door. His favorite activity was to fetch tennis balls in the park and he would often snuggle next to me when I watched TV. Could you help me feel his presence again by simulating a conversation I might have had with him when I come home from work?')

        response = openai.Completion.create(
            engine='gpt-3.5-turbo-instruct',
            prompt=prompt,
            max_tokens=2048,
            stop=None,
            n=1,
            temperature=0.5
        )

        generated_text = response.choices[0].text
        dispatcher.utter_message(text=prompt)
        dispatcher.utter_message(text=generated_text)

        return []


class ChatGPTAction(Action):
    def name(self) -> Text:
        return 'action_generate_WeChat'

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        prompt = ('Hello ChatGPT, I need your assistance in crafting a post for WeChat Moments. I want the post to radiate a sense of nostalgia and warmth, reflecting on a recent family gathering in a literary style. The mood should be gentle and evocative, using vivid imagery to convey the soft glow of sunset that bathed our reunion in a golden light. Please let your imagination flow freely and create a text that encapsulates the emotions of joy mixed with a longing for these moments to last forever. Thank you!')

        response = openai.Completion.create(
            engine='gpt-3.5-turbo-instruct',
            prompt=prompt,
            max_tokens=2048,
            stop=None,
            n=1,
            temperature=0.5
        )

        generated_text = response.choices[0].text
        dispatcher.utter_message(text=prompt)
        dispatcher.utter_message(text=generated_text)

        return []
