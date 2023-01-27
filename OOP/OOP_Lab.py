import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        self.connections[connection_id] = connection_load
        

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        for value in self.connections.values():
            total += value
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())


class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        server.add_connection(connection_id)
        self.connections[connection_id] = server
        self.ensure_availability()

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        for server in self.servers:
            if connection_id in server.connections:
                server.connections[connection_id] = 0
        self.avg_load()
        

    def avg_load(self):
        """Calculates the average load of all servers"""
        total = 0
        for server in self.servers:
            for value in server.connections.values():
                total += value
        return total/len(self.servers)

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        avg = self.avg_load()
        if avg > 50:
            self.servers.append(Server())


    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))


server = Server()
server.add_connection("192.168.1.1")

print(server.load())

server.close_connection("192.168.1.1")
print(server.load())


l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())


l.servers.append(Server())
print(l.avg_load())


l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

for connection in range(20):
    l.add_connection(connection)
print(l)

print(l.avg_load())
                    
