import threading
import time
import random


class Doctor(threading.Thread):
    def __init__(self, number, left_screwdriver, right_screwdriver):
        threading.Thread.__init__(self)
        self.number = number
        self.left_screwdriver = left_screwdriver
        self.right_screwdriver = right_screwdriver

    def run(self):
        while True:
            if self.left_screwdriver.acquire():
                if self.right_screwdriver.acquire(blocking=False):
                    print(f"Doctor {self.number}: BLAST!")
                    self.left_screwdriver.release()
                    self.right_screwdriver.release()
                    break
                else:
                    print("not now")
                    self.left_screwdriver.release()
            # time.sleep(random.random() / 2)


class Screwdriver():
    def __init__(self):
        self.lock = threading.Lock()


def main():
    screwdrivers = [Screwdriver() for _ in range(5)]

    doctors = []
    for i in range(5):
        left = screwdrivers[i]
        right = screwdrivers[(i+1) % 5]
        doctor = Doctor(i+9, left.lock, right.lock)
        doctors.append(doctor)

    random.shuffle(doctors)
    for doctor in doctors:
        doctor.start()


if __name__ == '__main__':
    main()
