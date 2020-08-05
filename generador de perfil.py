from instagram.client import InstagramAPI


access_token = "IGQVJVNmpQQUtubnlkMDFKLS1xck83WFZAmMGJMaEZAvMWtyOXlrelRzUjZADZAlNNQVR3XzhZAajVYMndmTXZA2TFBGTUN4aFFQVmRuRFJ1VF9TM1VWdjB6UWtfbGZAWXzVxLUlPRk9kV21Kb3YzRlVfcmxLQgZDZD"
client_secret = "972462359874171"
api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media, next_ = api.user_recent_media(user_id="", count=10)
for media in recent_media:
   print(media.caption.text)
   

