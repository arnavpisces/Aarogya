from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC64f5421baf4500a207dfd6f54752d9df"
# Your Auth Token from twilio.com/console
auth_token  = "21b55a570d845eaed3fa1e0d4aa92043"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+917838816965", 
    from_="+12014654883",
    body="Hello from Python!")

print(message.sid)