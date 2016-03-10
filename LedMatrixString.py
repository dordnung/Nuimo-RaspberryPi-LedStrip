#!/usr/bin/env python
class LedMatrixString:

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

    def getR(self):
        return "         " + \
            "   ***   " + \
            "   *  *  " + \
            "   *  *  " + \
            "   ***   " + \
            "   **    " + \
            "   * *   " + \
            "   *  *  " + \
            "         "

    def getG(self):
        return "         " + \
            "    ***  " + \
            "   *     " + \
            "   *     " + \
            "   * **  " + \
            "   *  *  " + \
            "   *  *  " + \
            "    ***  " + \
            "         "

    def getB(self):
        return "         " + \
            "   ***   " + \
            "   *  *  " + \
            "   *  *  " + \
            "   ***   " + \
            "   *  *  " + \
            "   *  *  " + \
            "   ***   " + \
            "         "

    def getA(self):
        return "         " + \
            "    *    " + \
            "   * *   " + \
            "  *   *  " + \
            "  *****  " + \
            "  *   *  " + \
            "  *   *  " + \
            "  *   *  " + \
            "         "

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
        return "    *    " + \
            "   * *   " + \
            "  *   *  " + \
            " *     * " + \
            "*       *" + \
            " *     * " + \
            "  *   *  " + \
            "   * *   " + \
            "    *    "

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
    print(LMS.getA())
    LMS.printMatrix(LMS.getA())
