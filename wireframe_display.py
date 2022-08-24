import wireframe
import pygame

class ProjectionViewer:
    def __init__(self, width, height):
        self.width = width
        self.heihgt = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Wireframe Display")
        self.background = (10,10,50)

        self.wireframes = {}
        self.displayNodes = True
        self.displayEdges = True
        self. nodeColour = (255,255,255)
        self.edgeColour = (200,200,200)
        self.nodeRadius = 4

    def run(self):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill(self.background)
            pygame.display.flip()  

if __name__ == '__main__':
    pv = ProjectionViewer(400, 300)
    pv.run()