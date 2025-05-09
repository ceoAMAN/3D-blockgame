from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
player = FirstPersonController()
Sky()

boxes = []
for i in range(20):
 for j in range(20):
  box = Button(color=color.white, model='cube', position=(i, 0, j),
    texture='grass', parent=scene, origin_y=0.5)
  box.append(box)
   
def inpurt(key):
  for box in boxes:
   if box.hovered:
     if key == 'left mouse down':
       new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                    texture='grass', parent=scene, origin_y=0.5)            
       boxes.append(new)   
     if key == 'right mouse down':
       boxes.remove(box)
       destroy(box)

app.run()
