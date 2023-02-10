from flet import *
from utils.extras import *

class SignupPage(Container):
  def __init__(self,switch_page,email):
    super().__init__()
    self.email = email
    self.offset = transform.Offset(0,0,)
    self.switch_page = switch_page

    self.expand = True
    self.password_box = TextField(
      password=True,
      suffix=Container(
        on_click=lambda _: print('yeah'),
        content=Text(
          value='View',
          color=base_color,
          font_family='poppins medium',
          
        ),                              
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
    
    self.name_box = TextField(
      hint_text='Name',
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
      content_padding=content_padding
    )

    self.error = Row(
      controls=[
        Image(
          src='assets/icons/danger.png',
          # scale=0.8,

        ),
        Text(
          value='Please check your email address.',
          color='red',
          font_family='poppins regular'

        )
      ]
    )
    
    self.content = Container(
        # padding=padding.symmetric(horizontal=8,vertical=20),
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
                    data = 'main_page',
                    on_click = self.switch_page,
                    content=Icon(
                      icons.ARROW_BACK_IOS_OUTLINED,
                      size=28
                    ),
                  ),

                  Container(height=160),

                  Container(
                    margin=margin.only(left=20),
                    content=Text(
                      value='Sign up',
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
                    content=Column(
                      controls=[
                        Column(
                          spacing=0,
                          controls=[
                            Text(
                              value=f'Looks like you don\'t have an account.\nLet\'s create a new account for',
                              size=14,
                              font_family='poppins light',
                              color='#ccffffff'
                            ),
                            Text(
                              value=self.email,
                              size=14,
                              font_family='poppins medium',
                              color='#ccffffff'
                            ),
                          ]
                        ),
                        Container(height=1),
                        Container(
                          height=btn_height,
                          bgcolor='white',
                          border_radius=10,
                          # padding=20,
                          content=self.name_box,
                        ),
                        Container(height=1),

                        Container(
                          height=btn_height,
                          bgcolor='white',
                          border_radius=10,
                          # padding=20,
                          content=self.password_box,
                        ),
                        Container(height=1),
                        Container(
                          content=Column(
                            spacing=0,
                            controls=[
                              Text(
                                value="By clicking 'Agree and Continue' below,",
                                size=14,
                                font_family='poppins light',
                                color='#ccffffff'
                              ),
                              Row(
                                spacing=0,
                                controls=[
                                  Text(
                                    value="I agree to ",
                                    size=14,
                                    font_family='poppins light',
                                    color='#ccffffff'
                                  ),
                                  Text(
                                    value="Terms of Service and Privacy Policy",
                                    size=14,
                                    font_family='poppins medium',
                                    color=base_green
                                  ),
                                ]
                              )
                            ]
                          )
                        ),

                        
                        Container(height=1),
                        
                        Container(
                          data='register',
                          on_click=self.switch_page,
                          height=btn_height,
                          width=btn_width,
                          bgcolor=base_green,
                          border_radius=10,
                          alignment=alignment.center,
                          content=Text(
                            value='Agree and Continue',
                            font_family='Poppins Medium',
                            size=16,

                          )
                        ),
                        
                        



                      ]
                    )
                  ),
                ]
              )

            )
           
          ]
        )
        
      )
    