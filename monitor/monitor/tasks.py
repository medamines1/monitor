
from myapp.server import _run_server
@app.task(bind=True)
def run_task_redis(self):
   _run_server()