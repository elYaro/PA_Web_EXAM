from flask import Flask, render_template, url_for
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/seasons/<tv_show_id>')
def seasons(tv_show_id):
    seasons                     = queries.get_seasons(tv_show_id)
    total_episodes_number       = queries.get_total_episodes_number(tv_show_id)
    total_seasons_number        = queries.get_total_seasons_number(tv_show_id)
    return render_template('seasons.html', seasons = seasons, total_episodes_number = total_episodes_number, total_seasons_number = total_seasons_number )


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()

# developer branch created
