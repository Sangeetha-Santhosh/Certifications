#frequency of alphabets in word
text = input("Enter a string: ").lower()
for ch in set(text):
    if ch.isalpha():  
        count = text.count(ch)
        print(ch, ":", count)