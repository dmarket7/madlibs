"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
story2 = Story(
    ["silly_word_1", "name", "illness", "plural_noun", "adjective_1", "adjective_2", "silly_word_2", "place", "number", "adjective_3"], """Dear School Nurse: \n
{silly_word_1} {name} will not be attending school today. He/she has come down with a case of {illness} and has horrible {plural_noun} and a/an {adjective_1} fever. We have made an appointment with the {adjective_2} Dr. {silly_word_2}, who studied for many years in {place} and has {number} degrees in pediatrics. He will send you all the information you need. Thank you! \n
Sincerely \n
Mrs. {adjective_3} """
)







story_list = [story, story2]