from unittest import TestCase
from ReqTracer import requirements
from pyTona.main import Interface
from datetime import datetime
import getpass


class TestAcceptableAnswers(TestCase):

    Q_MARK =  chr(0x3E)

    @requirements(['#0001'])
    def test_accept_q_strings_fail(self):
        comp = Interface()

        with self.assertRaises(Exception) as e:
            comp.ask(123)

        self.assertEqual(e.exception.message, "Not A String!")
        self.assertEqual(comp.last_question, None)

    @requirements(['#0002', '#0003'])
    def test_answer_hwwww_fail(self):
        comp = Interface()

        ret = comp.ask("This doesn't start with a keyword.")

        self.assertEqual(ret, "Was that a question?")

    @requirements(['#0004'])
    def test_answer_no_q_mark(self):
        comp = Interface()

        ret = comp.ask("This doesn't end with a " + self.Q_MARK + ".")

        self.assertEqual(ret, "Was that a question?")

    @requirements(['#0004', '#0009'])
    def test_valid_questions_unknown_answers(self):
        comp = Interface()

        how = comp.ask("How are you doing" + self.Q_MARK)
        what = comp.ask("What is the temperature" + self.Q_MARK)
        where = comp.ask("Where are you going" + self.Q_MARK)
        why = comp.ask("Why are you here" + self.Q_MARK)
        who = comp.ask("Who are you" + self.Q_MARK)

        self.assertEqual(how, "I don't know, please provide the answer")
        self.assertEqual(what, "I don't know, please provide the answer")
        self.assertEqual(where, "I don't know, please provide the answer")
        self.assertEqual(why, "I don't know, please provide the answer")
        self.assertEqual(who, "I don't know, please provide the answer")

    @requirements(['#0008', '#0017'])
    def test_valid_question_miles(self):
        comp = Interface()

        miles = comp.ask("What is 17.9 feet in miles" + self.Q_MARK)

        self.assertEqual(miles, str(float(17.9) / 5280) + "miles")

    @requirements(['#0008', '#0018'])
    def test_valid_question_time_since(self):
        comp = Interface()

        time_since = comp.ask("How many seconds since 2015-04-22 00:00:00" + self.Q_MARK)

        test_time = datetime.strptime("2015-04-22 03:30:00", "%Y-%m-%d %H:%M:%S")
        self.assertEqual(time_since, (datetime.now() - test_time).seconds)

    @requirements(['#0008', '#0019'])
    def test_valid_question_inventor(self):
        comp = Interface()

        inventor = comp.ask("Who invented python" + self.Q_MARK)

        self.assertEqual(inventor, "Guido Rossum(BFDL)")

    @requirements(['#0008', '#0020'])
    def test_valid_question_understand(self):
        comp = Interface()

        understand = comp.ask("Why don't you understand me" + self.Q_MARK)

        self.assertEqual(understand, "Because you do not speak 1s and 0s")

    @requirements(['#0008', '#0021'])
    def test_valid_question_shutdown(self):
        comp = Interface()

        shutdown = comp.ask("Why don't you shutdown" + self.Q_MARK)

        self.assertEqual(shutdown, "I'm afraid I can't do that " + getpass.getuser())

    @requirements(['#0010', '#0011'])
    def test_provide_answer_text(self):
        comp = Interface()

        response = comp.ask("What is your name" + self.Q_MARK)
        self.assertEqual(response, "I don't know, please provide the answer")

        comp.teach("My name is Interface")

        response = comp.ask("What is your name" + self.Q_MARK)
        self.assertEqual(response, "My name is Interface")

    @requirements(['#0010', '#0011'])
    def test_provide_answer_func(self):
        comp = Interface()

        response = comp.ask("What is the abs of -10 " + self.Q_MARK)
        self.assertEqual(response, "I don't know, please provide the answer")

        comp.teach(abs)

        response = comp.ask("What is the abs of -10 " + self.Q_MARK)
        self.assertEqual(response, 10)

    @requirements(['#0010', '#0012'])
    def test_no_pre_q(self):
        comp = Interface()

        response = comp.teach("Oompa Loompa")
        self.assertEqual(response, "Please ask a question first")

    @requirements(['#0010', '#0013'])
    def test_teach_overwrite(self):
        comp = Interface()

        comp.ask("Why don't you understand me" + self.Q_MARK)

        response = comp.teach("Because you don't speak assembly")
        self.assertEqual(response, "I don't know about that. I was taught differently")

        response = comp.ask("Why don't you understand me" + self.Q_MARK)
        self.assertEqual(response, "Because you do not speak 1s and 0s")

    @requirements(['#0014', '#0015'])
    def test_correction_text(self):
        comp = Interface()

        comp.ask("Who invented Python" + self.Q_MARK)
        comp.correct("Guido Rossum")
        response = comp.ask("Who invented Python" + self.Q_MARK)

        self.assertEqual(response, "Guido Rossum")

    @requirements(['#0014', '#0015'])
    def test_correction_func(self):
        comp = Interface()

        comp.ask("What is the abs of -10 " + self.Q_MARK)
        comp.teach("I don't know")

        comp.ask("What is the abs of -10 " + self.Q_MARK)
        comp.correct(abs)

        response = comp.ask("What is the abs of -10 " + self.Q_MARK)
        self.assertEqual(response, 10)

    @requirements(['#0014', '#0016'])
    def test_correction_no_pre_q(self):
        comp = Interface()

        response = comp.correct(abs)
        self.assertEqual(response, "Please ask a question first")

    @requirements(['#0005'])
    def test_no_space_fail(self):
        comp = Interface()

        response = comp.ask("Why don'tyouunderstandme" + self.Q_MARK)
        self.assertEqual(response, "Was that a question?")

    @requirements(['#0005', '#0007'])
    def test_number_extraction(self):
        comp = Interface()

        response = comp.ask("What is 50feet in miles" + self.Q_MARK)

        self.assertEqual(response, str(float(50) / 5280) + "miles")

    @requirements(['#0006', '#0007'])
    def test_number_extration_and_90(self):
        comp = Interface()

        qm100_if_no_num = "Um What is 5280 feet in miles" + self.Q_MARK
        q100_if_no_num = "What is 5280 feet in miles" + self.Q_MARK
        q_90_if_no_num = "What is 5280 ft in miles" + self.Q_MARK
        q_l90 = "What is 5280 in miles" + self.Q_MARK

        am100 = comp.ask(qm100_if_no_num)
        a100 = comp.ask(q100_if_no_num)
        a90 = comp.ask(q_90_if_no_num)
        al90 = comp.ask(q_l90)

        self.assertEqual(am100, str(float(5280) / 5280) + "miles")
        self.assertEqual(a100, str(float(5280) / 5280) + "miles")
        self.assertEqual(a90, str(float(5280) / 5280) + "miles")
        self.assertEqual(al90, "I don't know, please provide the answer")