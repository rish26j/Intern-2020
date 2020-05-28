def hello_visitor(**kwargs):
    if "Rishabh" in kwargs and kwargs["Rishabh"] == "Pirate":
        return "Captain Rishabh"
    elif "Rishabh" in kwargs and kwargs["Rishabh"] == "President":
        return "President Rishabh"
    elif "Rishabh" in kwargs:
        return "Hello citizen!"
    else:
        return "I don't know who you are"

print(hello_visitor(Stark="Iron Man"))
print(hello_visitor(Rishabh="Iron Man"))
print(hello_visitor(Rishabh="Pirate"))