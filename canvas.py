def raiseError(*a, **k):
    raise NotImplementedError()

class Canvas:

    width=128
    height=64
    clear = raiseError
    plot = raiseError
    redraw = raiseError
    create_plotter = raiseError

    
    font = dict()
    font["A"] = [0b01110, 0b10001, 0b10001, 0b10001, 0b11111, 0b10001, 0b10001]
    font["B"] = [0x1E, 0x11, 0x11, 0x1E, 0x11, 0x11, 0x1E]
    font["C"] = [0x0E, 0x11, 0x10, 0x10, 0x10, 0x11, 0x0E]
    font["D"] = [0x1E, 0x11, 0x11, 0x11, 0x11, 0x11, 0x1E]
    font["E"] = [0x1F, 0x10, 0x10, 0x1E, 0x10, 0x10, 0x1F]
    font["F"] = [0x1F, 0x10, 0x10, 0x1E, 0x10, 0x10, 0x10]
    font["G"] = [0x0E, 0x11, 0x10, 0x13, 0x11, 0x11, 0x0F]
    font["H"] = [0x11, 0x11, 0x11, 0x1F, 0x11, 0x11, 0x11]
    font["I"] = [0x0E, 0x04, 0x04, 0x04, 0x04, 0x04, 0x0E]
    font["J"] = [0x07, 0x02, 0x02, 0x02, 0x02, 0x12, 0x0C]
    font["K"] = [0x11, 0x12, 0x14, 0x18, 0x14, 0x12, 0x11]
    font["L"] = [0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x1F]
    font["M"] = [0x11, 0x1B, 0x15, 0x15, 0x11, 0x11, 0x11]
    font["N"] = [0x11, 0x11, 0x19, 0x15, 0x13, 0x11, 0x11]
    font["O"] = [0x0E, 0x11, 0x11, 0x11, 0x11, 0x11, 0x0E]
    font["P"] = [0x1E, 0x11, 0x11, 0x1E, 0x10, 0x10, 0x10]
    font["Q"] = [0x0E, 0x11, 0x11, 0x11, 0x15, 0x12, 0x0D]
    font["R"] = [0x1E, 0x11, 0x11, 0x1E, 0x14, 0x12, 0x11]
    font["S"] = [0x0E, 0x11, 0x10, 0x0E, 0x01, 0x11, 0x0E]
    font["T"] = [0x1E, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04]
    font["U"] = [0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x0E]
    font["V"] = [0x11, 0x11, 0x11, 0x11, 0x11, 0x0A, 0x04]
    font["W"] = [0x11, 0x11, 0x11, 0x15, 0x15, 0x15, 0x0A]
    font["X"] = [0x11, 0x11, 0x0A, 0x04, 0x0A, 0x11, 0x11]
    font["Y"] = [0x11, 0x11, 0x11, 0x0A, 0x04, 0x04, 0x04]
    font["Z"] = [0x1F, 0x01, 0x02, 0x04, 0x08, 0x10, 0x1F]
    font["a"] = [0x00, 0x00, 0x0E, 0x01, 0x0F, 0x11, 0x0F]
    font["b"] = [0x10, 0x10, 0x16, 0x19, 0x11, 0x11, 0x1E]
    font["c"] = [0x00, 0x00, 0x0E, 0x10, 0x10, 0x11, 0x0E]
    font["d"] = [0x01, 0x01, 0x0D, 0x13, 0x11, 0x11, 0x0F]
    font["e"] = [0x00, 0x00, 0x0E, 0x11, 0x1F, 0x10, 0x0E]
    font["f"] = [0x06, 0x09, 0x08, 0x1C, 0x08, 0x08, 0x08]
    font["g"] = [0x00, 0x00, 0x0F, 0x11, 0x0F, 0x01, 0x0E]
    font["h"] = [0x10, 0x10, 0x16, 0x19, 0x11, 0x11, 0x11]
    font["i"] = [0x04, 0x00, 0x04, 0x0C, 0x04, 0x04, 0x0E]
    font["j"] = [0x02, 0x00, 0x06, 0x02, 0x02, 0x12, 0x0C]
    font["k"] = [0x10, 0x10, 0x12, 0x14, 0x18, 0x14, 0x12]
    font["l"] = [0x0C, 0x04, 0x04, 0x04, 0x04, 0x04, 0x0E]
    font["m"] = [0x00, 0x00, 0x1A, 0x15, 0x15, 0x15, 0x15]
    font["n"] = [0x00, 0x00, 0x16, 0x19, 0x11, 0x11, 0x11]
    font["o"] = [0x00, 0x00, 0x0e, 0x11, 0x11, 0x11, 0x0E]
    font["p"] = [0x00, 0x00, 0x1E, 0x11, 0x1E, 0x10, 0x10]
    font["q"] = [0x00, 0x00, 0x0D, 0x13, 0x0F, 0x01, 0x01]
    font["r"] = [0x00, 0x00, 0x16, 0x19, 0x10, 0x10, 0x10]
    font["s"] = [0x00, 0x00, 0x0E, 0x10, 0x0E, 0x01, 0x1E]
    font["t"] = [0x08, 0x08, 0x1C, 0x08, 0x08, 0x09, 0x06]
    font["u"] = [0x00, 0x00, 0x11, 0x11, 0x11, 0x13, 0x0D]
    font["v"] = [0x00, 0x00, 0x11, 0x11, 0x11, 0x0A, 0x04]
    font["w"] = [0x00, 0x00, 0x11, 0x11, 0x15, 0x15, 0x0A]
    font["x"] = [0x00, 0x00, 0x11, 0x0A, 0x04, 0x0A, 0x11]
    font["y"] = [0x00, 0x00, 0x11, 0x11, 0x0E, 0x01, 0x0E]
    font["z"] = [0x00, 0x00, 0x1F, 0x02, 0x04, 0x08, 0x1F]
    font["0"] = [0x0E, 0x11, 0x13, 0x15, 0x19, 0x11, 0x0E]
    font["1"] = [0x04, 0x0C, 0x04, 0x04, 0x04, 0x04, 0x0E]
    font["2"] = [0x0E, 0x11, 0x01, 0x02, 0x04, 0x08, 0x1F]
    font["3"] = [0x1F, 0x02, 0x04, 0x02, 0x01, 0x11, 0x0E]
    font["4"] = [0x02, 0x06, 0x0A, 0x12, 0x1F, 0x02, 0x02]
    font["5"] = [0x1F, 0x10, 0x1E, 0x01, 0x01, 0x11, 0x0E]
    font["6"] = [0x06, 0x08, 0x10, 0x1E, 0x11, 0x11, 0x0E]
    font["7"] = [0x1F, 0x11, 0x02, 0x04, 0x08, 0x08, 0x08]
    font["8"] = [0x0E, 0x11, 0x11, 0x0E, 0x11, 0x11, 0x0E]
    font["9"] = [0x0E, 0x11, 0x11, 0x0F, 0x01, 0x02, 0x0C]
    font[")"] = [0x08, 0x04, 0x02, 0x02, 0x02, 0x04, 0x08]
    font["!"] = [0x04, 0x04, 0x04, 0x04, 0x04, 0x00, 0x04]
    font["("] = [0x04, 0x08, 0x10, 0x10, 0x10, 0x08, 0x04]
    font["/"] = [0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x00]
    font[","] = [0x00, 0x00, 0x00, 0x00, 0x06, 0x02, 0x04]
    font["."] = [0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0x06]
    font[":"] = [0x00, 0x06, 0x06, 0x00, 0x06, 0x06, 0x00]
    font["@"] = [0x0E, 0x11, 0x01, 0x0C, 0x15, 0x15, 0x0E]
    font["%"] = [0x18, 0x19, 0x02, 0x04, 0x08, 0x13, 0x03]
    font["\x10"] = [0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10]
    font["\x11"] = [0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18]
    font["\x12"] = [0x1C, 0x1C, 0x1C, 0x1C, 0x1C, 0x1C, 0x1C]
    font["\x13"] = [0x1E, 0x1E, 0x1E, 0x1E, 0x1E, 0x1E, 0x1E]
    font["\x14"] = [0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F]
    font["\x15"] = [0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F]
    font["\x16"] = [0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07]
    font["\x17"] = [0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03]
    font["\x18"] = [0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01]
    font["\x0a"] = [0x18, 0x18, 0x00, 0x07, 0x08, 0x08, 0x07]
    font["\x0b"] = [0x18, 0x18, 0x00, 0x0F, 0x08, 0x0E, 0x08]
    font["\x0c"] = [0x00, 0x00, 0x1F, 0x0E, 0x04, 0x00, 0x00]
    font["\x0d"] = [0x00, 0x08, 0x0A, 0x0E, 0x0A, 0x08, 0x00]
    font["\x0e"] = [0x00, 0x02, 0x06, 0x0E, 0x06, 0x02, 0x00]
    font["\x0f"] = [0x00, 0x00, 0x04, 0x0E, 0x1F, 0x00, 0x00]
    font["-"] = [0x00, 0x00, 0x00, 0x1F, 0x00, 0x00]


    def line(self, x1, y1, x2, y2, plot):
        diffX = abs(x2 - x1)
        diffY = abs(y2 - y1)
        shiftX = 1 if (x1 < x2) else -1
        shiftY = 1 if (y1 < y2) else -1
        err = diffX - diffY
        while True:
            plot(x1, y1)
            if x1 == x2 and y1 == y2:
                break
            err2 = 2 * err
            if err2 > -diffY:
                err -= diffY
                x1 += shiftX
            if err2 < diffX:
                err += diffX
                y1 += shiftY

    def fill_rect(self, x1, y1, x2, y2, plot):
        for y in range(y1, y2):
            self.line(x1, y, x2, y, plot)

    def rect(self, x1, y1, x2, y2, plot):
        self.line(x1, y1, x2, y1, plot)
        self.line(x2, y1, x2, y2, plot)
        self.line(x2, y2, x1, y2, plot)
        self.line(x1, y2, x1, y1, plot)

    def write_char(self, x1, y1, char, plot):

        cur_y = y1
        if " " in char:
            return
        for r in self.font[char]:
            if (r & 0b10000) != 0: 
                plot(x1,cur_y)
            if (r & 0b01000) != 0:
                plot(x1+1,cur_y)
            if (r & 0b00100) != 0:
                plot(x1+2,cur_y)
            if (r & 0b00010) != 0:
                plot(x1+3,cur_y)
            if (r & 0b00001) != 0:
                plot(x1+4,cur_y)
            cur_y += 1

    def write_string(self, x1, y1, data, plot, wrap=True):
        cur_x = x1
        cur_y = y1
        for c in data:
            self.write_char(cur_x, cur_y, c, plot)
            cur_x += 6
            if cur_x > 122:
                if wrap:
                    cur_y = cur_y + 9
                    cur_x = x1
                else:
                    return


