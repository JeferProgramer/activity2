import networkx as nx

class RuleBasedRouteSystem:
    def __init__(self):
        self.graph = nx.Graph()
        self.knowledge_base = {
            'rules': {
                'max_transfers': 2,  
                'max_time': 120     
            },
            'stations': {},          
            'connections': {} 
        }
    
    def add_station(self, name, coordinates):
        self.knowledge_base['stations'][name] = coordinates
        self.graph.add_node(name, pos=coordinates)
    
    def add_connection(self, origin, destination, distance, time):
        if time <= self.knowledge_base['rules']['max_time']:
            self.knowledge_base['connections'][(origin, destination)] = {
                'distance': distance, 'time': time
            }
            self.graph.add_edge(origin, destination, distance=distance, time=time)
    
    def find_route(self, start, end):
        route = nx.shortest_path(self.graph, start, end, weight='time')
            
        return route if len(route) - 1 <= self.knowledge_base['rules']['max_transfers'] else []
    
    def analyze_route(self, route):
        return {
            'route': route,
            'total_distance': sum(
                self.knowledge_base['connections'][(route[i], route[i+1])]['distance'] 
                for i in range(len(route)-1)
            ),
            'total_time': sum(
                self.knowledge_base['connections'][(route[i], route[i+1])]['time'] 
                for i in range(len(route)-1)
            )
        }

print("\nPrueba 3: Ruta directa sin transferencias")
system = RuleBasedRouteSystem()
system.add_station('P', (0, 0))
system.add_station('Q', (50, 50))
system.add_connection('P', 'Q', 70, 100)

route = system.find_route('P', 'Q')
details = system.analyze_route(route)
print("Ruta encontrada:", details)