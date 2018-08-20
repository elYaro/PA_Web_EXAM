from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')



def get_episodes(season_id):
    return data_manager.execute_select('''  SELECT ep.id AS episode_id, ep.title As episode_title, ep.episode_number, ep.overview, ep.season_id, se.title AS season_title, sh.id AS show_id, sh.title AS show_title FROM episodes ep
                                            JOIN seasons se ON ep.season_id = se.id
                                            JOIN shows sh ON sh.id = se.show_id
                                            WHERE se.id = %(id)s;''', {'id' : season_id })


def get_tv_show(tv_show_id):
    return data_manager.execute_select('SELECT * FROM shows WHERE id = %(id)s;', {'id': tv_show_id})


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

