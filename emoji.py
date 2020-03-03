def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😄",
        ":(": "😞"
    }
    # get(key, default value) => récupére une valeur dans un dictionnaire
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))
