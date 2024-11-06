from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initial board state
board = [''] * 9
current_player = 'X'
winner = None

def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combinations:
        a, b, c = combo
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

@app.route('/', methods=['GET', 'POST'])
def home():
    global board, current_player, winner

    if request.method == 'POST':
        index = int(request.form.get('index'))
        if board[index] == '' and winner is None:
            board[index] = current_player
            winner = check_winner(board)
            current_player = 'O' if current_player == 'X' else 'X'

    return render_template('index.html', board=board, winner=winner)

@app.route('/reset')
def reset():
    global board, current_player, winner
    board = [''] * 9
    current_player = 'X'
    winner = None
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
