
# element = [
           # {
            # "title":"Test",
            # "image_url":"arsenal_logo.png",
            # "subtitle":"subtitle",
            # "default_action": {
              # "type": "web_url",
              # "url": "http://arsenal.com",
              
            # },
            # "buttons":[
              # {
                # "type":"web_url",
                # "url":"http://arsenal.com",
                # "title":"View Website"
              # },{
                # "type":"postback",
                # "title":"Start ",
                # "payload":"PAYLOAD"
              # }
            # ]
           # }
  # ]
start_buttons_list1 = [
          {
            "type":"postback",
              "title": "HAAA",
              "payload": "haaa"
          },          {
            "type":"postback",
              "title": "oooo",
              "payload": "oooo"
          },          {
            "type":"postback",
              "title": "More options",
              "payload": "start_option1"
          }
        ]


start_buttons_list2 = [
          {
            "type":"postback",
              "title": "button 2",
              "payload": "talk_to_the_expert"
          },          {
            "type":"postback",
              "title": " check ",
              "payload": "test"
          },          {
            "type":"postback",
              "title": "View more options",
              "payload": "start_option2"
          }
        ]

element = [
           {
            "title":"Welcome!",
            "image_url":"arsenal_logo.png",
            "subtitle":" logo ",
            "default_action": {
              "type": "web_url",
              "url": "http://arsenal.com",
              "webview_height_ratio": "tall",
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"http://arsenal.com",
                "title":"View Website"
              },{
                "type":"postback",
                "title":"Start ",
                "payload":"DEVELOPER_DEFINED_PAYLOAD"
              }
            ]
           }
  ]