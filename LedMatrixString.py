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
        ret = " **   ** " + \
              " * * * * " + \
              "  *****  " + \
              "  *   *  " + \
              " * * * * " + \
              " *  *  * " + \
              " * * * * " + \
              "  *   *  " + \
              "   ***   "
        return ret

    def getR(self):
        ret = "         " + \
              "   ***   " + \
              "   *  *  " + \
              "   *  *  " + \
              "   ***   " + \
              "   **    " + \
              "   * *   " + \
              "   *  *  " + \
              "         "
        return ret

    def getG(self):
        ret = "         " + \
              "    ***  " + \
              "   *     " + \
              "   *     " + \
              "   * **  " + \
              "   *  *  " + \
              "   *  *  " + \
              "    ***  " + \
              "         "
        return ret

    def getB(self):
        ret = "         " + \
              "   ***   " + \
              "   *  *  " + \
              "   *  *  " + \
              "   ***   " + \
              "   *  *  " + \
              "   *  *  " + \
              "   ***   " + \
              "         "
        return ret

    def getA(self):
        ret = "         " + \
              "    *    " + \
              "   * *   " + \
              "  *   *  " + \
              "  *****  " + \
              "  *   *  " + \
              "  *   *  " + \
              "  *   *  " + \
              "         "
        return ret

if __name__ == "__main__":
    LMS = LedMatrixString()
    print(LMS.getA())
