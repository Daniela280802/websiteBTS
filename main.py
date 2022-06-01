from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_session import Session


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

socketio = SocketIO(app, manage_session=True)


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/SK')
def sk():
    return render_template('SK.html')


@app.route('/member')
def member():
    return render_template('member.html')


@app.route('/universe')
def world():
    return render_template('universe.html')


@app.route('/webtoon')
def webtoon():
    return render_template('webtoon.html')


@app.route('/awards')
def awards():
    return render_template('awards.html')


@app.route('/show')
def show():
    return render_template('show.html')


@app.route('/school')
def school():
    return render_template('school.html')


@app.route('/wild')
def wild():
    return render_template('wild.html')


@app.route('/youth')
def youth():
    return render_template('youth.html')


@app.route('/wings')
def wings():
    return render_template('wings.html')


@app.route('/love')
def love():
    return render_template('love.html')


@app.route('/btsw')
def btsw():
    return render_template('btsw.html')


@app.route('/mots')
def mots():
    return render_template('mots.html')


@app.route('/be')
def be():
    return render_template('be.html')


@app.route('/dynamite')
def dynamite():
    return render_template('dynamite.html')


@app.route('/ph2cool4school')
def ph2cool4school():
    return render_template('ph2cool4school.html')


@app.route('/phrul8')
def phrul8():
    return render_template('phrul8.html')


@app.route('/phluvaffair')
def phluvaffair():
    return render_template('phluvaffair.html')


@app.route('/phhyyh1')
def phhyyh1():
    return render_template('phhyyh1.html')


@app.route('/phhyyh2')
def phhyyh2():
    return render_template('phhyyh2.html')


@app.route('/phforever')
def phforever():
    return render_template('phforever.html')


@app.route('/phwings')
def phwings():
    return render_template('phwings.html')


@app.route('/phwalkalone')
def phwalkalone():
    return render_template('phwalkalone.html')


@app.route('/phher')
def phher():
    return render_template('phher.html')


@app.route('/phtear')
def phtear():
    return render_template('phtear.html')


@app.route('/phanswer')
def phanswer():
    return render_template('phanswer.html')


@app.route('/phbtsw')
def phbtsw():
    return render_template('phbtsw.html')


@app.route('/ph7')
def ph7():
    return render_template('ph7.html')


@app.route('/phpersona')
def phpersona():
    return render_template('phpersona.html')


@app.route('/phbe')
def phbe():
    return render_template('phbe.html')


@app.route('/phdynamite')
def phdynamite():
    return render_template('phdynamite.html')


@app.route('/phbutter')
def phbutter():
    return render_template('phbutter.html')


@app.route('/phptd')
def phptd():
    return render_template('phptd.html')


@app.route('/logchat', methods=['GET', 'POST'])
def index():
    return render_template('logchat.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        username = request.form['username']
        room = request.form['room']
        session['username'] = username
        session['room'] = room
        return render_template('chat.html', session=session)
    else:
        if session.get('username') is not None:
            return render_template('chat.html', session=session)
        else:
            return redirect(url_for('logchat'))


@socketio.on('join', namespace='/chat')
def join(message):
    room = session.get('room')
    join_room(room)
    emit('status', {'msg':  session.get('username') + ' now with us, so say HI.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('room')
    emit('message', {'msg': session.get('username') + ' : ' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room')
    username = session.get('username')
    leave_room(room)
    session.clear()
    emit('status', {'msg': username + ' has left the room.'}, room=room)


if __name__ == '__main__':
    socketio.run(app)
