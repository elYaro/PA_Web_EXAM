from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

#1 Yaro 
def get_tv_show(tv_show_id):
    return data_manager.execute_select('SELECT * FROM shows WHERE id = %(id)s;', {'id': tv_show_id})
# go to main.py

def get_seasons(tv_show_id):
    return data_manager.execute_select('''  SELECT seasons.id as season_id, seasons.title as season_title, shows.title as TV_show_title, shows.id FROM seasons
                                            JOIN shows ON seasons.show_id = shows.id
                                            WHERE shows.id = %(id)s
                                            ORDER BY seasons.title;''', {'id' : tv_show_id })


def get_total_episodes_number(tv_show_id):
    return data_manager.execute_select('''  SELECT COUNT(se.title) FROM shows sh
                                            JOIN seasons se ON sh.id = se.show_id
                                            JOIN episodes ep ON ep.season_id = se.id
                                            WHERE sh.id = %(id)s AND se.season_number >0;''', {'id'  : tv_show_id })


def get_total_seasons_number(tv_show_id):
    return data_manager.execute_select('''   SELECT se.season_number, se.title FROM seasons se
                                            JOIN shows sh ON se.show_id = sh.id
                                            WHERE sh.id = %(id)s AND se.season_number >=0;''', {'id'  : tv_show_id })