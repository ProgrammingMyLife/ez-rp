from os import stat_result
import PySimpleGUI as sg
from pypresence import Presence
from pypresence.exceptions import InvalidArgument, InvalidID, InvalidPipe, ServerError
import webbrowser
import json

# Raven's Rich Presence Generator is a free open source program to generate custom discord rich presences. If anyone tries to sell you Raven's Rich Presence Generator, or tries to redistribute it as their own, please report it immediately. You are being scammed"
theme_choice = 'DarkGrey5'
sg.theme(theme_choice) 
# All the stuff inside the window.
layout = [  [sg.Text("Raven\'s Rich Presence Generator", background_color="#212835")],
            [sg.Text("                                                                                                                                                                                                                                                                                 ", key="ERROR", text_color="red", background_color="#212835")], #This string is long.
            [sg.Text('Enter your client ID', key="~CLIENTID~", background_color="#212835", ), 
            sg.InputText(key="CLIENTIDBOX")],
            [sg.Text('Large Image ID:', key="~LIMAGEID~", background_color="#212835"),
            sg.InputText(key="LARGEIMAGEKEY")],
            [sg.Text('Small Image ID:', key="~SIMAGEID~", background_color="#212835"),
            sg.InputText(key="SMALLiMAGEKEY")],
            [sg.Text('Enter top line of text', key="~RPCDETAILS~", background_color="#212835"), 
            sg.InputText(key="DETAILS")],
            [sg.Text('Enter bottom line of text', key="~RPCSTATE~", background_color="#212835"), 
            sg.InputText(key="STATE")],
            [sg.Text('(Optional) First button text', key="~firstbuttontext~", visible = True, background_color="#212835", ), 
            sg.InputText(key="BUTTONLABEL")],
            [sg.Text('(Mandatory if you put text for first button) First button URL', key="~firstbuttonurl~", visible = True, background_color="#212835"), 
            sg.InputText(key="BUTTONURL")],
            [sg.Button('Run!', button_color="#d764f9"), sg.Button("Load from config.json", button_color="#d764f9"), sg.Button("Save to config.json", button_color="#d764f9"), sg.Button('Client ID', button_color="#d764f9"), sg.Button('Join Discord!', button_color="#d764f9"), sg.Button('Help', button_color="#d764f9"),],
            [sg.Text('Raven\'s Rich Presence Generator is a free open source program to generate custom discord rich presences. \n If anyone tries to sell you Ravens Rich Presence Generator, or tries to redistribute it as their own, please report it immediately.\n You are being scammed', justification='center', background_color="#212835", )]
            ]
            
            

