from pathlib import Path
#····Constant with the new of the file to open
FILENAME="ADA.txt"
#...Open and read the file
file_contents = Path(FILENAME).read_text()

#...Print the contents on the console

content= file_contents.split("\n")[1:]
Body_file = "."join(content).replace(".","")
print("Body of the ADA.txt file:")
print(len(Body_file))

