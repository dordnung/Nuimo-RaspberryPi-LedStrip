from PIL import Image
import random
import math

class Wheel:
  bg_color = 0x888888
  img_size = 100
  img_half = img_size / 2;
  inner_radius = 0
  outer_radius = 50

  color_wheel = [
    [0xff, 0x00, 0xff], 
    [0xff, 0x00, 0x00], 
    [0xff, 0xff, 0x00], 
    [0x00, 0xff, 0x00], 
    [0x00, 0xff, 0xff], 
    [0x00, 0x00, 0xff], 
    [0xff, 0x00, 0xff]] # one extra so less wrap-around logic is required

  def make_color(self, base, adj, ratio, shade):
    output = 0x0
    bit = 0
    """
    Go through each bit of the colors adjusting blue with blue, red with red,
    green with green, etc.
    """
    for pos in xrange(3):
      base_chan = self.color_wheel[base][pos]
      adj_chan = self.color_wheel[adj][pos]
      new_chan =  int(round(base_chan * (1 - ratio) + adj_chan * ratio))
      
      # now alter the channel by the shade
      if shade < 1:
        new_chan = new_chan * shade
      elif shade > 1:
        shade_ratio = shade - 1
        new_chan = (0xff * shade_ratio) + (new_chan * (1 - shade_ratio))

      output = output + (int(new_chan) << bit)
      bit = bit + 8
    return output

  def paintWheelAndGetColorAtAngle(self,angle1):
    im = Image.new('RGB', (self.img_size, self.img_size), self.bg_color)
    for x in xrange(self.img_size):
      for y in xrange(self.img_size):
        #dist = abs(math.sqrt((x - self.img_half) ** 2 + (y - self.img_half) ** 2));
        dist = self.outer_radius/2
        if dist < self.inner_radius or dist > self.outer_radius:
          continue;
        shade = 2 * (dist - self.inner_radius) / (self.outer_radius - self.inner_radius)
        #print(shade)
        # probably an error in my logic, but the center line is getting
        # inverted. so, manually set it if it's not right
        if x - self.img_half == 0:
          angle = angle = -90
          if y > self.img_half:
            angle = 90
        else: 
          angle = math.atan2((y - self.img_half), (x - self.img_half)) * 180 / math.pi
      
        angle = (angle + 30) % 360
          
        idx = angle / 60
        if idx < 0: 
          idx = 6 + idx
        base = int(round(idx))

        adj = (6 + base + (-1 if base > idx else 1)) % 6

        ratio = max(idx, base) - min(idx, base)

        color = self.make_color(base, adj, ratio, shade)
         
        im.putpixel((x, y), color)

    """for angle in xrange(360):
      x = dist * math.cos(angle) + self.outer_radius
      y = dist * math.sin(angle) + self.outer_radius
      x = int(x)
      y = int(y)

      im.putpixel((x, y), (0, 0, 0))"""
    x = dist * math.cos(angle1) + self.outer_radius
    y = dist * math.sin(angle1) + self.outer_radius
    
    return im.getpixel((x,y))

if __name__ == "__main__":
  w = Wheel()
  print(w.paintWheelAndGetColorAtAngle(0))
  print(w.paintWheelAndGetColorAtAngle(90))

#im = Image.new('RGB', (img_size, img_size), paintWheelAndGetColorAtAngle(0))
#im.show()
#im.save('gamut.png', 'PNG')
#im.show()