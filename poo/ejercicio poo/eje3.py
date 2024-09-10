
class StoryTime:
    def __init__(self, fileUrl):
        self.fileUrl = fileUrl

    def readStory(self):
        with open(self.fileUrl or "archivos\\texto.txt", "r", encoding="UTF-8") as file:
            print(file.read())

    def writeStory(self):
        myStory = input("Escribe tu Historia : ")
        with open(self.fileUrl, "w", encoding="UTF-8") as file:
            file.writelines([myStory])



myStoryTime = StoryTime("poo\\ejercicio poo\\myHistory.txt")
myStoryTime2 = StoryTime("poo\\ejercicio poo\\myHistory2.txt")
myStoryTime3 = StoryTime("poo\\ejercicio poo\\myHistory3.txt")

myStoryTime.writeStory()
myStoryTime2.writeStory()
myStoryTime3.writeStory()


