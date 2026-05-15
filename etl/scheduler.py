import schedule
import time
from pipeline import run

schedule.every(30).minutes.do(run)

print("Scheduler ativo. Pipeline rodando a cada 30 minutos.")
print("Pressione Ctrl+C para parar.\n")

run()

while True:
    schedule.run_pending()
    time.sleep(60)
