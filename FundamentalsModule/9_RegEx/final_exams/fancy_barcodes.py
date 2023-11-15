import re

rows_input = int(input())

pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"
digit_pattern = r"[0-9]+"

for text in range(rows_input):
    product_group = ""
    current_text = input()
    match_result = re.findall(pattern, current_text)
    if match_result:
        for match in match_result:
            digit_result = re.findall(digit_pattern, match)
            if digit_result:
                for digit in digit_result:
                    product_group += digit
            else:
                product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
