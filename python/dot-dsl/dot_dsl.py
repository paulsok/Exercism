NODE, EDGE, ATTR = range(3)


class Component(object):
    _schema = NotImplemented

    @classmethod
    def validate(cls, args):
        return all(isinstance(a, t) for a, t in zip(args, cls._schema))


class Node(Component):
    _schema = (str, (dict, set))

    def __init__(self, name, attrs={}):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(Component):
    _schema = (str, str, dict)

    def __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Attr(Component):
    _schema = (str, str)

    def __init__(self, key, value):
        self.kv = (key, value)


class Graph(object):
    def __init__(self, data=[]):
        if not self._validate(data):
            raise TypeError('Invalid DSL')

        self._nodes, self._edges, self._attrs = [], [], []

        self._graph = {
            NODE: (Node, self._nodes),
            EDGE: (Edge, self._edges),
            ATTR: (Attr, self._attrs),
        }

        for directive in data:
            componenet, args = directive[0], directive[1:]

            try:
                cls, storage = self._graph[componenet]
            except KeyError:
                raise ValueError('Unknown graph component `{}`'.format(componenet))

            if not cls.validate(args):
                raise ValueError('Invalid {}'.format(cls.__name__))

            storage.append(cls(*args))

    def _validate(self, data):
        return all(isinstance(x, tuple) and len(x) > 0 for x in data)

    @property
    def nodes(self):
        return self._nodes

    @property
    def edges(self):
        return self._edges

    @property
    def attrs(self):
        return dict(a.kv for a in self._attrs)
