import kivy
import databaseScript
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window


class MyDisplay(Widget):
    eventdetails = StringProperty(databaseScript.eventdetails)


class NoticeBoard(App):

    def build(self):
        Window.clearcolor = (0,1,0.2,1)
        return MyDisplay()


noticeBoard = NoticeBoard()
noticeBoard.run()