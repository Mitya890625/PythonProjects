class Programmer:
    def __init__(self, salary, work_hours):
        self.salary = salary
        self.work_hours = work_hours
    def __del__(self):
        print("oof, " + str(self.salary) +', ' + str(self.work_hours))
    def compare(self, other):
        if self.salary > other.salary:
            return "more"
        else:
            return "less"
        if self.work_hours > other.work_hours:
            return 'longer'
        else:
            return 'shorter'
def main():
    prog1 = Programmer(2500, 8)
    del prog1
    prog2 = Programmer(3000, 10)
    #print(prog2.compare(prog1))





main()

