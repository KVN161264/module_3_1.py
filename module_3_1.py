calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [words.lower() for words in list_to_search]
    return string in list_to_search
print(string_info('Чемпион'))
print(string_info('Уимблдон'))
print(is_contains('Строка', ['СТР', 'Око', 'СтрОка']))
print(is_contains('магия', ['маг', 'магистр']))
print(calls)




