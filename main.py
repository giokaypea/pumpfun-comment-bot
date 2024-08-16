import random
import time
........
from playwright.sync_api import Page, sync_playwright, BrowserContext
from gologin_functions import create_profile, delete_profile, quit_and_delete_profile, quit_profile, start_profile
from other_functions import EmptyCommentsFile, get_image_path_and_comment
from pumpfun_functions import *
import traceback

posts_commented_on = []
index = 0

with open('Data/settings.txt', 'r') as file:
    lines = file.read().strip().split('\n')
    ........

........
    gl_start = None
    profile_id = None
    page, context = None, None

    try:
        print("Creating profile")
        profile_id = create_profile()
        print(f"Created profile [{profile_id}]")

        print("Starting profile")
        ........
        print(f"Started profile [{profile_id}]")

        page, context = ........

        print("Creating dummy phantom wallet")
        create_phantom_wallet(page)
        print("Created dummy phantom wallet")

        print("Authenticating on pumpfun")
        authenticate(page, context)
        print("Authenticated on pumpfun")

        for x in range(10):
            print(f"Starting {x} comment")
            if(by != "bump order"):
                ........
            else:
                print("Default (bump order) selected, skipping sort")

            print("Clicking on first project")
            click_on_first_project(page)
            ........

            posted_comment = None
            retry_count = 0
            while(posted_comment is None and retry_count < 2):
                image_path, comment = get_image_path_and_comment()
                if(comment is None):
                    ........
                print(f"Using comment {comment} and image {image_path}")
                posted_comment = post_comment(page, comment, image_path)
                ........
            if retry_count == 2:
                raise CommentException("Failed to post comment after 2 retries")

            posts_commented_on.append(posted_comment)
            ........

        quit_and_delete_profile(gl_start, profile_id)

        print(f"Restarting in 5 seconds. Posts commented: {posts_commented_on}")
        time.sleep(5)
    except Exception as e:
        print(f"Failed with error: {str(e)}, Posts Commented On: {posts_commented_on}")

        if isinstance(e, EmptyCommentsFile):
            break

        if page is not None:
            ........

        with open('Data/errors.txt', 'a') as file:
            ........

        if(gl_start is not None):
            ........