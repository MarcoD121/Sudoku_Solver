from flask import Flask, request, jsonify
from flask_cors import CORS
import SudokuSolver

app = Flask(__name__)
CORS(app, resources={r"/solve": {"origins": "http://localhost:8080"}})

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    
    board = data['board']

    solved_board = SudokuSolver.solve(board)
    
    return jsonify(solved_board)

if __name__ == '__main__':
    app.run(debug=True)