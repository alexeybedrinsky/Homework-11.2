def uppercase_letter(input_letter):
    return input_letter.upper()
'''функция написания большими буквами'''

def capitalize_first_letters(input_string):
    """
    Функция capitalize_first_letters принимает на вход строку и делает заглавными первые буквы каждого слова в ней.

    Args:
        input_string (str): Входная строка, которую необходимо преобразовать.

    Returns:
        str: Строка с заглавными первыми буквами каждого слова.
    """
    return ' '.join(word.capitalize() for word in input_string.split())

