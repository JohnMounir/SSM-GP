import gc
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from WordCorrection import WordCorrection
class Pre_Processing:
    print("Pre Processing Started")
    def __init__(self, List):
        self.List = List

    def MainFunction(self):
        self.Tokenization()
        self.Stemming()
        self.RemoveEncoding()
        self.WordCorrection()
        print("PreProcessing Finished")
        return self.NewProcessedList
    def WordCorrection(self):
        WordCorrection_Object = WordCorrection()
        self.NewProcessedList = []

        for i in range(len(self.ProcessedList)):
            Text = ""
            for j in range(len(self.ProcessedList[i])):
                Text = Text+self.ProcessedList[i][j]+" "
            self.NewProcessedList.append(Text)
        del self.ProcessedList
        gc.collect()
        #for i in range(len(self.NewProcessedList)):
         #   self.NewProcessedList[i] = WordCorrection_Object.Correction(self.NewProcessedList[i])

    def Tokenization(self):
        self.ProcessedList = [[]]
        for ListItem in self.List:
            if(ListItem=="ans"): #added by John
                self.ProcessedList[0]=nltk.word_tokenize(ListItem)#added by John
                continue#added by John
            elif (len(ListItem)>0):
                self.ProcessedList.append(nltk.word_tokenize(ListItem))
            else:#added by John
                self.ProcessedList.append("")#added by John
        del self.List
        gc.collect()

    def Stemming(self):
        Stemmer = PorterStemmer()

        for i in range(len(self.ProcessedList)):
            for j in range(len(self.ProcessedList[i])):
                self.ProcessedList[i][j] = Stemmer.stem(self.ProcessedList[i][j])



    def Lemitization(self):
        Lem = WordNetLemmatizer()
        for i in range(len(self.ProcessedList)):
            for j in range(len(self.ProcessedList[i])):
                self.ProcessedList[i][j] = Lem.lemmatize(self.ProcessedList[i][j])

    def RemoveEncoding(self):
        for i in range(len(self.ProcessedList)):
            for j in range(len(self.ProcessedList[i])):
                Word = self.ProcessedList[i][j]
                for letter in Word:
                    if ord(letter) > 127:
                        del self.ProcessedList[i][j]
                        break