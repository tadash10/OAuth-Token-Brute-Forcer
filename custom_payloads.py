def generate_custom_payloads(grant_type):
    # Generate custom payloads based on the grant type
    custom_payloads = []

    if grant_type == "password":
        custom_payloads.append({"username": "user1", "password": "password1"})
        custom_payloads.append({"username": "user2", "password": "password2"})
        # Add more custom payloads for different scenarios

    # Add logic for other grant types and custom payloads

    return custom_payloads
