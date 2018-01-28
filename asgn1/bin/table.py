import textwrap

class Table:

    def __init__(self,
                 contents,
                 wrap,
                 wrapAtWordEnd = True,
                 colDelim = "",
                 rowDelim = ""):

        self.contents = contents
        self.wrap = wrap
        self.colDelim = colDelim
        self.wrapAtWordEnd = wrapAtWordEnd

        # Extra rowDelim characters where colDelim characters are
        p = len(self.colDelim) * (len(self.contents[0]) - 1)

        # Line gets too long for one concatenation
        self.rowDelim = self.colDelim
        self.rowDelim += rowDelim * (self.wrap * max([len(i) for i in self.contents]) + p)
        self.rowDelim += self.colDelim + "\n"


    def withTextWrap(self):

        print(self.wrap)

        string = self.rowDelim

        # Restructure to get textwrap.wrap output for each cell
        l = [[textwrap.wrap(col, self.wrap) for col in row] for row in self.contents]

        for row in l:
            for n in range(max([len(i) for i in row])):
                string += self.colDelim
                for col in row:
                    if n < len(col):
                        string += col[n].ljust(self.wrap)
                    else:
                        string += " " * self.wrap
                    string += self.colDelim
                string += "\n"
            string += self.rowDelim

        return string

    def __str__(self):
        return self.withTextWrap() 

    def withoutTextWrap(self):

        string = self.rowDelim

        for row in self.contents:
            maxWrap = (max([len(i) for i in row]) // self.wrap) + 1
            for r in range(maxWrap):
                string += self.colDelim
                for column in row:
                    start = r * self.wrap
                    end = (r + 1) * self.wrap 
                    string += column[start : end].ljust(self.wrap)
                    string += self.colDelim
                string += "\n"
            string += self.rowDelim

        return string

    def __str__(self):

        if self.wrapAtWordEnd:

            return self.withTextWrap() 

        else:

            return self.withoutTextWrap()

if __name__ == "__main__":

    l = [["heading 1", "heading 2", "asdf"],
         ["some text", "some more text", "Lorem ipsum dolor sit amet."],
         ["lots and lots and lots and lots and lots of text", "some more text", "foo"]]

    table = Table(l, 20, True)

    print(table)
