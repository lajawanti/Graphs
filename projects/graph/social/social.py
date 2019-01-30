from itertools import combinations
import random 

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # Add users
        for i in range(numUsers):
            self.addUser(f'User_{i}')
        
        # Create friendships
        possible_friendships = list(combinations(range(1, int(len(self.users) + 1)),2))
        #print(possible_friendships,"\nlength of possible combinations  : ", len(possible_friendships))
        random.shuffle(possible_friendships)
        index = (numUsers * avgFriendships) //2
        #print("index  : ", type(index))
        actual_friendships = possible_friendships[ : index]
        #print("\n\nactual friendships  : ", actual_friendships)
        
        for friendship in actual_friendships:
            self.addFriendship(friendship[0], friendship[1])
        

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        if userID in self.users:
            print("VALID USER.....")
            if self.friendships[userID]:
                print("Have Friends.........")
                print(self.friendships[userID])



            return visited
        else:
            return 'Invalid User...'

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
