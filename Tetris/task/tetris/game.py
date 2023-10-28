# Write your code here
class TetrisFigure:
    max_positions = 5

    all_figures = {
        'O': [[5, 6, 9, 10]],
        'I': [[1, 5, 9, 13], [4, 5, 6, 7]],
        'S': [[6, 5, 9, 8], [5, 9, 10, 14]],
        'Z': [[4, 5, 9, 10], [2, 5, 6, 9]],
        'L': [[1, 5, 9, 10], [2, 4, 5, 6], [1, 2, 6, 10], [4, 5, 6, 8]],
        'J': [[2, 6, 9, 10], [4, 5, 6, 10], [1, 2, 5, 9], [0, 4, 5, 6]],
        'T': [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
    }

    def __init__(self, figure_id: str, pos: int = 0):
        self.figure = TetrisFigure.all_figures[figure_id]
        self.__pos = pos % len(self.figure)

    def set_position(self, pos: int):
        self.__pos = pos % len(self.figure)

    def get_position(self):
        return self.__pos

    position = property(get_position, set_position)

    def shape(self, pos=None):
        if pos is not None:
            self.position = pos
        figure = self.figure[self.__pos]
        return "".join([(lambda i: "0 " if i in figure else "- ")(pos) for pos in range(16)])

    def all_shapes(self):
        return [self.shape(pos) for pos in range(0, self.max_positions)]

    @classmethod
    def empty_shape(cls):
        return "- " * 16

    @staticmethod
    def print(s):
        print(s[0:8])
        print(s[8:16])
        print(s[16:24])
        print(s[24:32])
        print("")


def stage_1():
    fig_id = input()
    figure = TetrisFigure(fig_id)
    lst = [TetrisFigure.empty_shape()]
    lst.extend(figure.all_shapes())
    for el in lst:
        TetrisFigure.print(el)


class TetrisBoard:
    _default_shape = (10, 20)
    _all_pieces_default = {
        "O": [[4, 14, 15, 5]],
        "I": [[4, 14, 24, 34], [3, 4, 5, 6]],
        "S": [[5, 4, 14, 13], [4, 14, 15, 25]],
        "Z": [[4, 5, 15, 16], [5, 15, 14, 24]],
        "L": [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]],
        "J": [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]],
        "T": [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]],
    }

    class TetrisPiece:

        def __init__(self, piece, board_shape):
            self.orientation = 0
            self.shift = [0, 0]
            self.piece = piece
            self.board_shape = board_shape
            self._current_pos = self.piece[self.orientation]

        def _check_bound(self, pos, dw, dh, has_bound, width, height):
            h, w = divmod(pos, width)

            if (h + self.shift[1]) == (height - 1):
                return -1

            w += self.shift[0] + dw
            h += self.shift[1] + dh

            if has_bound:
                if w >= width or w < 0 or h >= height:
                    return -1
            else:
                w %= width
                h %= height
            return h * width + w

        def rotate(self, forward=True):
            self.orientation += (1 if forward else -1)
            self.orientation %= len(self.piece)

        def set_board_position(self, dw, dh, has_bound, width, height, field):
            piece = self.piece[self.orientation]
            new_pos = [0] * len(piece)
            for i, pos in enumerate(piece):
                n = self._check_bound(pos, dw, dh, has_bound, width, height)
                if n < 0:
                    return False
                new_pos[i] = n
            for i in new_pos:
                if field[i] == 1:
                    return False
            self.shift[0] += dw
            self.shift[1] += dh
            self._current_pos = new_pos
            return True

        def get_board_position(self):
            return self._current_pos

    def __init__(self, width=10, height=20, has_bound=False):
        self.Width = width
        self.Height = height
        self._all_pieces = self._transform(width)
        self.Size = width * height
        self.field = [0] * self.Size
        self._current_piece = None
        self.hasBound = has_bound
        self._is_vertical_fill = False

    def _check_vertical(self):
        for i in range(self.Width):
            is_fill = True
            for j in range(self.Height):
                if self.field[i + j*self.Width] == 0:
                    is_fill = False
                    break
            if is_fill:
                return True
        return False

    def _show(self, is_show=True):
        sign = 1 if is_show else 0
        current_pos = self._current_piece.get_board_position()
        for pos in current_pos:
            self.field[pos] = sign

    def _move(self, dw, dh):
        self._show(False)
        self._current_piece.set_board_position(dw, dh, self.hasBound, self.Width, self.Height, self.field)
        self._show(True)

    def clean(self):
        self.field = [0] * self.Size

    def draw(self):
        for h in range(self.Height):
            line = " ".join(["-" if self.field[w + h * self.Width] == 0 else "0" for w in range(self.Width)])
            print(line)
        print("")

    def remove(self):
        if self._current_piece is not None:
            self._show(False)
            self._current_piece = None

    def add(self, piece_id):
        if piece_id in self._all_pieces:
            self._current_piece = TetrisBoard.TetrisPiece(self._all_pieces[piece_id], (self.Width, self.Height))
            self._show()
        else:
            raise ValueError(f"Unknown type of a tetris piece: {piece_id}")

    def piece(self):
        piece_id = input()
        self.add(piece_id)
        return 1

    def left(self):
        self._move(-1, 0)
        self._move(0, 1)
        return 2

    def right(self):
        self._move(1, 0)
        self._move(0, 1)
        return 3

    def down(self):
        self._move(0, 1)
        return 4

    def rotate(self):
        self._show(False)
        self._current_piece.rotate()
        if self._current_piece.set_board_position(0, 0, self.hasBound, self.Width, self.Height, self.field):
            position = self._current_piece.get_board_position()

            self._show(True)
            self._move(0, 1)
        return 5

    def _shift_raw(self, raw):

        if raw > 0:
            while raw > 0:
                for j in range(self.Width):
                    self.field[j + raw*self.Width] = self.field[j+(raw - 1)*self.Width]
                raw -= 1

        for j in range(self.Width):
            self.field[j] = 0


    def break_raw(self):
        for i in range(self.Height):
            isfill = True
            for j in range(self.Width):
                if self.field[j+i*self.Width] == 0:
                    isfill = False
                    break
            if isfill:
                self._shift_raw(i)
        return 6

    @staticmethod
    def exit():
        return 0

    def command(self, cmd: str):
        self._is_vertical_fill = self._check_vertical()
        if cmd == "rotate":
            result = self.rotate()
        elif cmd == "left":
            result = self.left()
        elif cmd == "right":
            result = self.right()
        elif cmd == "down":
            result = self.down()
        elif cmd == "piece":
            result = self.piece()
        elif cmd == "break":
            result = self.break_raw()
        else:
            result = self.exit()

        if self._is_vertical_fill:
            result = -1
        return result

    def check_if_raw_filled(self):
        for h in range(self.Height):
            if all([w for w in range(h * self.Width, (h + 1) * self.Width)]):
                return h
        return -1

    def check_if_col_filled(self):
        for col in range(self.Width):
            if all([self.field[i] for i in range(col, col + self.Width * self.Height, self.Width)]):
                return col
        return -1

    @staticmethod
    def _transform(width):
        if width == TetrisBoard._default_shape[0]:
            return TetrisBoard._all_pieces_default
        else:
            result = {}
            for o_id, orientations in TetrisBoard._all_pieces_default.items():
                new_orientations = []
                for orientation in orientations:
                    new_orientation = []
                    for pos in orientation:
                        h, w = divmod(pos, TetrisBoard._default_shape[0])
                        new_pos = h * width + w
                        new_orientation.append(new_pos)
                    new_orientations.append(new_orientation)
                result[o_id] = new_orientations
            return result


def stage_2():
    piece_id = input()
    [w, h] = [int(dim) for dim in input().split()]
    board = TetrisBoard(w, h)
    is_run = True

    board.draw()
    board.add(piece_id)
    while is_run:
        board.draw()
        cmd = input()
        is_run = board.command(cmd)


def stage_3() -> object:
    piece_id = input()
    [w, h] = [int(dim) for dim in input().split()]
    board = TetrisBoard(w, h, True)
    is_run = True

    board.draw()
    board.add(piece_id)
    while is_run:
        board.draw()
        cmd = input()
        is_run = board.command(cmd)

def stage_4():
    [w, h] = [int(dim) for dim in input().split()]
    board = TetrisBoard(w, h, True)
    is_run = 1

    board.draw()
    while is_run > 0:
        cmd = input()
        is_run = board.command(cmd)
        if is_run != 0:
            board.draw()
        if is_run == -1:
            print("Game Over!!!")


if __name__ == "__main__":
    # stage_1()
    # stage_2()
    # stage_3()
    stage_4()
