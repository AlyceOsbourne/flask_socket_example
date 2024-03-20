import application as app

@app.route('/')
def index():
    return app.render_template_string("""
<ul id="messages"></ul>
<input type="text" id="message" placeholder="Enter message">
<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js" integrity="sha512-q/dWJ3kcmjBLU4Qc47E4A9kTB4m3wuTY7vkFJDTZKjTs8jhyGQnaUrxa0Ytd0ssMZhbNua9hE+E7Qv1j+DyZwA==" crossorigin="anonymous"></script>
<script>
    var socket = io();
    var messages = document.getElementById('messages');
    var message = document.getElementById('message');
    message.focus();
    message.addEventListener('keypress', function(event) {
        if (event.keyCode === 13) {
            socket.emit('message', message.value);
            message.value = '';
        }
    });
    socket.on('message', function(data) {
        var li = document.createElement('li');
        li.appendChild(document.createTextNode(data));
        messages.appendChild(li);
    });
</script>
    """)

@app.on('message')
def message(data):
    app.emit('message', data)
    
@app.on('connect')
def connect():
    app.emit('message', 'Connected')
    
@app.on('disconnect')
def disconnect():
    app.emit('message', 'Disconnected')

if __name__ == '__main__':
    app.run()