# Create the Window
window = sg.Window('Rich Presence', layout, icon="test.png", element_justification='c', background_color="#212835")

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    
    

    if event == sg.WIN_CLOSED : # if user closes window or clicks cancel
        break
    
    elif event == "Client ID": 
        webbrowser.open("https://discord.com/developers/applications")
        
    elif event == 'Join Discord!':
        webbrowser.open("https://discord.gg/MwmnXNsjsj")
    elif event == 'Help':
        sg.Popup('''Raven\'s Rich Presence Generator\n
Client ID: the long number associated with the app you made in the Discord Developer Portal. \n
Large Image ID: The filename of the large image\n
Small Image I: The filename of the small image\n
State of Rich Presence: This is the top text that will be displayed in your presence\n
Details of Rich Presence: The text that is right below your state text\n
Button Text: The label text shown on the button\n
Button URL: The URL that will be opened when a user clicks on the button''')

    elif event == "Save to config.json":
        
        data = {
            "ClientID": values["CLIENTIDBOX"],
            "LargeImageKey": values["LARGEIMAGEKEY"],
            "SmallImageKey": values["SMALLiMAGEKEY"],
            "State": values["STATE"],
            "Details": values["DETAILS"],
            "ButtonLabel": values["BUTTONLABEL"],
            "ButtonUrl": values["BUTTONURL"]

        }
        json_object = json.dumps(data, indent = 4) 


        with open("config.json", "w") as f:
            f.write(json_object)
            

            

        
        


    elif event == "Load from config.json":
        config = None
        largeimage = None
        smallimagekey = None
        state = None
        details = None
        buttonurl = None
        buttonlabel = None

        try :
            config = json.load(open("config.json"))

        except FileNotFoundError :
            window.Element("ERROR").Update("Error occured! The config.json file does not exist. Make sure it is in the folder of ez-rp.exe")
        
        try :
            cid = str(config["ClientID"])
            window.Element("CLIENTIDBOX").Update(cid)
        
        except KeyError :
            sg.Popup("Error occured! Client ID Value does not exist.")

        try :
            largeimage = str(config["LargeImageKey"])
            window.Element("LARGEIMAGEKEY").Update(largeimage)

        except KeyError:
            print("No Large Iage") 

        try :
            smallimage = str(config["SmallImageKey"])
            window.Element("SMALLiMAGEKEY").Update(smallimage)

        except KeyError :
            print("No small image")

        try :
            
            state = str(config["State"])
            print(state)
            window.Element("STATE").Update(state)

        except KeyError :
            print("No state in config.json")

        try :
            details = str(config["Details"])
            window.Element("DETAILS").Update(details)

        except KeyError :
            print("No details in config.json")

        try :
            buttonlabel = str(config["ButtonLabel"])
            window.Element("BUTTONLABEL").Update(buttonlabel)

        except KeyError :
            print("No button label in config.json")

        try :
            buttonurl = str(config["ButtonURL"])
            window.Element("BUTTONURL").Update(buttonurl)

        except KeyError :
            print("No state in config.json")
            
        


        

        
        

        
        

    elif window["~firstbuttontext~"] == None and not window["~firstbuttonurl~"] == None:
        window.Element("ERROR").Update("An error occured! Please make sure to add a URL!")

    elif window["~firstbuttonurl~"] == None and not window["~firstbuttontext~"] == None:
        window.Element("ERROR").Update("An error occured! Make sure to add a label for your button!")
    
    else:
        
        try :
            
            print(values["BUTTONLABEL"])
            print("bruh moment")
            RPC = Presence(values["CLIENTIDBOX"])
            RPC.connect()

            print(RPC.update(state=values["STATE"], details=values["DETAILS"], buttons=[{"label": values["BUTTONLABEL"], "url": values["BUTTONURL"]}]))

            
            print("Ran this function")
            window.Element("ERROR").Update("Success! Your rich presence is now up! Make sure to leave this window open.", text_color="green")
            window.TKroot.title("ez-rp Custom Rich Presence. Currently Running!")

        
        except InvalidID :
            window.Element("ERROR").Update("An error occured! Please correct your Client ID!")

        except :
            try :
        
                RPC = Presence(values["CLIENTIDBOX"])
                RPC.connect()
                RPC.update(state=values["STATE"], details=values["DETAILS"], large_image=values["LARGEIMAGEKEY"], small_image=values["LARGEIMAGEKEY"])
                window.Element("ERROR").Update("Success! Your rich presence is now up! Make sure to leave this window open.", text_color="green")
                window.TKroot.title("ez-rp Custom Rich Presence. Currently Running!")
            except ServerError:
                try:
                    RPC = Presence(values["CLIENTIDBOX"])
                    RPC.connect()
                    RPC.update(state=values["STATE"], details=values["DETAILS"], large_image=values["LARGEIMAGEKEY"])
                    window.Element("ERROR").Update("Success! Your rich presence is now up! Make sure to leave this window open.", text_color="green")
                    window.TKroot.title("ez-rp Custom Rich Presence. Currently Running!")
                except ServerError:
                    try:
                        RPC = Presence(values["CLIENTIDBOX"])
                        RPC.connect()
                        RPC.update(state=values["STATE"], details=values["DETAILS"], small_image=values["SMALLiMAGEKEY"])
                        window.Element("ERROR").Update("Success! Your rich presence is now up! Make sure to leave this window open.", text_color="green")
                        window.TKroot.title("ez-rp Custom Rich Presence. Currently Running!")
                    except ServerError:
                        RPC = Presence(values["CLIENTIDBOX"])
                        RPC.connect()
                        RPC.update(state=values["STATE"], details=values["DETAILS"])
                        window.Element("ERROR").Update("Success! Your rich presence is now up! Make sure to leave this window open.", text_color="green")
                        window.TKroot.title("ez-rp Custom Rich Presence. Currently Running!")


            except ServerError:
                window.Element("ERROR").Update("An error occured! Please make sure you entered everything required!")
            except InvalidID :
                sg.Popup("You entered an invalid Client ID! Client IDs are not user IDs, you must obtain them by making an app in the discord developer portal. Click the Client ID Button below to go to the discord developer portal")

 

window.close()
