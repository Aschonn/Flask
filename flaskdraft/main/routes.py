from flask import render_template, request, Blueprint
from sqlalchemy import desc
from flaskdraft.models import Post

main = Blueprint('main', __name__)

#----------------------------HOME ENDPOINT----------------------------#


@main.route('/')
@main.route('/home')
def home():
    #Request Option parameter 'page' and set it to int(throws value error if not int) 
    page = request.args.get('page', 1, type=int)
    #paginate and lists post by most recent
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page = 5)


    return render_template('home.html', title = 'Home', posts = posts)


@main.route('/about')
def about():
    return render_template('about.html', title='About', notside = "this is to get rid of sidebar")