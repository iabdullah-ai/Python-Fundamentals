import os
files=os.listdir("clutter")
i=1
for file in files:
    if file.endswith(".png"):
        os.rename(f"clutter/{file}",f"clutter/{i}.png")
        i=i+1