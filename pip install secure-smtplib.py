from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'AC1e29ffdbc2255d7ea1376a261d1218d0'
auth_token = 'becf53c0352716f21dfccc6a92cff127'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send a text message
message = client.messages.create(
    body='HI',
    from_='18776190123',
    to='8312058632'
)

print(message.sid)
