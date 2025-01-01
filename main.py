#counts words in the text file specified
def count_words(file):
    counter = 0
    words = file.split()
    for i in words:
        counter += 1
    return counter

#adds each possible letter to a dictionary and then checks each letter of the text against the dictionary and increments it before printing output
def count_letters(file):
    keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    dict = {key: 0 for key in keys}

    words = file.lower()

    total_counter = 0
    for j in keys:
        counter = 0
        for i in words:
            if j == i:
                counter += 1
                total_counter += 1
                dict.update({j:counter})

        
    print(f"breakdown of letters used can be found below \n{dict}")
    print(f"total letters used: {total_counter}")
    return dict

#sorts the dictionary of letters and outputs count of each letter in order from most to least
def sort_dict(dict):
    char_list = []
    def sort_on(dict):
        return dict["count"]
    for char, count in dict.items():
        char_info = {"char": char, "count": count}
        char_list.append(char_info)
        char_list.sort(reverse=True, key=sort_on)
    for i in char_list:
        print(f"the {i["char"]} character shows up {i["count"]}")
    return char_list
        


def main():
    #open path to frankenstein text
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    num_words = count_words(file_contents)
    print(f"{num_words} total words!")
    dict = count_letters(file_contents)
    sorted_dict = sort_dict(dict)
    
    

main()