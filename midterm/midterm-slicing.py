# Author: Ty Brien
# Description:
from email.quoprimime import quote


print("Name: Ty Brien")

with open("slicing-file.txt", "r") as slicingfile:
    slice_list = slicingfile.read().split("\n")

four_a = slice_list[-3]
four_b = slice_list[2:5]
four_c = slice_list[-10:-15:-2]
four_d = slice_list[10:13]
four_e = slice_list[-19:-22:-1]
quote = f"{four_a} {' '.join(four_b)} {' '.join(four_c)} {' '.join(four_d)} {' '.join(four_e)}"
print(quote)