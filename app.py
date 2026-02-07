from flask import Flask, render_template, request, jsonify
import sys
import io
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get('code', '')
    
    # Перехватываем стандартный вывод (print)
    output = io.StringIO()
    sys.stdout = output
    
    try:
        # Выполняем код
        exec(code)
        result = output.getvalue()
    except Exception as e:
        result = str(e)
    finally:
        sys.stdout = sys.__stdout__
        
    return jsonify({'output': result})

if __name__ == '__main__':
    # Хостинг сам пробросит нужный порт через переменную PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)