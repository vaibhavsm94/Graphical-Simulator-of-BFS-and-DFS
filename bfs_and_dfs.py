from node import *
from pygame.locals import *
import pygame, sys
from menu import *
import time
from text import *

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
swidth, sheight = 1000, 600


def get_neighbors(screen, v, nodes, edges):
    source_of = v.source_of
    neighbors = []
    for edge in source_of:
        neighbors.append(edge.dest)
    return neighbors


def dfs(screen, all_nodes, all_edges):
    text(screen, "DFS Simulation", 20, 0, size=50, color=BLACK)
    DFS.a = 40
    for node in all_nodes:
        node.visited = False
        node.color = BLACK
        node.cir_width = 2
    start = all_nodes[0]
    DFS(screen, start, all_nodes, all_edges)


def DFS(screen, v, all_nodes, all_edges):
    for x in all_edges:
        x.color = BLACK
        x.width = 2
    b = sheight - 40
    v.color = BLUE
    v.cir_width = 4

    # For Stack simulation
    p = swidth - 100
    pygame.draw.rect(screen, BLACK, Rect((p, DFS.q), (60, 40)), 2)
    text(screen, str(v.node_no), DFS.a, b, color=BLACK)
    dfs.traversal.append(v.node_no)
    dfs.stack.append(v.node_no)
    draw_all_nodes(screen)
    draw_all_edges(screen)
    draw_stack_contents(screen)
    draw_dfs_traversal(screen)
    pygame.display.update()
    #DFS.a += 5000
    time.sleep(1)
    v.visited = True
    neighbors = get_neighbors(screen, v, all_nodes, all_edges)
    for x in neighbors:
        if x.visited == False:
            e = get_edge(v, x, all_nodes, all_edges)
            e.color = BLUE
            e.width = 4
            draw_all_nodes(screen)
            draw_all_edges(screen)
            draw_stack_contents(screen)
            draw_dfs_traversal(screen)
            pygame.display.update()
            time.sleep(1)
            DFS(screen, x, all_nodes, all_edges)
    dfs.stack.remove(v.node_no)
    draw_all_nodes(screen)
    draw_all_edges(screen)
    draw_stack_contents(screen)
    draw_dfs_traversal(screen)


DFS.a = 40
DFS.q = sheight - 80
dfs.traversal = []
dfs.stack = []


def draw_stack_contents(screen):
    p = 40
    q = sheight - 100
    screen.fill(WHITE)
    for x in dfs.stack:
        draw_all_nodes(screen)
        draw_all_edges(screen)
        draw_dfs_traversal(screen)
        pygame.draw.rect(screen, BLACK, Rect((p, q), (40, 40)), 2)
        text(screen, str(x), p + 10, q + 10, color=BLACK)
        draw_bfs_traversal(screen)
        p += 40
        pygame.display.update()
    time.sleep(1)


def draw_dfs_traversal(screen):
    a = 40
    b = sheight - 40
    for x in dfs.traversal:
        text(screen, str(x), a, b, color=BLACK)
        a += 40


def bfs(screen, all_nodes, all_edges):
    for x in all_edges:
        x.color = BLACK
        x.width = 2
    mat = construct_matrix(all_nodes, all_edges)
    text(screen, "BFS Simulation", 20, 20, size=50, color=BLACK)
    for node in all_nodes:
        node.visited = False
        node.color = BLACK
        node.cir_width = 2
    start = all_nodes[0]
    start.visited = True
    que = [start]
    draw_q_contents(screen, que)
    while len(que):
        v = que[0]
        v.color = BLUE
        v.cir_width = 4
        time.sleep(1)
        draw_bfs_traversal(screen)
        draw_all_nodes(screen)
        draw_all_edges(screen)
        bfs.traversal.append(v.node_no)
        pygame.display.update()
        time.sleep(1)
        neighbors = get_neighbors(screen, v, all_nodes, all_edges)
        for x in neighbors:
            if x.visited == False:
                e = get_edge(v, x, all_nodes, all_edges)
                if e is not None:
                    e.color = BLUE
                    e.width = 4
                    draw_all_nodes(screen)
                    draw_all_edges(screen)
                    draw_q_contents(screen, que)
                    pygame.display.update()
                    x.visited = True
                    que.append(x)
        draw_q_contents(screen, que)
        que.remove(v)
        draw_q_contents(screen, que)


bfs.traversal = []


def draw_bfs_traversal(screen):
    a = 40
    b = sheight - 40
    for x in bfs.traversal:
        text(screen, str(x), a, b, color=BLACK)
        a += 40


def get_edge(src, dest, all_nodes, all_edges):
    srcs = src.source_of
    print(srcs)
    dests = dest.dest_of
    print(dests)
    for x in all_edges:
        if x in srcs and x in dests:
            return x
    return None


def draw_q_contents(screen, que):
    p = 40
    q = sheight - 100
    screen.fill(WHITE)
    for x in que:
        draw_all_nodes(screen)
        draw_all_edges(screen)
        pygame.draw.rect(screen, BLACK, Rect((p, q), (40, 40)), 2)
        text(screen, str(x.node_no), p + 10, q + 10, color=BLACK)
        draw_bfs_traversal(screen)
        p += 40
        pygame.display.update()
    time.sleep(2)
