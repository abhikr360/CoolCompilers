import me;
import mu;


class BookList inherits IO {

    def isNil : Bool () { { isNil(); TRUE; } };
    
    def cons : Cons(hd : Book) {
        (let new_cell : Cons <- new Cons in
            new_cell.init(hd,self)
        tel)
    };

    def car : Book() { { abort(); new Book; } };

    def cdr : BookList() { { abort(); new BookList; } };
    
    def print_list : Object() { abort() };
};
