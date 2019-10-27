from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC3c1060cf9c5700d98029dcd2e8693d16"
# Your Auth Token from twilio.com/console
auth_token  = "6f3ad24140d08f40c2b6c85531e3f048"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12014654883", 
    from_="+12057032768",
    body="location")

print(message.sid)