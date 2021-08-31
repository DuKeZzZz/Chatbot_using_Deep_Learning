import PySimpleGUI as sg


def mail_GUI():
    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Enter Details below:(Use TAB to goto next input)')],
              [sg.Text('Gmail Username :', size=(15, 1)), sg.In('', key='username')],
              [sg.Text('Password :', size=(15, 1)), sg.In('', key='password', password_char='*')],
              [sg.Text('Receiver''s address :', size=(15, 1)), sg.In('', key='receiver')],
              [sg.Text('Subject :', size=(15, 1)), sg.In('', key='subject')],
              [sg.Text('Body :', size=(15, 1)), sg.Multiline('', size=(70, 10), key='body')],
              [sg.Button('Ok', size=(10, 1), bind_return_key=True), sg.Button('Cancel', size=(10, 1))]]

    # Create the Window
    window = sg.Window('Mail Sender', font='Helvetica 14').Layout(layout)

    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        window.close()
        return {'username': ''}
    window.close()
    return values


def weather_GUI():
    sg.theme('DarkAmber')

    layout = [[sg.Text('Enter City Name :', size=(15, 1)), sg.In('', key='city')],
              [sg.Button('Ok', size=(10, 1), bind_return_key=True), sg.Button('Cancel', size=(10, 1))]]

    window = sg.Window('Weather', font='Helvetica 14').Layout(layout)

    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        window.close()
        return {'city': ''}

    window.close()
    return values


