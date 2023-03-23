import random
import time


def emit_gel():
    pressure = random.randint(50, 100)
    while True:
        step = yield pressure
        pressure += random.uniform(0, step)


def valve(emit_gel, step):
    pressure = next(emit_gel)
    while True:
        if pressure < 20 or pressure > 80:
            step = -step
        if pressure > 90 or pressure < 10:
            emit_gel.close()
            print("Emergency break activated!")
            return
        pressure = emit_gel.send(step)
        print("Pressure:", round(pressure, 3))
        time.sleep(0.01)


if __name__ == "__main__":
    gen = emit_gel()
    valve(gen, 1)
