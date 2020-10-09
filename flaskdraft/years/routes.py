from flask import Blueprint, render_template, request, abort, flash
from flaskdraft.models import Year, Player
from flaskdraft.years.forms import SelectMockYear


mock = Blueprint('mock', __name__)


#-------------------------MOCK DRAFT YEAR--------------------------#

#not finished
#maybe at a fitler bar to optimize searches

@mock.route('/mock-draft', methods=['GET', 'POST'])
def select_year():
    
    #Request Option parameter 'page' and set it to int(throws value error if not int) 
    page = request.args.get('page', 1, type=int)
    
    #paginate and lists post by most recent
    players = Player.query.order_by(Player.year_rank).filter_by(year_id = '2020').paginate(page=page, per_page = 10)
    
    #Form
    form = SelectMockYear()

    #made it the same value but there probable better way
    form.mock.choices = [(g.year, g.year) for g in Year.query.order_by(Year.id)]
    
    if request.method == 'POST':
        value = form.mock.data
        players = Player.query.order_by(Player.year_rank).filter_by(year_id = value).paginate(page=page, per_page = 10)
        flash('Mock Has Been Updated!', 'success')
        return render_template('year.html', form=form, title=value, players=players, notside = "this is to get rid of sidebar") 
    
#return results
    return render_template('year.html', form=form, players=players, notside = "this is to get rid of sidebar")

     
