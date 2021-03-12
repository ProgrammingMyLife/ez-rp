from os import stat_result
import PySimpleGUI as sg
from pypresence import Presence
from pypresence.exceptions import InvalidArgument, InvalidID, InvalidPipe
import webbrowser
# Raven's Rich Presence Generator is a free open source program to generate custom discord rich presences. If anyone tries to sell you Raven's Rich Presence Generator, or tries to redistribute it as their own, please report it immediately. You are being scammed"

# All the stuff inside the window.
layout = [  [sg.Text("Raven\'s Rich Presence Generator")],
            [sg.Text("                                                                                                                                                                                                                                                                                 ", key="ERROR", text_color="red")], #This string is long.
            [sg.Text('Enter your client ID', key="~CLIENTID~"), 
            sg.InputText()],
            [sg.Text('Large Image ID:', key="~LIMAGEID~"),
            sg.InputText()],
            [sg.Text('Small Image ID:', key="~SIMAGEID~"),
            sg.InputText()],
            [sg.Text('Enter state of Rich Presence (Top text)', key="~RPCSTATE~"), 
            sg.InputText()],
            [sg.Text('Enter details of Rich Presence (2nd to bottom text)', key="~RPCDETAILS~"), 
            sg.InputText()],
            [sg.Text('(Optional) First button text', key="~firstbuttontext~", visible = True), 
            sg.InputText()],
            [sg.Text('(Mandatory if you put text for first button) First button URL', key="~firstbuttonurl~", visible = True), 
            sg.InputText()],
            [sg.Button('Run!'), sg.Button('Cancel'), sg.Button('Join Discord!'), sg.Button('Help'),],
            [sg.Text('Ravens Rich Presence Generator is a free open source program to generate custom discord rich presences. \n If anyone tries to sell you Ravens Rich Presence Generator, or tries to redistribute it as their own, please report it immediately.\n You are being scammed', justification='center')]
            ]
            
            

# Create the Window
window = sg.Window('Rich Presence', layout, icon="test.png", element_justification='c')

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

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


    elif window["~firstbuttontext~"] == None and not window["~firstbuttonurl~"] == None:
        window.Element("ERROR").Update("An error occured! Please make sure to add a URL!")

    elif window["~firstbuttonurl~"] == None and not window["~firstbuttontext~"] == None:
        window.Element("ERROR").Update("An error occured! Make sure to add a label for your button!")

    else:
        
        try :
        
            RPC = Presence(values[0])
            RPC.connect()
            RPC.update(state=values[3], details=values[4],large_image=values[1],small_image=values[2], buttons=[
                {
                    "label": values[5],
                    "url": values[6]

                }
            ])  # Set the presence
            window.Element("ERROR").Update("Success! Your rich presence is now up! Make sure to leave this window open.", text_color="green")

        
        except InvalidID :
            window.Element("ERROR").Update("An error occured! Please correct your Client ID!")

        except :
            try :
        
                RPC = Presence(values[0])
                RPC.connect()
                RPC.update(state=values[3], details=values[4], large_image=values[1], small_image=values[2])
                window.Element("ERROR").Update("Success! Your rich presence is now up! Make sure to leave this window open.", text_color="green")

        
            except InvalidID :
                window.Element("ERROR").Update("An error occured! Please correct your Client ID!")

 

window.close()
