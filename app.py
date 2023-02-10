from flet import *
import pickle
from utils.extras import *
from pages.mainpage import MainPage
from pages.login import LoginPage
from pages.signup import SignupPage
from pages.dashboard import DashboardPage
from service.auth import get_user,authenticate, verify_token, register_user, is_valid_email
import asyncio

async def save_token(token):
  try:
    with open("token.pkl", "wb") as f:
      pickle.dump(token, f)
    return 'Saved'
  except:
    return None 



async def load_token():
  try:
    with open("token.pkl", "rb") as f:
      stored_token = pickle.load(f)
    return stored_token
  except:
    return None



class WindowDrag(UserControl):
  def __init__(self):
    super().__init__()
    # self.color = color
  def build(self):
    return Container(content=WindowDragArea(height=10,content=Container(bgcolor='white')))


class App(UserControl):
  def __init__(self,pg:Page):
    super().__init__()

    pg.window_title_bar_hidden = True
    pg.window_frameless = True
    pg.window_title_bar_buttons_hidden = True
    pg.bgcolor = colors.TRANSPARENT
    pg.window_bgcolor = colors.TRANSPARENT
    pg.fonts = {
    "SF Pro Bold":"fonts/SFProText-Bold.ttf",
    "SF Pro Heavy":"fonts/SFProText-Heavy.ttf",
    "SF Pro HeavyItalic":"fonts/SFProText-HeavyItalic.ttf",
    "SF Pro Light":"fonts/SFProText-Light.ttf",
    "SF Pro Medium":"fonts/SFProText-Medium.ttf",
    "SF Pro Regular":"fonts/SFProText-Regular.ttf",
    "SF Pro Semibold":"fonts/SFProText-Semibold.ttf",
    "SF Pro SemiboldItalic":"fonts/SFProText-SemiboldItalic.ttf",
    
    
    "Poppins ThinItalic":"fonts/poppins/Poppins-ThinItalic.ttf",
    "Poppins Thin":"fonts/poppins/Poppins-Thin.ttf",
    "Poppins Semibold":"fonts/poppins/Poppins-Semibold.ttf",
    "Poppins SemiboldItalic":"fonts/poppins/Poppins-SemiboldItalic.ttf",
    "Poppins Regular":"fonts/poppins/Poppins-Regular.ttf",
    "Poppins MediumItalic":"fonts/poppins/Poppins-MediumItalic.ttf",
    "Poppins Medium":"fonts/poppins/Poppins-Medium.ttf",
    "Poppins LightItalic":"fonts/poppins/Poppins-LightItalic.ttf",
    "Poppins Light":"fonts/poppins/Poppins-Light.ttf",
    "Poppins Italic":"fonts/poppins/Poppins-Italic.ttf",
    "Poppins ExtraLightItalic":"fonts/poppins/Poppins-ExtraLightItalic.ttf",
    "Poppins ExtraLight":"fonts/poppins/Poppins-ExtraLight.ttf",
    "Poppins ExtraBold":"fonts/poppins/Poppins-ExtraBold.ttf",
    "Poppins ExtraBoldItalic":"fonts/poppins/Poppins-ExtraBoldItalic.ttf",
    "Poppins BoldItalic":"fonts/poppins/Poppins-BoldItalic.ttf",
    "Poppins Bold":"fonts/poppins/Poppins-Bold.ttf",
    "Poppins BlackItalic":"fonts/poppins/Poppins-BlackItalic.ttf",
    "Poppins Black":"fonts/poppins/Poppins-Black.ttf",
  }
    pg.window_width = base_width
    pg.window_height = base_height



    auth = asyncio.run(verify_token(asyncio.run(load_token())))
    self.pg  = pg
    self.pg.spacing = 0
    self.delay = 0.1
    self.anim = animation.Animation(300,AnimationCurve.EASE_IN_OUT_CUBIC)

    self.main_page = MainPage(self.switch_page)
    
    self.screen_views = Stack(
        expand=True,
        controls=[
          self.main_page if not auth else DashboardPage(self.switch_page, auth["email"]),
        ]
      )

    self.init_helper()

  def switch_page(self,e):
    if e.control.data == 'register':
      name = self.signup_page.name_box.value
      password = self.signup_page.password_box.value
      email = self.main_page.email_input.content.value
   
      user = register_user(name, email, password)
      self.screen_views.controls.clear()
      self.screen_views.controls.append(DashboardPage(self.switch_page,email,))
      self.screen_views.update()
      return


    elif e.control.data == 'process_login':
      email = self.main_page.email_input.content.value
      if is_valid_email(email):
        user = get_user(email)
        if user:
          id = user[0]
          self._name = user[1]
          self._email = user[2]
          self.screen_views.controls.clear()
          self.login_page = LoginPage(self.switch_page,name=self._name,email=self._email,dp='')
          # self.login_page.content.on_focus = self.hide_error
          self.screen_views.controls.append(self.login_page)
          self.screen_views.update()
        else:
          self.screen_views.controls.clear()  
          self.signup_page = SignupPage(self.switch_page,email)
          self.screen_views.controls.append(self.signup_page)
          self.screen_views.update()
      else:
        self.main_page.email_input.bgcolor = input_error_bg
        self.main_page.email_input.border = border.all(width=2,color=input_error_outline)
        
        self.main_page.main_content.controls.insert(1,self.main_page.error)

        self.main_page.update()
        # self.main_page.email_input.update()
        
      
    elif e.control.data == 'main_page':
      self.screen_views.controls.clear()
      self.screen_views.controls.append(self.main_page)
      self.screen_views.update()
      
    elif e.control.data == 'login_clicked':
      password = self.login_page.pwd_input.content.value
      email = self.login_page.email

      auth = authenticate(email,password)
      if auth:
        asyncio.run(save_token(auth))
        self.screen_views.controls.clear()
        self.screen_views.controls.append(DashboardPage(self.switch_page,email))
        self.screen_views.update()

      else:
        self.login_page.login_box.controls.insert(4,self.login_page.error)  
        self.login_page.pwd_input.bgcolor = input_error_bg
        self.login_page.pwd_input.border=border.all(width=2, color=input_error_outline)
        self.login_page.pwd_input.update()
        self.login_page.login_box.update()

    elif e.control.data == 'logout':
      try:
        os.remove('token.pkl')  
      except:
        pass
      self.screen_views.controls.clear()
      self.screen_views.controls.append(self.main_page)
      self.screen_views.update()

    


      

  def init_helper(self):
    self.pg.add(
      WindowDrag(),
      self.screen_views 
    )


app(target=App,assets_dir='assets')