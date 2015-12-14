class BusinessTasks:

    def getTask(self, list, n):
        data = []
        for x in list:
            data.append(x)
        startIndex = 0
        increase = n - 1
        while len(data) > 1:
            removeIndex = ((startIndex + increase) % (len(data)))
            del data[removeIndex]
            startIndex = removeIndex % len(data)
        return data[0]
