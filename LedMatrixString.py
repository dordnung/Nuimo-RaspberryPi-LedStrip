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

if __name__ == "__main__":
    LMS = LedMatrixString()
    print(LMS.getA())
