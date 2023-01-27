from django.conf import settings
# from twilio.rest import Client
from .models import *

# class MessageHandler:

#     phone_number = None
#     otp = None

#     def __init__(self, phone_number , otp) -> None:
#         self.phone_number = phone_number
#         self.otp = otp

#     def send_otp_on_phone(self):

#         # client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
#         client = Client('AC81c847752bdb95277a90b4055cf12111', 'acac6df1c11a9d351044769d7ba6cf0b')
#         message = client.messages.create(
#                 body=f'Your Area360 verification code is: {self.otp}',
#                 from_='+12673148248',
#                 to=self.phone_number
#             )
#         print(message.sid)


# import http.client

# conn = http.client.HTTPSConnection("api.msg91.com")

# payload = "{\n  \"Param1\": \"value1\",\n  \"Param2\": \"value2\",\n  \"Param3\": \"value3\"\n}"

# headers = { 'Content-Type': "application/JSON" }
# url = "https://control.msg91.com/api/sendotp.php?otp="+otp+'&sender=ABC&message='+'Your otp is '+otp +'&mobile='+mobile+'&authkey='+authkey+'&country=91'
# conn.request("GET",headers=headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))

from twilio.rest import Client


def send_otp_code(phone_number, otp_code):
    # Your Twilio Account SID and Auth Token
    account_sid = settings.ACCOUNT_SID
    auth_token = settings.AUTH_TOKEN

    # Your Twilio phone number
    from_phone_number = settings.PHONE_NUMBER

    # print(account_sid)

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=f'+91{phone_number}',
        from_=from_phone_number,
        body=f'Your OTP code is: {otp_code}'
    )
    # print(message.sid)


# def verifyotp(mobile,otp):
#     data = Profile.objects.get(phoneno=mobile)
#     if otp == data.otp:
#         data.is_verified = True
#         data.save()
#         return redirect('/')
#     else:
#         msg = "Please enter correct otp."
#         return msg
