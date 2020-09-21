def reverse_sentence(st):
    listed_string = st.split(" ")
    new_string = [abc[::-1] for abc in listed_string]
    xyz = " ".join(new_string)
    return xyz


s = input("Enter string: \n")
print(reverse_sentence(s))
