from flet import *
from utils.extras import *

class DashboardPage(Container):
  def __init__(self,switch_page,email,):
    super().__init__()
    self.offset = transform.Offset(0,0,)
    self.email = email
    self.switch_page = switch_page
    self.expand = True
    self.content = Container(
      
        height=base_height,
        width=base_width,
        bgcolor=base_color,
        clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
        border_radius=br,
        
        content=Column(
          alignment='center',
          horizontal_alignment='center',
          controls=[
            Text(
              value=f'Hello!',
              
            ),
            Text(
              value=f'Your email is\n{self.email}',
              
            ),
            Container(
              on_click= self.switch_page,
              data ='logout',
              height=50,
              width=100,
              border_radius=30,
              bgcolor='white',
              content=Icon(
                icons.LOGOUT_OUTLINED,
                color='black'
              )
            )
          ]
        )
        
      )
      