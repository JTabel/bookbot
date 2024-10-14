def sort_on(dict):
    return dict["count"]

with open("books/frankenstein.txt") as f:
    file_contents = f.read() 
    words = file_contents.split()
    count = {}

    for c in file_contents:
        decap_c = c.lower()
        if decap_c in count:
            count[decap_c] += 1
        else:
            count[decap_c] = 1

    count_list = []
    for c in count:
        count_list.append({"character": c, "count": count[c]})
    
    count_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {f.name} ---")
    print(f"{len(words)} words found in the document\n")
    for char in count_list:
        if char["character"].isalpha():
            print(f"The '{char["character"]}' character was found {char["count"]} times")
    print("--- End report ---")