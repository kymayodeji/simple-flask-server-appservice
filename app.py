from quart import Quart, render_template, request

# Create a flask app
app = Quart(
  __name__,
  template_folder='templates',
  static_folder='static'
)

@app.get('/')
async def index():
  return await render_template('index.html')

@app.get('/about')
async def about():
  return await render_template('about.html', location=request.args.get('location'), title="About")

@app.get('/hello')
async def hello():
  return await render_template('hello.html', name=request.args.get('name'))

@app.errorhandler(404)
async def handle_404(e):
    return await render_template('status.html', status='404'), 404


if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0', debug=True, port=8080)