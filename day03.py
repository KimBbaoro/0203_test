letter = '''
        Dear {salutation} {name},
        Thank you for your letter. We are sorry that out {product} {verbed} in your {room}. Please note that it should never be used in a {room}, especially near any {animals}.

        Send us your reciept and {amount} for shipping and handling. We will send you another {product} that, in our tests, is {percent}% less to have {verbed}.

        Thank you for you support.
        Sicerely,
        {spokesman}
        {job_title}
'''
print(letter.format(salutation="1", name='김건유', product='car', verbed='ate',
                    room='oneroom', animals='dog', amount='three', percent="10", spokesman="building owner", job_title="manager"))
