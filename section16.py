from PIL import Image

mask = Image.open('C:\\Users\\Pranav Pagote\\Downloads\\mask.png')
matrix = Image.open('C:\\Users\\Pranav Pagote\\Downloads\\word_matrix.png')

print(mask.size)
print(matrix.size)
mask = mask.resize((1015, 559))
print(mask.size)
mask.putalpha(200)
matrix.paste(im=mask, box=(0, 0), mask=mask)
matrix.show()
