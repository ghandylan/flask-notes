from flask import Blueprint, redirect, url_for, request, render_template, flash
from flask_login import login_user, login_required, current_user

from rbac import role_required

user_blueprint = Blueprint('user_views', __name__, template_folder='templates')


@user_blueprint.route('/dashboard/user/<username>')
@login_required
@role_required('user')
def dashboard(username):
    return render_template('user/dashboard.html')
