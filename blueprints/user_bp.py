import uuid
from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from forms import AddNoteForm, EditNoteForm
from models import Note, db
from rbac import role_required

user_blueprint = Blueprint('user_views', __name__, template_folder='templates')


@user_blueprint.route('/dashboard/user/<username>', methods=['GET'])
@login_required
@role_required('user')
def dashboard(username):
    notes = Note.query.filter_by(user_id=current_user.user_id).all()
    return render_template('user/dashboard.html', notes=notes)


@user_blueprint.route('/add-note', methods=['GET', 'POST'])
@login_required
@role_required('user')
def add_note():
    form = AddNoteForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        new_note = Note(
            note_id=str(uuid.uuid4()),
            title=form.title.data,
            content=form.content.data,
            date_created=datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            user_id=current_user.user_id
        )

        db.session.add(new_note)
        db.session.commit()
        flash("Note added.", category='success')
        return redirect(url_for('user_views.dashboard', username=current_user.username))

    return render_template('user/addnote.html', form=form)


@user_blueprint.route('/edit-note/<note_id>', methods=['GET', 'POST'])
@login_required
@role_required('user')
def edit_note(note_id):
    form = EditNoteForm(request.form)
    note = Note.query.filter_by(note_id=note_id).first()
    if request.method == 'POST' and form.validate_on_submit():
        note.title = form.edit_title.data
        note.content = form.edit_content.data,
        note.date_created = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        db.session.commit()
        flash("Note updated.", category='success')
        return redirect(url_for('user_views.dashboard', username=current_user.username))
    return render_template('user/editnote.html', form=form, note=note)


@user_blueprint.route('/delete-note/<note_id>', methods=['GET'])
@login_required
@role_required('user')
def delete_note(note_id):
    note = Note.query.filter_by(note_id=note_id).first()
    db.session.delete(note)
    db.session.commit()
    flash("Note deleted.", category='success')
    return redirect(url_for('user_views.dashboard', username=current_user.username))
