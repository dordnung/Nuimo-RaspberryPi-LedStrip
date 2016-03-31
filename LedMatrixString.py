#!/usr/bin/env python

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class LedMatrixString:

    def getFromLetter(self, letter, font, size, pos):
        img = Image.new('RGB', (9, 9), "white")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font, size)
        draw.text(pos, letter[0], (0, 0, 0), font=font)
        # img.show()
        pixels = img.load()

        ret = ''
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if (pixels[j, i][0] < 135):
                    ret += '*'
                else:
                    ret += ' '

        return ret

    def getArialLetter(self, letter):
        return self.getFromLetter(letter, 'fonts/arial.ttf', 11, (1, -2))

    def getPi(self):
        return "         " + \
            " ***     " + \
            " *  * *  " + \
            " *  *    " + \
            " ***  *  " + \
            " *    *  " + \
            " *    *  " + \
            " *    *  " + \
            "         "

    def getRaspberry(self):
        return " **   ** " + \
            " * * * * " + \
            "  *****  " + \
            "  *   *  " + \
            " * * * * " + \
            " *  *  * " + \
            " * * * * " + \
            "  *   *  " + \
            "   ***   "

    def getOn(self):
        return "         " + \
            "    *    " + \
            "    *    " + \
            "    *    " + \
            "    *    " + \
            "    *    " + \
            "    *    " + \
            "    *    " + \
            "         "

    def getOff(self):
        return self.getFromLetter(u'\uf011', 'fonts/fontawesome-webfont.ttf', 9, (1, 0))

    def getColorBar(self, colorValue):
        bar = ""
        step = 255 / 9
        start = 255 - step
        end = 255 - 9 * step

        for x in xrange(start, end, -step):
            if colorValue >= x:
                bar += "*********"
            else:
                bar += "         "

        # First one is always on
        bar += "*********"
        return bar

    def printMatrix(self, matrixStr):
        print(">" + matrixStr[0 * 9:1 * 9] + "<")
        print(">" + matrixStr[1 * 9:2 * 9] + "<")
        print(">" + matrixStr[2 * 9:3 * 9] + "<")
        print(">" + matrixStr[3 * 9:4 * 9] + "<")
        print(">" + matrixStr[4 * 9:5 * 9] + "<")
        print(">" + matrixStr[5 * 9:6 * 9] + "<")
        print(">" + matrixStr[6 * 9:7 * 9] + "<")
        print(">" + matrixStr[7 * 9:8 * 9] + "<")
        print(">" + matrixStr[8 * 9:10 * 9] + "<")

if __name__ == "__main__":
    LMS = LedMatrixString()

    LMS.printMatrix(LMS.getArialLetter('R'))
    LMS.printMatrix(LMS.getArialLetter('G'))
    LMS.printMatrix(LMS.getArialLetter('B'))
    LMS.printMatrix(LMS.getArialLetter('A'))
    LMS.printMatrix(LMS.getOff())

    LMS.printMatrix(LMS.getFromLetter(
        u'\uf047', 'fonts/fontawesome-webfont.ttf', 9, (0, 0)))

    LMS.printMatrix(LMS.getFromLetter(
        u'\uf294', 'fonts/fontawesome-webfont.ttf', 10, (2, 0)))
