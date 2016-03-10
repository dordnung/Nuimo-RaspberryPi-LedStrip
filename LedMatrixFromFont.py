#!/usr/bin/env python

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class LedMatrixStringFromFont:

    def getFromLetter(self, letter, font, size, pos):
        img = img = Image.new('RGB', (9, 9), "white")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font, size)
        draw.text(pos, letter[0], (0, 0, 0), font=font)
        # img.show()
        pixels = img.load()

        ret = ''
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if (pixels[j, i][0] < 140):
                    ret += '*'
                else:
                    ret += ' '

        return ret

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
    LMSFF = LedMatrixStringFromFont()

    LMSFF.printMatrix(LMSFF.getFromLetter('A', 'fonts/arial.ttf', 11, (0, -2)))

    LMSFF.printMatrix(LMSFF.getFromLetter(
        u'\uf047', 'fonts/fontawesome-webfont.ttf', 9, (0, 0)))

    LMSFF.printMatrix(LMSFF.getFromLetter(
        u'\uf294', 'fonts/fontawesome-webfont.ttf', 10, (2, 0)))
