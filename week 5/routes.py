"""
Graph search to find shortest path between two cities. 
Authors: Amber Straub, Eric Ditrich(not enrolled)

A road map is represented as a directed graph.
Edges represent road segments and are labeled with distances.
Nodes represent cities. 
We use depth first search to find the shortest distance
between two cities. During the depth-first search from
start to end, we compute a 'shortest known distance to here from start'
attribute for each node.  After completion of depth first search,
destination city should be labeled with the shortest distance from
the start city.  
"""

import argparse

def read_distances(map_file):
    """Read a distance table from a named file into a dict
       mapping sources to lists of (destination, distance) pairs. 
    Args:
       map_file: A readable text file in which each line either 
           begins with #  (indicating a comment line) or is of the form
           from location, to location, distance or time, for example
              Minis Tirith,Cair Andros,5
           indicating one can travel from Minis Tirith to Cair Andros in 5.0 hours.
    Returns:
        Dict in which each entry d[from] is a list [(to, cost), (to, cost), ... ]
        where from is a location name, to is a location name, and cost is time
        or distance
        as a floating point number.  If x,y,z appears in the input file, then 
        we should have both d[x] contains (y,z) and d[y] contains (x,z), i.e., 
        we assume that roads are bi-directional. 
    """
    connections = dict() 
    for line in map_file:
        line = line.strip()  
        if line.startswith("#") or line=="" :
            # print("Skipping comment: ", line)
            continue  ## Discard and go on to next
        # print("Processing line: ", line)
        fields = line.split(",")
        place_from = fields[0]
        place_to = fields[1]
        cost = float(fields[2])
        if not (place_from in connections): 
            connections[place_from] = [ ]
        connections[place_from].append( (place_to, cost) )
        if not (place_to in connections): 
            connections[place_to] = [ ]
        connections[place_to].append( (place_from, cost) )
    return connections


return_choices=0


def translator(roads, start_in, target, choices, choice_pos):
    """ this function investigates each path as it is given
    information from dfs function.
    args: start_in
    target
    choices(information on how to increment)
    returns: dist_so_far if target is reached
    """
    while(choice_pos<len(choices)+1):
        start=start_in
        dis_so_far=0
        if (start==target):
            return (True, dis_so_far)
        else:
            if (choice_pos<len(choices)):
                start=roads[start[choices[choice_pos]]][0]
                pos,dis=roads[start[choices[choice_pos]]][0]
                dis_so_far=dis_so_far+int(dis)
                choice_pos=choice_pos+1
            else:
                return (False, None)



def increment(roads,choices, level):
    """ this function increments each path option to be run through by
    translator, as it is given information from dfs function.
    args: roads
    choices(information on how to increment)
    level
    returns: none. increments level to be used by translator
    """
    if(level <= len(choices)):
        if(choices[len(roads)-level]+1 > len(roads[choices[level]])):
            choices[level]=0
            increment(roads,choices,level+1)
        else:                               
            choices[level]=choices[leval+1]
            global return_choices
            return_choices=choices
            
    else:
        global return_choices
        return_choices==choices



def dfs(roads,start,target,choices,shortest,found):
    """ this function recusively finds the shortest path between 2 points in a map.
    args:
    roads
    start
    target
    choices
    shortest
    found
    returns:
    found: shortest path from star to finish
    """
    data, dis=translator(roads,start, target, choices, 0)[0]#finds initial route(simplest path)
    if(data):
        found=True
        if(dis<shortest):
            shortest=dis

    newdata=increment(roads,choices,0)

    if(newdata[1]):
        end(found,shortest,start,target)
    else:
        choices=newdata[0]

           

    dfs(roads,start,target,choices,shortest,counter+1,new_msb,found)########## recurtion
        


def end(found,distance,start,target):#data to return to user
    if(found):
        print("Distance from ",start," to ",target," is ",distance)
    else:
        print("You can't get from ",start, " to ",target,".")




def main():

    parser = argparse.ArgumentParser(
        description="Find shortest route in road network")
    parser.add_argument('from_place', 
                help = "Starting place (quoted if it contains blanks)")
    parser.add_argument('to_place', 
                help = "Destination place (quoted if it contains blanks)")
    parser.add_argument('map_file', type=argparse.FileType('r'),
                help = "Name of file containing road connections and distances")
    args = parser.parse_args()
    start_place  = args.from_place
    destination = args.to_place
    roads = read_distances(args.map_file)#### connections
    global return_choices
    return_choices=[0]*len(roads) 


    if not start_place in roads: 
        print("Start place ", start_place, " is not on the map")
        exit(1)
    if not destination in roads: 
        print("Destination ", destination, " is not on the map")
        exit(1)
    
    dfs(roads,start_place,destination,return_choices,None,False)

if __name__ == "__main__":
    main()
