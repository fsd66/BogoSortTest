import random
import time

class BogoSort:
        def __init__(self, sort_size, lower_bound, upper_bound):
                self.list_to_sort = []
                for i in range(sort_size):
                        self.list_to_sort.append(random.randint(lower_bound, upper_bound))

        def attempt_sort(self):
                random.shuffle(self.list_to_sort)

        def check_sort(self):
                check = self.list_to_sort[0]
                for n in range(len(self.list_to_sort)):
                        if self.list_to_sort[n] < check:
                                return False
                        check = self.list_to_sort[n]
                return True

        
        def print_list(self):
                print(self.list_to_sort)

if __name__ == '__main__':
        TIMES_TO_ITERATE = 10
        iteration = 0
        times = []
        while iteration < TIMES_TO_ITERATE:
                bg = BogoSort(10, 0, 10)
                bg.print_list()
                times_sorted = 0
                startTime = time.time()
                is_sorted = not bg.check_sort()
                while is_sorted:
                        bg.attempt_sort()
                        times_sorted += 1
                        is_sorted = not bg.check_sort()
                times.append(time.time() - startTime)
                print('List successfully sorted in {} shuffles!'.format(times_sorted))
                bg.print_list()
                print('Elapsed time: {}'.format(times[iteration]))
                print('Current average sort time: {}'.format(sum(times)/len(times)))
                print('\n')
                iteration += 1
        print('Final average sort time: {}\n'.format(sum(times)/len(times)))
