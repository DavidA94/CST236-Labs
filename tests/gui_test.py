import pywinauto
import time
from pywinauto import application
from unittest import TestCase


class TestSharpTonaGUI(TestCase):
    app = None

    def setUp(self):
        self.app = application.Application()
        self.app.start_("SharpTona.exe")

    def tearDown(self):
        self.app.SharpTona.TypeKeys("%{F4}")
        self.app = None

    def test_title_bar(self):
        # Check the title
        self.assertEqual(self.app.SharpTona.WindowText(), "SharpTona")

    def test_has_question_label(self):
        # Check for the question label
        self.assertEqual(self.app.SharpTona["Question"].Texts()[0], "Question:")

    def test_has_answer_label(self):
        # Check for the answer label
        self.assertEqual(self.app.SharpTona["Answer"].Texts()[0], "Answer: ")

    def test_has_question_answer_box_ask_button(self):
        # Check for a place to enter a question
        self.assertEqual(self.app.SharpTona["Question:Edit"].friendlyclassname, "Edit")
        # And an ask button
        self.assertEqual(self.app.SharpTona["Ask"].friendlyclassname, "Button")

    def test_everything_answer(self):
        # Focus on the question box and ask the question
        self.app.SharpTona["Question:Edit"].SetFocus()
        self.app.SharpTona["Question:Edit"].TypeKeys("What is the answer to everything?",with_spaces=True)
        # Click ask
        self.app.SharpTona["Ask"].Click()
        # Check the answer
        self.assertEqual(self.app.SharpTona["Answer:Edit"].Texts()[0], "42")

    def test_teach_correct_disabled(self):
        # Ensure that the Teach button is disabled
        self.assertFalse(self.app.SharpTona['Teach'].IsEnabled())
        # Ensure that the Correct button is disabled
        self.assertFalse(self.app.SharpTona['Correct'].IsEnabled())

    def test_is_a_question(self):
        # Ensure that when the ask button is clicked, and nothing has been asked
        self.app.SharpTona["Ask"].Click()
        # It asks if that was a question
        self.assertEqual(self.app.SharpTona["Answer:Edit"].Texts()[0], "Was that a question?")

    def test_press_ask_enable_typing(self):
        # Ensure that when a question is asked
        self.app.SharpTona["Question:Edit"].TypeKeys("What is the answer to everything?",with_spaces=True)
        self.app.SharpTona["Ask"].Click()
        # The answer is returned
        self.assertEqual(self.app.SharpTona["Answer:Edit"].Texts()[0], "42")
        # And we cna type into the answer box
        self.assertTrue(self.app.SharpTona["Answer:Edit"].IsEnabled())

    def test_press_correct_disable_all(self):
        # Ensure that when a question is ashed
        self.app.SharpTona["Question:Edit"].TypeKeys("What is the answer to everything?",with_spaces=True)
        self.app.SharpTona["Ask"].Click()
        # That we can then type into the answer box a new answer
        self.app.SharpTona["Answer:Edit"].SetFocus()
        self.app.SharpTona["Answer:Edit"].TypeKeys("Jesus Christ {(}Heb 2:8 KJV{)}", with_spaces=True)
        # Click correct
        self.app.SharpTona["Correct"].Click()
        # And answer, teach, and correct will all be disabled
        self.assertFalse(self.app.SharpTona["Answer:Edit"].IsEnabled())
        self.assertFalse(self.app.SharpTona["Teach"].IsEnabled())
        self.assertFalse(self.app.SharpTona["Correct"].IsEnabled())
        # Also ensure the answer has been updated
        self.app.SharpTona["Ask"].Click()
        self.assertEqual(self.app.SharpTona["Answer:Edit"].Texts()[0], "Jesus Christ (Heb 2:8 KJV)")
        # And that it was re-asked (Because the box should be typeable again if so)
        self.assertTrue(self.app.SharpTona["Answer:Edit"].IsEnabled())

    def test_no_known_answer(self):
        # Ensure that when an unkown question is asked
        self.app.SharpTona["Question:Edit"].TypeKeys("Who are you?",with_spaces=True)
        self.app.SharpTona["Ask"].Click()
        # That the system asks for the answer
        self.assertEqual(self.app.SharpTona["Answer:Edit"].Texts()[0], "I don't know please teach me.")
        # And that the teach button is now enabled (Bot not correct)
        self.assertTrue(self.app.SharpTona["Teach"].IsEnabled())
        self.assertFalse(self.app.SharpTona["Correct"].IsEnabled())
        # Then provide a new answer
        self.app.SharpTona["Answer:Edit"].TypeKeys("I am SharpTona.", with_spaces=True)
        # Click Teach
        self.app.SharpTona["Teach"].Click()
        # Ensure everything is now disabled
        self.assertFalse(self.app.SharpTona["Answer:Edit"].IsEnabled())
        self.assertFalse(self.app.SharpTona["Teach"].IsEnabled())
        self.assertFalse(self.app.SharpTona["Correct"].IsEnabled())
        # Then re-ask the question
        self.app.SharpTona["Ask"].Click()
        # Ensure the answer is now correct
        self.assertEqual(self.app.SharpTona["Answer:Edit"].Texts()[0], "I am SharpTona.")
        # And that it was re-asked (Because the box should be typeable again if so)
        self.assertTrue(self.app.SharpTona["Answer:Edit"].IsEnabled())