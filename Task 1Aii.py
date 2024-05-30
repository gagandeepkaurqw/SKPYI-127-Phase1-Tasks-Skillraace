import emoji
text_with_emoji=input("Enter the text to be converted: ")
text_without_emoji=emoji.demojize(text_with_emoji)
print("The converted text= ",text_without_emoji)