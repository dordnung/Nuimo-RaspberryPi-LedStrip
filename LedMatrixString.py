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
        return "         " + \
              "    *    " + \
              "  *   *  " + \
              " *     * " + \
              "*       *" + \
              " *     * " + \
              "   * *   " + \
              "    *    " + \
              "         "

    def getColorBar(self, colorValue):
        bar = ""
        step = 255.0 / 9.0

        for x in self.frange(255.0 - step, 0, step):
            if colorValue >= x:
                bar += "*********"
            else:
                bar += "         "

        # First one is always on
        bar += "*********"
        return bar

    def frange(self, start, end, step):
      if step == 0:
          return

      # xrange for floats
      if start < end:
          while start < end:
              yield start
              start += step
      else:
          while start > end:
              yield start
              start -= step

if __name__ == "__main__":
    LMS = LedMatrixString()
    print(LMS.getA())
