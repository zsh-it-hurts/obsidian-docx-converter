from pathlib import Path
import subprocess

#with open ("example.md") as file:
 #   print(file.read())

input_file = Path("example.md")
output_file = Path("example.docx")

try:
    proc = subprocess.run(["pandoc", str(input_file), "-o", str(output_file)], capture_output=True, text=True, check=True)
    print("Document coverted successfully\n")
    print(f"Generated Document: {output_file.name}")
except subprocess.CalledProcessError as e:
    print(f"Document convert failed: {e.stderr}")
finally:
    print("its ALIVE!!!")
