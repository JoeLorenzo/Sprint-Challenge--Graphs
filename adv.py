from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue  

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

