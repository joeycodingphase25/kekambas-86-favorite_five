from app import app
from flask import render_template
from app.forms import SignUpForm

@app.route('/')
def index():
    title = 'Home'
    user = {'id': 1, 'username': 'These are my current favorite pianists -- jojo', 'email': 'brians@codingtemple.com'}
    posts = [
        {
            'id': 1,
            'title': 'Franz Liszt',
            'body': 'The famous pianist that invented the paino recital, and my hero.',
            'author': '1811 to 1886',
            'link' : 'https://www.biography.com/musician/franz-liszt'
        },
        {
            'id': 2,
            'title': 'Frederic Chopin',
            'body': 'Friends with Liszt, and made some of the most beautiful music ever listened too.',
            'author': '1810 to 1849',
            'link' : 'https://www.biography.com/musician/frederic-chopin'
        },
        {
            'id': 3,
            'title': 'Frederick Burgmuller',
            'body': 'A criminally underatted pianist. He never wanted fame, yet wrote amazing pieces for children.',
            'author': '1806 to 1874',
            'link' :'https://prabook.com/web/johann_friedrich_franz.burgmuller/725103'
        },
        {
            'id': 4,
            'title': 'Muzio Clementi',
            'body': 'A very influential Italian pianist who made several joyous pieces, yet it overlooked in the mainstream',
            'author': '1752 to 1852',
            'link' :'https://www.britannica.com/biography/Muzio-Clementi'
        }
    ]
    return render_template('index.html', current_user=user, title=title, posts=posts)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    title = 'Sign Up'
    form = SignUpForm()
    return render_template('signup.html', title=title, form=form)


@app.route('/login')
def login():
    title = 'Log In'
    return render_template('login.html', title=title)