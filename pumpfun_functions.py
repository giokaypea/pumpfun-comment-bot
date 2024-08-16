import random
import time
import playwright
from playwright.sync_api import Page, sync_playwright, BrowserContext, Browser, ElementHandle

p = sync_playwright().start()

def random_wait():
    ........
    
def open_browser(debugger_address:str):
    ........

def create_phantom_wallet(page:Page):
    ..........

def authenticate(page:Page, context:BrowserContext):
    ........

def sort_by(page:Page, by:str="creation time"):
    ........

def click_on_first_project(page:Page):
    ........

def post_comment(page:Page, comment:str, image:str=None):
    ........
    
class CommentException(Exception):
    pass