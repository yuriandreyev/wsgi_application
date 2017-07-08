'''This module contains wsgi application'''
def application(environ, start_response):
    '''This function returns assurance, that somebody is an engineer.
    Be careful, because fuction doesn't check if it is truth or not.
    '''
    status = '200 OK'
    output = '''
    <!DOCTYPE html>
    <html>
    <head>
    <style>

    h1:hover {color: DarkRed;}

    </style>
    </head>
    <body bgcolor="D3D3D3">
 
    <h1 align="center">Trust Me I'm An Engineer</h1>

    </body>
    </html>
    '''

    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
