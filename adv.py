from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue  
#####
#                                                                                                                                                           #
#                                                        434       497--366--361  334--384--435  476                                                        #
#                                                         |                   |    |              |                                                         #
#                                                         |                   |    |              |                                                         #
#                                              477--443  425            386--354--321  338  313  380--445--446                                              #
#                                                    |    |              |         |    |    |    |    |                                                    #
#                                                    |    |              |         |    |    |    |    |                                                    #
#                                                   408  350  483  385  388  285  304  278  287--353  480                                                   #
#                                                    |    |    |    |    |    |    |    |    |                                                              #
#                                                    |    |    |    |    |    |    |    |    |                                                              #
#                                    442  461  426  392--281  223--169  257  253  240  196--224  255  373                                                   #
#                                     |    |    |         |         |    |    |    |    |         |    |                                                    #
#                                     |    |    |         |         |    |    |    |    |         |    |                                                    #
#                                    417  422--394--318--199--197--165--163--228  233--152  192--239--336--421                                              #
#                                     |              |                   |              |    |                                                              #
#                                     |              |                   |              |    |                                                              #
#                          491  453--351  444  374--340  328--200--204  148--178  143  147--154--184  282  363  389                                         #
#                           |         |    |                   |         |         |    |              |    |    |                                          #
#                           |         |    |                   |         |         |    |              |    |    |                                          #
#                          489  441  332  387  341--316  195  175--141  121--123--138--139--176  136--231--294--311--499                                    #
#                           |    |    |    |         |    |         |    |                        |                                                         #
#                           |    |    |    |         |    |         |    |                        |                                                         #
#                     396--391  319  295  331  307  292--185--155  107  111--114--120  172  146  109  186--262--390--398                                    #
#                           |    |    |    |    |              |    |    |              |    |    |    |              |                                     #
#                           |    |    |    |    |              |    |    |              |    |    |    |              |                                     #
#           452--428--411--324--289--250  277  208--166  140  082  102--064  101  093  132  086--095  098  245--343  487                                    #
#                 |                   |    |         |    |    |         |    |    |    |    |         |    |                                               #
#                 |                   |    |         |    |    |         |    |    |    |    |         |    |                                               #
#           451--429  397  357--342--221--174  210  161  063--061  033  060  091  051  073  084  078--090--142  381--431                                    #
#                      |                   |    |    |         |    |    |    |    |    |    |    |              |                                          #
#                      |                   |    |    |         |    |    |    |    |    |    |    |              |                                          #
#      492--400--399--358  352  297--207  124--112--106--079--046--017--028  037--042  056--067  075--088--125--238--293                                    #
#                      |    |         |                             |    |    |         |         |    |    |                                               #
#                      |    |         |                             |    |    |         |         |    |    |                                               #
#           414--365--333--303  171--168--137  085  074  032  047--014  030  031  027--055  048--053  103  198--270--300--320                               #
#                 |         |              |    |    |    |         |         |    |         |                             |                                #
#                 |         |              |    |    |    |         |         |    |         |                             |                                #
#                447  301--187--167--108--081--045--040--019--015--013--009  020--026  035--044--059--189--275--283--376  471                               #
#                                          |                             |    |         |                             |                                     #
#                                          |                             |    |         |                             |                                     #
#                436  470  227--194--128--092  069--041--036--021  004  007--012--018--034--039--071--150--251  325  468                                    #
#                 |    |              |    |    |    |         |    |    |         |         |    |              |                                          #
#                 |    |              |    |    |    |         |    |    |         |         |    |              |                                          #
#           465--368--284--254--205--162  100  072  076  011--003--000--001--022  024--025  052  115--160--214--246--412                                    #
#                      |                        |         |         |    |         |    |                                                                   #
#                      |                        |         |         |    |         |    |                                                                   #
#           479--418--349  274--222--190--129  089  083--080  016--008  002--010  029  043--049--119--131--329--407                                         #
#                 |                        |    |    |                   |    |    |    |         |                                                         #
#                 |                        |    |    |                   |    |    |    |         |                                                         #
#                463--458  379  226--225--105--104  099  058--023--006--005  038  054  077--130  219--305--330--454                                         #
#                      |    |    |              |    |         |    |    |                        |         |                                               #
#                      |    |    |              |    |         |    |    |                        |         |                                               #
#           486--462  359  266--260  235--158--126  122  068--057  062  050--070--087  182--211  242  326  348                                              #
#                 |    |                   |    |              |    |    |    |    |    |    |    |    |                                                    #
#                 |    |                   |    |              |    |    |    |    |    |    |    |    |                                                    #
#                367--344--230  243  180--164  135  145--113--094  065  066  116  117--170  248  286--288--498                                              #
#                           |    |              |    |         |    |    |    |    |         |    |                                                         #
#                           |    |              |    |         |    |    |    |    |         |    |                                                         #
#                339--314--220--215--177--156--149  183  153--097  134  096  159  127--173  272  309--377--456                                              #
#                 |                        |    |              |    |    |         |    |         |                                                         #
#                 |                        |    |              |    |    |         |    |         |                                                         #
#           482--404  258--236--216--213--209  191  188  157--110  144  179--201  212  202--249  371--430--440                                              #
#            |              |         |         |    |         |    |    |    |    |    |                                                                   #
#            |              |         |         |    |         |    |    |    |    |    |                                                                   #
#           484  433--372--263  271--217  241--193  151--133--118--218  181  206  229  267--302--402--403--439                                              #
#                           |    |         |    |         |         |         |    |                                                                        #
#                           |    |         |    |         |         |         |    |                                                                        #
#      494--457--355--312--299  310  327--256  203  247--234--259  252  244--232  237--370  364--401--427--474                                              #
#                      |    |         |    |    |    |    |    |    |    |    |              |    |    |                                                    #
#                      |    |         |    |    |    |    |    |    |    |    |              |    |    |                                                    #
#                437--347  356  469--362  279  269  369  280  291  261  264  265--273--298--360  420  438                                                   #
#                      |    |         |    |    |              |    |    |    |    |              |    |                                                    #
#                      |    |         |    |    |              |    |    |    |    |              |    |                                                    #
#                393--375  405  423--395  323  315--335--378  306  345  290  268  296--308--337  464  448--490                                              #
#                      |    |                   |    |    |    |    |         |    |    |    |         |                                                    #
#                      |    |                   |    |    |    |    |         |    |    |    |         |                                                    #
#           493--478--413  432--473       410--406  346  466  415  409  322--276  382  317  383       475                                                   #
#                      |    |                             |         |    |    |    |    |    |         |                                                    #
#                      |    |                             |         |    |    |    |    |    |         |                                                    #
#                     419  449--450                      472--495  488  424  459  455  416  460       496                                                   #
#                                                         |                   |                                                                             #
#                                                         |                   |                                                                             #
#                                                   485--481                 467                                                                            #
#                                                                                                                                                           #

