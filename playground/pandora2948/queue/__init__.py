class Queue:
    data = list()

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        if self.is_empty():
            print("queue is empty!")

        else:
            print(self.data.pop())

    def is_empty(self):
        if len(self.data) == 0:
            return True

        else:
            return False

    def get_head(self):
        print(self.data[0])

    def get_queue(self):
        print(self.data)