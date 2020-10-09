from flask import Blueprint, abort, render_template, jsonify
from flaskdraft.models import Player
from flaskdraft.players.forms import PlayerForm
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskdraft import db, bcrypt
from flaskdraft.models import UserInfo, Post 
from flaskdraft.users.forms import (RegisterForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm, FeedbackForm)
from flaskdraft.users.utils import save_picture, send_reset_email


players = Blueprint('players', __name__)

#------------------VEHICLE ENDPOINT------------------#



@players.route('/players/add', methods=['GET','POST'])
def post_players():

    form = PlayerForm()
    if form.validate_on_submit():
        return render_template('post_player.html', message = 'Player has been added!', form = form )
    return render_template('post_player.html', title='Add Player', form=form)


#POSTMAN APPROVED
# VEHICLES (DELETE) #maybe
@players.route('/players/<int:id>', methods=["DELETE"])
def delete_vehicle(id):
    try:
        #grab all questions
        players = Player.query.filter(Player.id == id).one_or_none()    


        #if no questions abort 422
        if players is None:
            abort(422)
        
        #else delete
        else:
            players.delete()


        #json 
        return jsonify({
            'success': True,
            'deleted': id,
            }), 200

    except Exception:
        abort(422)