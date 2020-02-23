import re
import emoji


def strip_emoji(text):

    print(emoji.emoji_count(text))

    new_text = re.sub(emoji.get_emoji_regexp(), r"", text)

    return new_text


with open("data/twline.txt", "r") as filee:
    old_text = None
    old_text = filee.read()

no_emoji_text = None
no_emoji_text = strip_emoji(old_text)

with open("data/twemoji3.txt", "w") as new_file:
    new_file.write('')
    new_file.write(no_emoji_text)
