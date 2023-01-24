import cv2
from copy import deepcopy

class ImageConverter():

    def resize(self, fract_x, fract_y):
        self.img = cv2.resize(self.img, (0, 0), fx=fract_x, fy=fract_y)
        return None

    def makeDefSize(self):
        WIDTH_PIX = 1000
        height, width = self.img.shape
        self.img = cv2.resize(self.img, (WIDTH_PIX, round((WIDTH_PIX / width) * height)))
        return None

    def createSymbolsImage(self):
        new_img = deepcopy(self.img)
        for row in range(len(new_img)):
            for col in range(len(new_img[0])):
                if new_img[row][col] < 17:
                    new_img[row][col] = 0
                else:
                    new_img[row][col] = (new_img[row][col] - 17) // 24
        self.symb_img = new_img
        return None

    def getStringsFile(self):
        INVERTED_COLOR = False
        symbols = ['.', ',', ':', '+', '*', '?', '%', '$', '#', '@']

        if INVERTED_COLOR == False:
            symbols = symbols[::-1]
        img = self.symb_img
        upload_filename = self.filename[:self.filename.find('.')] + '.txt'
        self.upload_filename = upload_filename
        file = open('./website/uploads/' + upload_filename, mode='w', encoding='utf-8')
        for row in range(len(img)):
            for col in range(len(img[0])):
                file.write(symbols[img[row][col]])
            file.write('\n')
        file.close()


    def Convert(self, filename):
        self.filename = filename
        self.makeDefSize()
        self.resize(1, 0.33)
        self.createSymbolsImage()
        self.getStringsFile()



    
