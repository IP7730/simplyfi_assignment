def indian_currency(number):

    result = ""
    count = 0
    c = 0

    for digit in reversed(number):
        if c == 3 or (c == 2 and count >= 5):
            result += ','
            c = 0

        result += digit
        count += 1
        c += 1

    result = result[::-1]

    return result

input_number = input("Enter a number: ")
output_currency = indian_currency(input_number)
print(f"Input: {input_number}\nOutput: {output_currency}")