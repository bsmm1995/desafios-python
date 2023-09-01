def is_palindrome(text):
    text = text.lower()
    text_without_spaces = text.replace(" ", "")
    return text_without_spaces == text_without_spaces[::-1]


def first_letter_repeated(text):
    text = text.lower()
    text_without_spaces = text.replace(" ", "")
    list_letters = []
    for letter in text_without_spaces:
        if letter in list_letters:
            return letter
        else:
            list_letters.append(letter)
    return None


def convert_schedules(time):
    time_parts = time.split(":")
    if time[-2:].lower() == "pm":
        if time_parts[0] != 12:
            time_parts[0] = str(int(time_parts[0]) + 12)
    else:
        if time_parts[0] == 12:
            time_parts[0] = "00"
    return ":".join(time_parts)[:-2]


def are_anagrams(word_1, word_2):
    letters_word_1 = sorted(word_1.lower())
    letters_word_2 = sorted(word_2.lower())
    return letters_word_1 == letters_word_2


if __name__ == '__main__':
    print("Palindrome:", is_palindrome('aNa'))
    print("Repeated:", first_letter_repeated("Hola"))
    print("Schedules:", convert_schedules("10:00pm"))
    print("Anagrams:", are_anagrams("calor", "coral"))
