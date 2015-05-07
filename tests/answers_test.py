from unittest import TestCase
from ReqTracer import requirements
from pyTona.main import Interface
import pyTona.answer_funcs
#from predef_dict import predef_dict
import getpass
import subprocess
import mock
import socket
import random
import time


def mutate_data(func, *args, **kwargs):
    if not hasattr(mutate_data, 'funcs'):
        mutate_data.funcs = {}

    if func not in mutate_data.funcs:
            mutate_data.funcs[func] = None
            return func(*args, **kwargs)
    else:
        return None


class TestAcceptableAnswers(TestCase):

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

        ret = comp.ask("This doesn't end with a ?.")

        self.assertEqual(ret, "Was that a question?")

    @requirements(['#0004', '#0009'])
    def test_valid_questions_unknown_answers(self):
        comp = Interface()

        how = comp.ask("How are you doing?")
        what = comp.ask("What is the temperature?")
        where = comp.ask("Where are you going?")
        why = comp.ask("Why are you here?")
        who = comp.ask("Who are you?")

        self.assertEqual(how, "I don't know, please provide the answer")
        self.assertEqual(what, "I don't know, please provide the answer")
        self.assertEqual(where, "I don't know, please provide the answer")
        self.assertEqual(why, "I don't know, please provide the answer")
        self.assertEqual(who, "I don't know, please provide the answer")

    @requirements(['#0008', '#0017'])
    def test_valid_question_miles(self):
        comp = Interface()

        miles = comp.ask("What is 17.9 feet in miles?")

        self.assertEqual(miles, str(float(17.9) / 5280) + " miles")

    @requirements(['#0008', '#0019'])
    def test_valid_question_inventor(self):
        comp = Interface()

        inventor = mutate_data(comp.ask, "Who invented python?")
        self.assertEqual(inventor, "Guido Rossum(BDFL)")
        inventor = mutate_data(comp.ask, "Who invented python?")
        self.assertNotEqual(inventor, "Guido Rossum(BDFL)")

    @requirements(['#0008', '#0020'])
    def test_valid_question_understand(self):
        comp = Interface()

        understand = comp.ask("Why don't you understand me?")

        self.assertEqual(understand, "Because you do not speak 1s and 0s")

    @requirements(['#0008', '#0021'])
    def test_valid_question_shutdown(self):
        comp = Interface()

        shutdown = comp.ask("Why don't you shutdown?")
        self.assertEqual(shutdown, "I'm afraid I can't do that " + getpass.getuser())

    @requirements(['#0010', '#0011'])
    def test_provide_answer_text(self):
        comp = Interface()

        response = comp.ask("What is your name?")
        self.assertEqual(response, "I don't know, please provide the answer")

        comp.teach("My name is Interface")

        response = comp.ask("What is your name?")
        self.assertEqual(response, "My name is Interface")

    @requirements(['#0010', '#0011'])
    def test_provide_answer_func(self):
        comp = Interface()

        response = comp.ask("What is the abs of -10?")
        self.assertEqual(response, "I don't know, please provide the answer")

        comp.teach(abs)

        response = comp.ask("What is the abs of -10?")
        self.assertEqual(response, 10)

    @requirements(['#0010', '#0012'])
    def test_no_pre_q(self):
        comp = Interface()

        response = comp.teach("Oompa Loompa")
        self.assertEqual(response, "Please ask a question first")

    @requirements(['#0010', '#0013'])
    def test_teach_overwrite(self):
        comp = Interface()

        comp.ask("Why don't you understand me?")

        response = comp.teach("Because you don't speak assembly")
        self.assertEqual(response, "I don't know about that. I was taught differently")

        response = comp.ask("Why don't you understand me?")
        self.assertEqual(response, "Because you do not speak 1s and 0s")

    @requirements(['#0014', '#0015'])
    def test_correction_text(self):
        comp = Interface()

        comp.ask("Who invented Python?")
        comp.correct("Guido Rossum")
        response = comp.ask("Who invented Python?")

        self.assertEqual(response, "Guido Rossum")

    @requirements(['#0014', '#0015'])
    def test_correction_func(self):
        comp = Interface()

        comp.ask("What is the abs of -10?")
        comp.teach("I don't know")

        comp.ask("What is the abs of -10?")
        comp.correct(abs)

        response = comp.ask("What is the abs of -10?")
        self.assertEqual(response, 10)

    @requirements(['#0014', '#0016'])
    def test_correction_no_pre_q(self):
        comp = Interface()

        response = comp.correct(abs)
        self.assertEqual(response, "Please ask a question first")

    @requirements(['#0005'])
    def test_no_space_fail(self):
        comp = Interface()

        response = comp.ask("Why doyouunderstandme?")
        self.assertEqual(response, "I don't know, please provide the answer")

    @requirements(['#0005', '#0007'])
    def test_number_extraction(self):
        comp = Interface()

        with self.assertRaises(Exception) as e:
            comp.ask("What is 50feet in miles?")

        self.assertEqual(e.exception.message, "Too many extra parameters")

    @requirements(['#0006', '#0007'])
    def test_number_extration_and_90(self):
        comp = Interface()

        qm100_if_no_num = "What um is 5280 feet in miles?"
        q100_if_no_num = "What is 5280 feet in miles?"
        q_90_if_no_num = "What is 5280 ft in miles?"
        q_l90 = "What is 5280 in miles?"

        am100 = comp.ask(qm100_if_no_num)
        a100 = comp.ask(q100_if_no_num)
        a90 = comp.ask(q_90_if_no_num)
        al90 = comp.ask(q_l90)

        self.assertEqual(am100, str(float(5280) / 5280) + " miles")
        self.assertEqual(a100, str(float(5280) / 5280) + " miles")
        self.assertEqual(a90, str(float(5280) / 5280) + " miles")
        self.assertEqual(al90, "I don't know, please provide the answer")

    def call_cmd_process(self, command):
        try:
            output = subprocess.check_output(command)
            return "Unknown" if not output else output.strip()
        except subprocess.CalledProcessError:
            return "Unknown"



    @requirements(['#0022'])
    def test_get_git_branch(self):
        comp = Interface()

        output = self.call_cmd_process(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
        response = comp.ask("Where am I?")

        self.assertEqual(output, response)

    @requirements(['#0022'])
    def test_git_git_branch_fail(self):
        comp = Interface()
        m = mock.Mock()
        m.return_value = [False]

        temp = subprocess.Popen.communicate
        subprocess.Popen.communicate = m

        response = comp.ask("Where am I?")
        self.assertEqual(response, "Unknown")

        m.side_effect = subprocess.CalledProcessError
        response = comp.ask("Where am I?")
        self.assertEqual(response, "Unknown")

        subprocess.Popen.communicate = temp

    @requirements(['#0023'])
    def test_get_git_url(self):
        comp = Interface()

        output = self.call_cmd_process(['git', 'config', '--get', 'remote.origin.url'])
        response = comp.ask("Where are you?")

        self.assertEqual(output, response)

    @requirements(['#0023'])
    def test_get_git_url_fail(self):
        comp = Interface()
        m = mock.Mock()
        m.return_value = [False]

        temp = subprocess.Popen.communicate
        subprocess.Popen.communicate = m

        response = comp.ask("Where are you?")
        self.assertEqual(response, "Unknown")

        m.side_effect = subprocess.CalledProcessError
        response = comp.ask("Where are you?")
        self.assertEqual(response, "Unknown")

        subprocess.Popen.communicate = temp

    @requirements(['#0024', '#0025', '#0026'])
    def test_which_users_are_here(self):
        comp = Interface()
        with mock.patch('socket.socket') as MockSock:
            instance = MockSock.return_value
            instance.connect.return_value = None
            instance.send.return_value = None
            instance.recv.return_value = "Lary$Amy$Mark$Edmund"

            response = comp.ask("Who else is here?")
            self.assertEqual(response, ["Lary", "Amy", "Mark", "Edmund"])
            instance.send.assert_called_with("Who?")
            instance.connect.assert_called_with(('192.168.64.3', 1337))


    @requirements(['#0024', '#0025', '#0026'])
    def test_which_users_are_here_real(self):
        return
        comp = Interface()
        res = "IT'S A TRAAAPPPP"
        try:
            s = socket.socket()
            s.connect(('192.168.64.3', 1337))
            s.send("Who?")
            data = s.recv(255)

            res = comp.ask("Who else is here?")

            self.assertEqual(res, data.split("$"))

        except:
            self.assertEqual(res, "IT'S A TRAAAPPPP")

    @requirements(['#0024', '#0025', '#0027'])
    def test_which_users_are_here_fail(self):
        comp = Interface()

        response = comp.ask("Who else is here?")

        self.assertEqual(response, "IT'S A TRAAAPPPP")

    @requirements(['#0028'])
    def test_fib_num(self):
        comp = Interface()

        # Ask
        comp.ask("What is the 2 digit of the Fibonacci sequence?")
        # Sleep so it can calculate
        time.sleep(.5)
        # Should have had enough time to calculate now.
        response = comp.ask("What is the 2 digit of the Fibonacci sequence?")
        self.assertEqual(response, 1)

    @requirements(['#0029'])
    def test_fib_num_fail(self):
        comp = Interface()

        m = mock.Mock()

        temp = random.randint
        random.randint = m

        m.return_value = 0
        response0 = comp.ask("What is the 999999 digit of the Fibonacci sequence?")
        m.return_value = 1
        response1 = comp.ask("What is the 999999 digit of the Fibonacci sequence?")
        m.return_value = 3
        response3 = comp.ask("What is the 999999 digit of the Fibonacci sequence?")
        m.return_value = 4
        response4 = comp.ask("What is the 999999 digit of the Fibonacci sequence?")
        m.return_value = 9
        response9 = comp.ask("What is the 999999 digit of the Fibonacci sequence?")

        self.assertEqual(response0, "cool your jets")
        self.assertEqual(response1, "One second")
        self.assertEqual(response3, "One second")
        self.assertEqual(response4, "Thinking...")
        self.assertEqual(response9, "Thinking...")

        pyTona.answer_funcs.seq_finder.stop()
        pyTona.answer_funcs.seq_finder = None



    @requirements(['#0030'])
    def test_1m_q_a(self): # To only be run manually... for now
        return
        comp = Interface()

        #comp.question_answers = predef_dict

        for i in range(10):
            rand = random.randint(0, 999999)
            response = comp.ask("What is {0}?".format(rand))
            self.assertEqual(response, "It is {0}".format(rand))

        self.assertEqual((len(comp.question_answers), 1000000))

    @requirements(['#0031'])
    def test_5ms_store_time(self):
        comp = Interface()

        comp.ask("How are you?")

        time1 = time.clock()
        comp.teach("I'm doing well today.")
        time2 = time.clock()

        self.assertLessEqual(time2 - time1, 5)

        time1 = time.clock()
        comp.correct("I'm feeling well today.")
        time2 = time.clock()

        self.assertLessEqual(time2 - time1, 5)

    @requirements(['#0032'])
    def test_5ms_answer_time(self):
        comp = Interface()

        time1 = time.clock()
        response = comp.ask("What is 6000 feet in miles?")
        time2 = time.clock()

        self.assertLessEqual(time2 - time1, 5)
        self.assertEqual(response, "{0} miles".format(float(6000) / 5280))

    @requirements(['#0033', '#0034'])
    def test_only_1000_fib(self):
        comp = Interface()

        time1 = time.clock()
        while(comp.ask("What is the 1000 digit of the fibonacci sequence?") in
              ("Thinking...", "One second", "cool your jets")):
            pass

        time2 = time.clock()

        self.assertLessEqual(time2 - time1, 60 * 1000)

        self.assertEqual(comp.ask("What is the 1000 digit of the fibonacci sequence?"),
                         43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875L)

        self.assertIn(comp.ask("What is the 1001 digit of the fibonacci sequence?"),
                      ("Thinking...", "One second", "cool your jets"))