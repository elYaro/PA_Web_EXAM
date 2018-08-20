from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_episodes(season_id):
    return data_manager.execute_select('''  SELECT ep.id AS episode_id, ep.title As episode_title, ep.episode_number, ep.overview, ep.season_id, se.title AS season_title, sh.id AS show_id, sh.title AS show_title FROM episodes ep
                                            JOIN seasons se ON ep.season_id = se.id
                                            JOIN shows sh ON sh.id = se.show_id
                                            WHERE se.id = %(id)s;''', {'id' : season_id })
