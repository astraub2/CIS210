"""
sdtactics.py:
Tactics and checks for Sudoku.

Authors: Amber Straub

A tactic is a rule that can be used to determine and/or constrain the
possible choices for a Sudoku tile. We use both the naked single and
hidden single tactic.

A check determines whether a given Sudoku board
(whether complete or incomplete) is legal.  A board is
legal if it contains only digits and open spaces, and
if all of the digits are unique in each row, column,
and 3x3 block.

CIS 210 assignment 7, Fall 2015
"""
import sdkboard

# The following variables are private but global to the module
global groups
global progress

def prepare(board):
    """ 
    Prepare for checking and solving a sudoku board.
    Args:
       board:  An sdkboard.Board object
    Returns:
       nothing
    Effects:
       prepared for check(board) and solve(board)
    """
    global groups  # rows, columns, and blocks
    groups = [ ]
    
    # Rows
    for row in range(9):
        groups.append(board.tiles[row])
    # Columns
    # I used the already constructed Rows to build
    # my columns
    column_builder=[[],[],[],[],[],[],[],[],[]]
    x=0
    while x<9:#each loop adds an item to each column
        current=groups[x]#using the Rows
        i=0
        for item in current:
            column_builder[i]=column_builder[i]+[item]
            i=i+1
        x=x+1
    groups=groups+column_builder

    # Blocks
    for start_row in [0, 3, 6]:
        for start_col in [0, 3, 6]:
            sq_tiles = [ ] 
            for row in range(3):
                for col in range(3): 
                    t = board.tiles[start_row + row][start_col+col]
                    sq_tiles.append(t)
            groups.append(sq_tiles)

    # We need to know when we are making progress 
    for row in board.tiles:
        for tile in row:
            tile.register(progress_listener)
    
 
def progress_listener(tile, event):
    """
    An event listener, used to determine whether we have made
    some progress in solving a Sudoku puzzle.  This listener
    will be attached to Sudoku Tile objects, and informed when
    "determined" and "constrained" events occur.
    Args:
       tile:  The tile on which an event occurred
       event: What happened.  The events we listen for are "determined"
         and "constrained"
    Returns:  nothing
    Effects: module-global variable progress may be set to True
    """
    global progress 
    if event == "determined" or event == "constrained":
       progress = True

def good_board(): 
        """Check that every group (row, column, and block)
        contains unique elements (no duplicate digits).
        Args:
           none  (implicit through prepare_board)
        Returns:
           Boolean True if all groups contain unique elements
        Effects:
           Will announce "duplicate" event on tiles that are
           not unique in a group.
        Requires:
           prepare(board) must be called before good_board
        """
        global groups
        list=[]#stores known values, to check for repeates
        ex=[]#stores tiles of these values, so we can flag them
        x=0
        y=0
        compare=""
        for group in groups:
            for tile in group:
                if (len(tile.possible)==1):
                    list.append(tile.symbol)
                    ex=ex+[tile]
            if((len(set(list)))==len(list)):#checks for repeates
                x=x+1
            else:#if there is a repeat, this tells us where and what
                for tile in ex:
                    compare=compare+tile.symbol
                for tile in ex:
                    for elm in compare:
                        if(tile.symbol==elm):
                            y=y+1
                    if (y>1):
                        tile.announce("duplicate")
                    y=0
            
            list=[]
            ex=[]
            compare=""
        if(x==27):
            return True

def solve():
    """
    Keep applying naked_single and hidden_single tactics to every
    group (row, column, and block) as long as there is progress.
    Args: 
        none
    Requires:
        prepare(board) must be called once before solve()
        use only if good_board() returns True
    Effects: 
        May modify tiles in the board passed to prepare(board), 
        setting symbols in open tiles, and reducing the possible
        sets in some tiles. 
    """
    global groups
    global progress
    progress = True
    while(progress):
        progress = False 
        for group in groups:
            naked_single(group)
            hidden_single(group)

def naked_single(group):
        """Constrain each tile to not contain any of the digits 
        that have already been used in the group.
        Args: 
            group: a list of 9 tiles in a row, column, or block
        Returns:
            nothing
        Effects:
            For each tile in the group, eliminates "possible" elements
            that match a digit used by another tile in the group.  If 
            this reduces it to one possibility, the selection will be 
            made (Tile.remove_choices does this), and progress may be 
            signaled.
        """
        choices=set()
        for tile in group:
            if (len(tile.possible)==1):
                x=(tile.possible)
                choices=choices.union(x)
        for tile in group:
            if (len(tile.possible)>1):
                tile.remove_choices(choices)
        return
        
        
def hidden_single(group):
        """Each digit has to go somewhere.  For each digit, 
        see if there is only one place that digit should 
        go.  If there is, put it there. 
        Args: 
           group:  a list of 9 tiles in a row, column, or block
        Returns: 
           nothing
        Effects: 
           For each tile, if it is the only tile that can accept a 
           particular digit (according to its "possible" set), 
           
        """
        choices=set(["1","2","3","4","5","6","7","8","9"])
        stored=[]
        taker=0
        for tile in group:
            if (len(tile.possible)==1):
                choices=choices-set(tile.possible)
        for choice in choices:
            for tile in group:
                if (len(tile.possible)>1):
                    for x in tile.possible:
                        if(choice==x):
                            stored=stored+[tile]
                            taker=x
            if (len(stored)==1):              
                stored[0].determine(taker)
            stored=[]
            taker=0
        return

        
