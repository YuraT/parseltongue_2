def main():
    punctuation = [",", ".", ":", ";", " ", ]
    string = input("Enter the text which may be a palindrome: ")
    string = string.lower()

    for i in punctuation:
        string = string.replace(i, "")
    #    print(string)
    
    string_reversed = ""
    for i in range(len(string)):
        string_reversed = string_reversed + string[len(string) - i - 1]
    
    palindrome = False
    if string == string_reversed:
        palindrome = True

    if palindrome:
        print("The entered text is in fact a palindrome")
    else:
        print("The entered text in unfortunately not a palindrome")
main()