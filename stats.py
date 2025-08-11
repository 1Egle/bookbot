def get_book_text(path):
    with open(path) as f:
        read_contents = f.read()
        letters = read_contents.split()
        counter = 0

        for i in letters:
            counter += 1
        
        return (f"{counter}")

def counting_ants(path):
    with open(path) as f:
        read_contents = f.read().lower()
        list = []
        dictionary  = {}
        counter = 0

    for item in read_contents:
        
        if item not in dictionary:
            dictionary[item] = 1
        else:
            dictionary[item] += 1
    return dictionary
    
def print_statement(dictionary):
    sorted_dict = {k: v for k,v in sorted(dictionary.items(), key = lambda item: item[1], reverse = True)}
    for x, y in sorted_dict.items():
        if x.isalpha() == True:
            print (f"{x}:", y)
        else:
            pass




#    items = counting_ants('books'+"/frankenstein.txt").sort(reverse = True, key =)
    
        





