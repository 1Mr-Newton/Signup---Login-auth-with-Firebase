from flet import *
from utils.extras import *

class LoginPage(Container):
  def __init__(self,switch_page,name,email,dp,):
    super().__init__()
    self.name = name
    self.email = email
    self.dp_url = dp
    self.offset = transform.Offset(0,0,)
    self.switch_page = switch_page
    self.expand = True
    self.view_hide_text = Text(
      value='View',
      color=base_color,
      font_family='poppins medium',
      
    )

    self.pwd_input = Container(
      height=btn_height,
      bgcolor='white',
      border_radius=10,
      # padding=20,
      content=TextField(
        on_focus=self.password_field_in_focus,
        password=True,
        suffix=Container(
          on_click=self.view_hide_password,
          content=self.view_hide_text,                              
        ),
        hint_text='Password',
        hint_style=TextStyle(
          size=16,
          font_family='Poppins Regular',
          color=input_hint_color,
        ),
        text_style=TextStyle(
          size=16,
          font_family='Poppins Regular',
          color=input_hint_color,
        ),
        border=InputBorder.NONE,
        content_padding=content_padding,
        selection_color=base_green,
        cursor_color=base_color
      )
    )

    self.error = Row(
      controls=[
        Image(
          src='assets/icons/danger.png',
          # scale=0.8,

        ),
        Text(
          value='Please enter the correct password to login',
          color='red',
          font_family='poppins regular'

        )
      ]
    )
    
    self.login_box = Column(
      controls=[
        Row(
          controls=[
            Container(
              height=50,width=50,bgcolor='white',border_radius=25,
              image_fit=ImageFit.COVER,image_src=img_src
            ),
            Column(
              spacing=0,
              controls=[
                Text(
                  value=self.name,
                  font_family='Poppins Semibold',
                  size=14,
                ),
                Text(
                  value=self.email,
                  font_family='Poppins light',
                  size=14,
                ),
              ]
            )
          ]
        ),
        
        Container(height=2),
        
        self.pwd_input,
        
        Container(height=1),

        # self.error,
        
        Container(height=1),

        Container(
          data = 'login_clicked',
          on_click= self.switch_page,
          height=btn_height,
          width=btn_width,
          bgcolor=base_green,
          border_radius=10,
          alignment=alignment.center,
          content=Text(
            value='Continue',
            font_family='Poppins Medium',
            size=16,

          )
        ),
        Container(height=5),


        
        Container(
          content=Text(
            value="Forgot your password?",
            size=14,
            font_family='poppins medium',
            color=base_green
          ),
        ),
        
        Container(height=5),

      ]
    )



    self.content = Container(
        height=base_height,
        width=base_width,
        bgcolor=base_color,
        clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
        border_radius=br,
        
        content=Stack(
          controls=[
            Container(
              height=base_height,
              width=base_width,
              left=60,
              top=-200,
              content=Image(
                src='assets/images/2.png',
                scale=0.9,
              )
            ),
            Container(
              border_radius=br,
              height=base_height,
              width=base_width,
              
              padding=padding.only(top=30,left=10,right=10,),
              content=Column(
                controls=[
                  Container(
                    on_click=self.switch_page,
                    data='main_page',
                    content=Icon(
                      icons.ARROW_BACK_IOS_OUTLINED,
                      size=28
                    )
                  ),
                  Container(height=160),
                  Container(
                    margin=margin.only(left=20),
                    content=Text(
                      value='Login',
                      font_family='Poppins Bold',
                      size=30,
                    ),
                  ),
                  Container(height=2),
                  Container(
                    padding=20,
                    # height=550,
                    bgcolor='#cc2d2b2c',
                    border_radius=10,
                    content=self.login_box,
                  ),
                ]
              )

            )
           
          ]
        )
        
      )
    

  def password_field_in_focus(self,e):

    y = self.error in self.login_box.controls
    if y == True:
      self.login_box.controls.remove(self.error)
      self.pwd_input.bgcolor = 'white'
      self.pwd_input.border = None
      self.pwd_input.update()
      self.login_box.update()

      # pass
  def view_hide_password(self,e):
    det = self.pwd_input.content.password
    if det == True:
      self.pwd_input.content.password = False
      self.view_hide_text.value = 'Hide'
    else:
      self.view_hide_text.value = 'View'
      self.pwd_input.content.password = True
    self.pwd_input.content.update()
    self.view_hide_text.update()



