files = ["app.py", "chat.py", "qchat.py", "vision.py"]


for file in files:
    with open(file, "w") as f:
        f.write("# " + file + " file\n")