import pyodbc

def get_all_games():
    connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-MVCD165;DATABASE=project'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    id = 2
    get_all_info_about_game = 'exec GetAllInfoOfGame'
    cursor.execute(f'{get_all_info_about_game} {id}')
    result = cursor.fetchone()
    return(result)