#####
# ['w', 'w', 's', 's', 'e', 'e', 'n', 'n', 'n', 'w', 'w', 'n', 's', 'e', 'e', 'e', 'e', 'n', 's', 'w', 'w', 's', 'e', 'e', 'w', 'w']
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

rooms = {}
for k, v in room_graph.items():
    rooms[k] = v[1]

# print(rooms)

player = Player(world.starting_room)

# 1. transalte problem into graph terminology

# -- the rooms are the vertices (nodes)

# -- the cardinal directions are the edges

# -- the graph is undirected because the player can travel to an avaible 
#    room and travel back.

# -- the graph is cyclic 


# 2. Build your graph
# 3. Traverse the graph


# Fill this out with directions to walk

# You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.
inverse_room = {
    "n":"s", "s":"n", "e":"w", "w":"e"
}

cardinal_dir = ["s", "w", "e", "n"]

# helper function to get adjacent room
def get_neighbor_id(room_id, direction):
    if direction not in rooms[room_id]:
        return None
    else:
        return rooms[room_id][direction]

# helper function that will return a boolean value if there is a dead end
# if the room number has any "?" values then the function will return false
def dead_end(room_id):
    count = 0
    for direction in cardinal_dir:
        if visited[room_id][direction] != "?":
            count +=1
    if count == 4:
        return True
    else:
        return False

# helper function to gets all "?" rooms in the visited dictionary given a room number
# output is an array of cardinal directions. ie ["s", "n"]
def get_unvisited_directions(room_id):
    unvisited_rooms = []
    if dead_end(room_id) == False:
        for direction in cardinal_dir:
            if visited[room_id][direction] == "?":
                unvisited_rooms.append(direction)
    return unvisited_rooms 

# helper function that returns exits given a room number
# output is an array of cardinal directions ie ["s", "e"]
def get_exits(room_id):
    exits = []
    for direction in cardinal_dir:
        if direction in rooms[room_id]:
            exits.append(direction)
    return exits



visited = {}

def dfs(starting_room):
    
    curr_room = player.current_room.id
    visited[curr_room] = {"n": "?", "e": "?", "s": "?", "w": "?"}
    # create the stack
    s = Stack()
    path = []
    reverse_path = []

    for direction in get_exits(curr_room):
        s.push(direction)
    
    while s.size() > 0:
        walk_dir = s.pop()
        print(f"CURRENT ROOM: {curr_room}")
        print(f"popping from stack {walk_dir}")
        
        # check if visited

        # if not in visited
        if visited[curr_room][walk_dir] == "?":

            # add to visited
            neighbor_id = get_neighbor_id(curr_room, walk_dir)
            visited[curr_room][walk_dir] = neighbor_id
            if neighbor_id not in visited:
                visited[neighbor_id] = {"n": "?", "e": "?", "s": "?", "w": "?"}
                visited[neighbor_id][inverse_room[walk_dir]] = curr_room
            curr_room = neighbor_id
            print(f"walking {walk_dir} to room {curr_room} ")

            # append step to path
            path.append(walk_dir)
            print(f"path {path}")
            # append a reverse step to reverse path
            reverse_path.append(inverse_room[walk_dir])
            print(f"reverse path {reverse_path}")
                
            # get adjacent neighbors not in visited and add to stack
            for direction in get_unvisited_directions(curr_room):
                if get_neighbor_id(curr_room, direction) == None:
                    visited[curr_room][direction] = None
                else:
                    s.push(direction)
                    print(f"stack {s.stack}")
            
            # if no adjacent unvisited neigbors then walkback one step
            if dead_end(curr_room) == True:
                if len(reverse_path) > 0: 
                    walkback_step = reverse_path.pop()
                    path.append(walkback_step)
                    s.push(walkback_step)
                    print(f"need to walk back {walkback_step} to room {get_neighbor_id(curr_room, walkback_step)}") 
                    curr_room = get_neighbor_id(curr_room, walkback_step)

        # if the current room is in a visited dead end then walk back one step
        elif dead_end(curr_room) == True:
            if len(reverse_path) > 0: 
                walkback_step = reverse_path.pop()
                path.append(walkback_step)
                s.push(walkback_step)
                print(f"need to walk back {walkback_step} to room {get_neighbor_id(curr_room, walkback_step)}") 
                curr_room = get_neighbor_id(curr_room, walkback_step)

    print(visited)
    print(f"path {path}")

    return path

    
traversal_path = dfs(player.current_room)


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

