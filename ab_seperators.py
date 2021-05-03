import networkx as nx
import graphs
from itertools import product


def min_ab_separators(G, a, b):
    """
    Implementation of:
    Efficient enumeration of all minimal separators in a graph
    H. Shen, W. Liangi in Theoretical Computer Science 180 (1997) 169-180

    :param G: Subject graph
    :param a: start node
    :param b: end node
    :return: all minimal ab-seperators
    """
    n = len(G)
    if type(a) is not set:
        a = {a}
    if type(b) is not set:
        b = {b}

    def N(X):
        """Return set of neighbours of node-set X"""
        if type(X) is not set:
            X = {X}
        neighbors = set()
        for v in X:
            neighbors.update(nx.all_neighbors(G, v))
        return neighbors - X

    def I(X, Cb):
        if type(X) is not set:
            X = {X}
        isolated = set()
        for v in X:
            if v not in N(Cb):
                isolated.add(v)
        return isolated

    def calculate_Cb(S):
        H = G.copy()
        H.remove_nodes_from(S)

        for C in nx.connected_components(H):
            if len(b - C) == 0:
                return C
        return set()

    Cb = calculate_Cb(N(a))
    k = 0
    L = {k: [(a, N(a) - I(N(a), Cb))]}
    for i in range(1, n - 2):
        L[i] = []
    seperators = [N(a) - I(N(a), Cb)]

    while k <= n - 3 and len(Cb) != 0:
        for p, S in L[k]:
            for x in S:
                if len(b.intersection(N(x))) == 0:
                    N_plus = N(x) - a - S
                    SuN_plus = S.union(N_plus)
                    Cb = calculate_Cb(SuN_plus)

                    if len(Cb) != 0:
                        S_new = SuN_plus - I(SuN_plus, Cb)
                        if S_new not in seperators:
                            L[k + 1].append((x, S_new))
                            seperators.append(S_new)
        k += 1
        if not L[k]:
            break

    return seperators
