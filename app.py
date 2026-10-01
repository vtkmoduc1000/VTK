from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
  return 'Xin chào! Chương trình Python của tôi đã chạy trên web.'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
