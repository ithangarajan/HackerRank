def count_substring(string, sub_string):
    counter=0
    occurance=0
    while (counter<len(string)):
        if string.find(sub_string,counter) != -1:
            counter=string.find(sub_string,counter)+1
            occurance=occurance+1
        else:
            break
    return occurance 