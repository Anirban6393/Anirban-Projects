def identify_person(col1, col2, col3): 
    return([[i for i, x in enumerate(data) if col1 in x or col2 in x or col3 in x],
            [i for i, x in enumerate(data) if col1 not in x and col2 not in x and col3 not in x]])

# Enumerate returns both index and values. Presence of value determines index value.

data = [
("username1","phone_number1", "email1"),
("usernameX","phone_number1", "emailX"),
("usernameZ","phone_numberZ", "email1Z"),
("usernameY","phone_numberY", "emailX"),
]

identify_person(None,"phone_number1", "emailX")