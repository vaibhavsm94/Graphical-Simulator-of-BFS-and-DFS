import pygame, sys
from random import randint
from pygame.locals import *
from text import text
import math

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

everything = []


class Edge:
    all_edges = []
    directed = True

    def __init__(self, nodes):
        self.source = nodes[0]
        self.dest = nodes[1]
        self.width = 2
        x1 = self.source.x
        y1 = self.source.y
        x2 = self.dest.x
        y2 = self.dest.y
        distance = dist(x1, x2, y1, y2)
        n = float(Node.radius) / distance
        m = 1 - n
        self.start_x = get_co_ordinate(x1, x2, m, n)
        self.start_y = get_co_ordinate(y1, y2, m, n)
        self.end_x = get_co_ordinate(x1, x2, n, m)
        self.end_y = get_co_ordinate(y1, y2, n, m)

        self.color = BLACK
        Edge.all_edges.append(self)
        everything.append(self)

        if not Edge.directed:
            nodes[0].source_of.append(self)
            nodes[1].source_of.append(self)
            nodes[0].dest_of.append(self)
            nodes[1].dest_of.append(self)
        else:
            nodes[0].source_of.append(self)
            nodes[1].dest_of.append(self)

    def draw_arrow(self, x1, y1, x2, y2, screen, color):
        # Calculate the angle of the line with x=0 line
        deg = math.degrees(math.atan2(y1 - y2, x2 - x1))
        # convert angle to radians
        deg = math.pi * deg / 180
        r = 5
        x4 = x2 - (r * math.cos(deg))
        y4 = y2 + (r * math.sin(deg))
        x3 = x4 + (r * math.sin(deg))
        y3 = y4 + (r * math.cos(deg))
        x5 = x4 - (r * math.sin(deg))
        y5 = y4 - (r * math.cos(deg))
        pygame.draw.polygon(screen, color, [(x2, y2), (x3, y3), (x4, y4), (x5, y5), (x2, y2)])

    def draw_edge(self, screen):
        if not Edge.directed:
            pygame.draw.line(screen, self.color, (self.start_x, self.start_y), (self.end_x, self.end_y), self.width)
        else:
            pygame.draw.line(screen, self.color, (self.start_x, self.start_y), (self.end_x, self.end_y), self.width)
            self.draw_arrow(self.start_x, self.start_y, self.end_x, self.end_y, screen, self.color)


class Node:
    all_nodes = []
    radius = 20

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.node_no = len(Node.all_nodes)
        Node.all_nodes.append(self)
        self.color = BLACK
        self.cir_width = 2
        self.source_of = []
        self.dest_of = []
        everything.append(self)
        self.visited = False

    def draw_node(self, screen):
        textx = self.x - 5
        texty = self.y - 5
        pygame.draw.circle(screen, self.color, (self.x, self.y), Node.radius, self.cir_width)
        text(screen, str(self.node_no), textx, texty, 20, BLACK)


# Draw all nodes
def draw_all_nodes(screen):
    for node in Node.all_nodes:
        node.draw_node(screen)


def draw_all_edges(screen):
    for edge in Edge.all_edges:
        edge.draw_edge(screen)


# Is the point closer to the earlier drawn circle
def is_near(x, y):
    for node in Node.all_nodes:
        if (x > (node.x - 2 * Node.radius)) and (x < (node.x + 2 * Node.radius)) and (
                y > (node.y - 2 * Node.radius)) and (y < (node.y + 2 * Node.radius)):
            return True
    return False


# is the given point inside any of the nodes/circles
def is_in(x, y):
    for node in Node.all_nodes:
        if (x > (node.x - Node.radius)) and (x < (node.x + Node.radius)) and (y > (node.y - Node.radius)) and (
                y < (node.y + Node.radius)):
            return node
    return False


# distance between two points on a plane
def dist(x1, x2, y1, y2):
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


# Class 12 formula to calculate co-ordinates given a line divides 2 points in the ratio m:n
def get_co_ordinate(a, b, m, n):
    return (m * a + n * b) / (m + n)


def construct_matrix(all_nodes, all_edges):
    size = len(all_nodes)
    mat = [[0] * size]
    for i in range(size - 1):
        mat.append([0] * size)
    for i in range(size):
        for j in range(size):
            if i != j:
                for k in range(len(all_nodes[i].source_of)):
                    if all_nodes[i].source_of[k] in all_nodes[j].dest_of:
                        mat[i][j] = 1  # starts[k]
                        break
