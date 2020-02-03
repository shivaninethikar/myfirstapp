import os, sys
import random
from flask import Flask, request
from pymessenger import Bot
from fb_element import element,start_buttons_list1,start_buttons_list2
 
app= Flask(__name__)

PAGE_ACCESS_TOKEN="EAAjgLoiA3iQBACaRnrG1H516aHfsx8KZBGqqX5lK4YWuAwiLnUCQ18cG0bqCZBtvF4ZBDhJSIVXrLhQgmZC9x5is8gPeiDtpaelSYWTtFLg15IAQ9GShqd0q6E9DikbiRwWmQQ1AUtnOIZB3pRikrP3eqVZBdJHVySvjEorJTTZAwZDZD"

bot=Bot(PAGE_ACCESS_TOKEN)


@app.route('/',methods=['GET'])
def verify():
    #webhook verification
    if request.args.get("hub.mode")== "subscribe"  and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch",403
        return request.args["hub.challenge"], 200
    return "Hello World" ,200



@app.route('/',methods=['POST'])


def webhook():
    data = request.get_json() #retrive the data from post request
    log(data) #to print data on the terminal
    print("hello")
    if data['object'] =='page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
            
                #for Id's
                sender_id=messaging_event['sender']['id']
                recipient_id=messaging_event['recipient']['id']
             
                
                #check message is text or not
                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                        bot.send_text_message(sender_id, messaging_text)
                    # if messaging_event['message'].get('attachments'):
                        # for att in messaging_event['message'].get('attachments'):
                            # bot.send_attachment_url(recipient_id, att['type':'image'], att['payload']['url':'http://www.messenger-rocks.com/image.jpg'])
                    else:
                        pass
                    
                    a="hello"
                    b="how are you"
                    c="have a good day"
                    
                    response=""
                    if messaging_event['message']['text']==a:                       
                        response= "You are stunning!"
                    elif messaging_event['message']['text']==b:  
                        response= "good"
                    elif messaging_event['message']['text']==c:  
                        response= "You Too"
                    bot.send_text_message(sender_id,response) 
                    if messaging_event['message']['text'] == "element":
                        payoad["recipient"]["id"] = sender_id
                        bot.send_generic_messege(str(payload))
                    else:
                        pass
		

					
                   
              
    return "ok",200  
 
def log(message):
    print(message)
    sys.stdout.flush() #prints compltete op message that store in the buffer
    

if __name__=="__main__":
    app.run(debug = True,port = 3000)
