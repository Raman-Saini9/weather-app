import PySimpleGUI as sg
from data import get_info
sg.theme('Black')
layout = [[sg.Text("City"),sg.Input(key='-CITY-')],
            [sg.Text(size=(40,6), key='-OUTPUT-')],
            [sg.Button('Search'), sg.Button('Quit')]]

window = sg.Window('Weather Today',layout)
while True:
    event, values = window.read()	    
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    if event == 'Search':	
        try:
            info = get_info(values['-CITY-'])
            # print(get_info(values['-CITY-']))
            information_1 = f'City\t: {info[0]}\t\twind speed : {info[8]}\nCountry\t: {info[1]}\t\thumidity : {info[7]}\nCurrent Temp : {info[2]} C\n'
            information_2 = f'Max temp  : {info[3]} C\nMin temp  : {info[4]} C\n'
            information_3 = f'Description  : {info[6]}, {info[5]}'
            window['-OUTPUT-'].update(information_1+information_2+information_3)
        except:
            window['-OUTPUT-'].update(f"No data for {values['-CITY-']}")

window.close()