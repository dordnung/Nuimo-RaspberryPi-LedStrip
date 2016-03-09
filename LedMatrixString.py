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

if __name__ == "__main__":
    LMS = LedMatrixString()
    print(LMS.getA())
