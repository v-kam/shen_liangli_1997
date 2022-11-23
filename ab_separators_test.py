#!/usr/bin/env python3.8
# coding: utf-8

import networkx as nx

from ab_separators import min_ab_separators

def test_min_ab_separators_paper_example() -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from(range(1,8))

    G.add_edges_from([(1,3), (1,4), (3,4)])
    G.add_edges_from([(1,5), (3,7), (4,6)])
    G.add_edges_from([(2,6),(2,7),(5,6), (5,7)])

    sep = min_ab_separators(G, 1, 2)

    # set of sets to make the comparison easy, ignoring order of separators
    assert {frozenset(s) for s in sep} == \
    { frozenset({5, 3, 6}), \
      frozenset({4, 5, 7}), \
      frozenset({6, 7}), \
      frozenset({5, 4, 3}) }

def test_min_ab_separators_tcsstack_example() -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from(range(1,8))

    G.add_edges_from([(1,2), (1,3)])
    G.add_edges_from([(2,3)])
    G.add_edges_from([(2,4), (2,5), (2,6)])
    G.add_edges_from([(3,4), (3,5), (3,6)])
    G.add_edges_from([(4,7), (5,7), (6,7)])

    sep = min_ab_separators(G, 1, 7)

    # set of sets to make the comparison easy, ignoring order of separators
    assert {frozenset(s) for s in sep} == \
    { frozenset({2, 3}), \
      frozenset({4, 5, 6}) }

def test_min_ab_separators_grid() -> nx.Graph:
    G = nx.grid_graph(dim=(2,3))
    sep = min_ab_separators(G, (0,0), (2,1))

    # set of sets to make the comparison easy, ignoring order of separators
    assert {frozenset(s) for s in sep} == \
    { frozenset({ (0,1),(1,0) }), \
      frozenset({ (1,0),(1,1) }), \
      frozenset({ (1,1),(2,0) }) }

def test_min_ab_separators_P5() -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from(range(1,6))
    G.add_edges_from([(1,2), (2,3), (3,4), (4,5)])

    sep_1_2 = min_ab_separators(G, 1, 2)
    sep_1_3 = min_ab_separators(G, 1, 3)
    sep_1_4 = min_ab_separators(G, 1, 4)
    sep_1_5 = min_ab_separators(G, 1, 5)
    sep_2_3 = min_ab_separators(G, 2, 3)
    sep_2_4 = min_ab_separators(G, 2, 4)
    sep_2_5 = min_ab_separators(G, 2, 5)
    sep_3_4 = min_ab_separators(G, 3, 4)
    sep_3_5 = min_ab_separators(G, 3, 5)
    sep_4_5 = min_ab_separators(G, 4, 5)

    # set of sets to make the comparison easy, ignoring order of separators
    assert {frozenset(s) for s in sep_1_2} == set()
    assert {frozenset(s) for s in sep_1_3} == { frozenset({2}) }
    assert {frozenset(s) for s in sep_1_4} == { frozenset({2}), frozenset({3}) }
    assert {frozenset(s) for s in sep_1_5} == \
      { frozenset({2}), frozenset({3}), frozenset({4}) }
    assert {frozenset(s) for s in sep_2_3} == set()
    assert {frozenset(s) for s in sep_2_4} == { frozenset({3}) }
    assert {frozenset(s) for s in sep_2_5} == { frozenset({3}), frozenset({4}) }
    assert {frozenset(s) for s in sep_3_4} == set()
    assert {frozenset(s) for s in sep_3_5} == { frozenset({4}) }
    assert {frozenset(s) for s in sep_4_5} == set()

def main():
    test_min_ab_separators_paper_example()
    test_min_ab_separators_tcsstack_example()
    test_min_ab_separators_grid()
    test_min_ab_separators_P5()
    print("min_ab_separators(): success on all tests")

    #nx.draw(G, with_labels=True)
    #plt.show()
    #plt.savefig("graph.png")

if __name__ == "__main__":
    main()
