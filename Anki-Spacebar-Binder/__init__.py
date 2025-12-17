# Anki Spacebar Button Binder

# This add-on changes which answer button is selected when you press the spacebar during reviews

from aqt.reviewer import Reviewer

def my_defaultEase(self):

    """
    Anki uses numbers for answer buttons:

    1 = again
    2 = hard
    3 = good
    4 = easy

    TO CHANGE THE SPACEBAR BEHAVIOR, CHANGE THE NUMBER BELOW...
    """

    return 2

# Override Anki's default spacebar behavior

Reviewer._defaultEase = my_defaultEase

# Created by Ryleigh Newman. Wanna say hi? ryleighnewman.com