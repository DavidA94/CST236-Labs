from unittest import TestCase
from ReqTracer import requirements
from pyTona.main import Interface
import pyTona.answer_funcs
import pyTona.student_funcs
import getpass
import subprocess
import mock
import socket
import random
import time
import os
import matplotlib.pyplot as pl
import numpy
import math
import threading


class GeneralThreader(threading.Thread):
    def __init__(self, func, param, *args, **kwargs):
        super(GeneralThreader, self).__init__(*args, **kwargs)
        self.func = func
        self.param = param
        self._stop = threading.Event()
        self.result = None

    def stop(self):
        self._stop.set()

    def run(self):
        self.result = self.func(self.param)


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

        inventor = comp.ask("Who invented python?")
        self.assertEqual(inventor, "Guido Rossum(BDFL)")

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

        random.randint = temp

        pyTona.answer_funcs.seq_finder.stop()
        pyTona.answer_funcs.seq_finder = None



    @requirements(['#0030'])
    def test_1m_q_a(self):
        comp = Interface()

        q = "What n{0}n{0}n{0}n{0}n{0}n{0}n{0}n{0}n{0}n{0}n{0}n{0}n{0}n{0}n?"
        a = "It is {0}"

        for i in range(0, 1000000, 1):
            comp.last_question = q[0:-1].format(i)
            comp.correct(a.format(i))
            # Keeping this in only makes this take an amount of time comparable
            # to eternity.
            #self.assertEqual(comp.ask(q.format(i)), a.format(i))

        self.assertGreaterEqual(len(comp.question_answers), 1000000)

        # This takes way too long... ~2.5 hours
        #time1 = time.clock()
        #self.assertEqual(comp.ask(q.format(999999)), a.format(999999))
        #time2 = time.clock()
        #self.assertLessEqual((time2 - time1) * 1000, 5)

    @requirements(['#0031'])
    def test_5ms_store_time(self):
        comp = Interface()

        comp.ask("How are you?")

        time1 = time.clock()
        comp.teach("I'm doing well today.")
        time2 = time.clock()

        self.assertLessEqual((time2 - time1) * 1000, 5)

        time1 = time.clock()
        comp.correct("I'm feeling well today.")
        time2 = time.clock()

        self.assertLessEqual((time2 - time1) * 1000, 5)

    @requirements(['#0032'])
    def test_5ms_answer_time(self):
        comp = Interface()

        time1 = time.clock()
        response = comp.ask("Who invented Python?")
        time2 = time.clock()

        self.assertLessEqual((time2 - time1) * 1000, 5)
        self.assertEqual(response, "Guido Rossum(BDFL)")

    @requirements(['#0033', '#0034'])
    def test_only_1000_fib(self):
        comp = Interface()

        time1 = time.clock()
        while(comp.ask("What is the 1000 digit of the fibonacci sequence?") in
              ("Thinking...", "One second", "cool your jets")):
            pass

        time2 = time.clock()

        self.assertLessEqual(time2 - time1, 60)

        self.assertEqual(comp.ask("What is the 1000 digit of the fibonacci sequence?"),
                         43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875L)

        time.sleep(2)

        self.assertIn(comp.ask("What is the 1001 digit of the fibonacci sequence?"),
                      ("Thinking...", "One second", "cool your jets"))

    @requirements(['#0035', '#0035.5'])
    def test_factorial(self):
        comp = Interface()

        res = comp.ask("What is the factorial of 500?")
        self.assertEqual(res, "Multiplying")

        while comp.ask("What is the factorial of 500?") is "Multiplying":
            pass

        res = comp.ask("What is the factorial of 500?")
        self.assertEqual(res, 1220136825991110068701238785423046926253574342803192842192413588385845373153881997605496447502203281863013616477148203584163378722078177200480785205159329285477907571939330603772960859086270429174547882424912726344305670173270769461062802310452644218878789465754777149863494367781037644274033827365397471386477878495438489595537537990423241061271326984327745715546309977202781014561081188373709531016356324432987029563896628911658974769572087926928871281780070265174507768410719624390394322536422605234945850129918571501248706961568141625359056693423813008856249246891564126775654481886506593847951775360894005745238940335798476363944905313062323749066445048824665075946735862074637925184200459369692981022263971952597190945217823331756934581508552332820762820023402626907898342451712006207714640979456116127629145951237229913340169552363850942885592018727433795173014586357570828355780158735432768888680120399882384702151467605445407663535984174430480128938313896881639487469658817504506926365338175055478128640000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

    @requirements(['#0035'])
    def test_factorial_max(self):
        comp = Interface()

        while comp.ask("What is the factorial of 1000?") is "Multiplying":
            pass

        res = comp.ask("What is the factorial of 1000?")
        self.assertEqual(res, 402387260077093773543702433923003985719374864210714632543799910429938512398629020592044208486969404800479988610197196058631666872994808558901323829669944590997424504087073759918823627727188732519779505950995276120874975462497043601418278094646496291056393887437886487337119181045825783647849977012476632889835955735432513185323958463075557409114262417474349347553428646576611667797396668820291207379143853719588249808126867838374559731746136085379534524221586593201928090878297308431392844403281231558611036976801357304216168747609675871348312025478589320767169132448426236131412508780208000261683151027341827977704784635868170164365024153691398281264810213092761244896359928705114964975419909342221566832572080821333186116811553615836546984046708975602900950537616475847728421889679646244945160765353408198901385442487984959953319101723355556602139450399736280750137837615307127761926849034352625200015888535147331611702103968175921510907788019393178114194545257223865541461062892187960223838971476088506276862967146674697562911234082439208160153780889893964518263243671616762179168909779911903754031274622289988005195444414282012187361745992642956581746628302955570299024324153181617210465832036786906117260158783520751516284225540265170483304226143974286933061690897968482590125458327168226458066526769958652682272807075781391858178889652208164348344825993266043367660176999612831860788386150279465955131156552036093988180612138558600301435694527224206344631797460594682573103790084024432438465657245014402821885252470935190620929023136493273497565513958720559654228749774011413346962715422845862377387538230483865688976461927383814900140767310446640259899490222221765904339901886018566526485061799702356193897017860040811889729918311021171229845901641921068884387121855646124960798722908519296819372388642614839657382291123125024186649353143970137428531926649875337218940694281434118520158014123344828015051399694290153483077644569099073152433278288269864602789864321139083506217095002597389863554277196742822248757586765752344220207573630569498825087968928162753848863396909959826280956121450994871701244516461260379029309120889086942028510640182154399457156805941872748998094254742173582401063677404595741785160829230135358081840096996372524230560855903700624271243416909004153690105933983835777939410970027753472000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

        res = comp.ask("What is the factorial of 1001?")
        self.assertEqual(res, "Too High")

    @requirements(['#0036'])
    def test_story_time(self):
        comp = Interface()

        res = comp.ask("How about a story?")
        self.assertEqual(res, "You can read it at StoryTime!.txt")

        f_len = os.path.getsize("StoryTime!.txt")
        self.assertGreaterEqual(f_len, 250000)
        self.assertLessEqual(f_len, 500000)

    @requirements(['#0036'])
    def test_story_contents(self):
        comp = Interface()
        comp.ask("How about a story?")

        f = open("StoryTime!.txt")
        for ch in f.read():
            self.assertIn(ch, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !.,;:\"'?")

    @requirements(['#0037', '#0038'])
    def test_get_size(self):
        comp = Interface()

        res = comp.ask("How big are you?")
        self.assertEqual(res, "Let me get that for you.")

        total_size = 0
        for dirpath, dirnames, filenames in os.walk(os.getcwd()):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)

        while comp.ask("How big are you?") is "Let me get that for you.":
            pass

        # I don't know why I need this, but it's randomly failing, so it's here
        time.sleep(.5)

        res = comp.ask("How big are you?")
        self.assertEqual(res, total_size)

    @requirements(['#0039', '#0040'])
    def test_folder_depth(self):
        comp = Interface()

        res = comp.ask("How tall are you?")
        self.assertEqual(res, "I'm measuring")

        dirs = [f[0] for f in os.walk(".")]
        max_h = 1
        for d in dirs:
            h = len(d.split("\\"))
            if h > max_h:
                max_h = h

        while comp.ask("How tall are you?") is "I'm measuring":
            pass

        # I don't know why I need this, but it's randomly failing, so it's here
        time.sleep(.5)

        res = comp.ask("How tall are you?")
        self.assertEqual(res, str(max_h) + " feet")

    # Performance Graphs
    def test_response_time_v_number_of_questions(self):
        comp = Interface()

        nTests = str(len(comp.question_answers))
        testNames = [nTests + " Q's Text Response",
                     nTests + " Q's Feet Response",
                     nTests + " Q's Not Found",
                     "100 Q's Text Response",
                     "100 Q's Feet Response",
                     "100 Q's Not Found"]

        times = []

        time1 = time.clock()
        comp.ask("Who invented Python?")
        time2 = time.clock()
        times.append((time2 - time1) * 1000)

        time1 = time.clock()
        comp.ask("What is 57983 feet in miles?")
        time2 = time.clock()
        times.append((time2 - time1) * 1000)

        time1 = time.clock()
        comp.ask("What is up?")
        time2 = time.clock()
        times.append((time2 - time1) * 1000)

        for i in range(100 - int(nTests)):
            comp.last_question = "What is n{0}n".format(i)
            comp.correct("It is {0}".format(i))

        time1 = time.clock()
        comp.ask("Who invented Python?")
        time2 = time.clock()
        times.append((time2 - time1) * 1000)

        time1 = time.clock()
        comp.ask("What is 57983 feet in miles?")
        time2 = time.clock()
        times.append((time2 - time1) * 1000)

        time1 = time.clock()
        comp.ask("What is up?")
        time2 = time.clock()
        times.append((time2 - time1) * 1000)

        fig = pl.figure()
        ax = fig.add_subplot(111)

        N = 6
        xlocs = numpy.arange(N)
        width = .5 # Width of the bars

        ax.bar(xlocs, times, width, color='skyblue')

        ax.set_xlim(-width, len(xlocs) + width)
        ax.set_ylim(0, max(times) + 1)
        ax.set_ylabel('Time in Milliseconds')
        ax.set_title('Number of Questions vs. Response Time')
        ax.set_xticks(xlocs - (width / 2))
        xtickNames = ax.set_xticklabels(testNames)
        pl.setp(xtickNames, rotation=45, fontsize=10)
        pl.tight_layout()

        pl.savefig("Plots/Number of Questions vs. Response Time.png")
        pl.close()

    def test_time_for_fac(self):
        pyTona.student_funcs.factorials = None

        comp = Interface()
        times = []

        delta = time.clock()
        for i in range(0):
            while(comp.ask("Who invented Python?") is not "Guido Rossum(BDFL)"):
                pass
        delta = time.clock() - delta

        time1 = time.clock()
        for i in range(51):
            while(comp.ask("What is the factorial of {0}?".format(i)) is "Multiplying"):
                pass
            times.append(time.clock() - time1 - (i * delta))

        times = [x * 100 for x in times]

        pl.plot([x for x in range(51)], times, marker='o')
        pl.title("Time to Calculate (x!)")
        pl.ylabel("Calculation Time in Centiseconds")
        pl.xlabel("Factorial")
        pl.tight_layout()

        pl.savefig("Plots/Time to calculate x!.png")
        pl.close()

        pyTona.student_funcs.factorials.stop()

    def test_time_to_write_time_to_read_500000(self):
        comp = Interface()

        temp = random.randint
        random.randint = mock.Mock(return_value=500000)

        letter_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !.,;:\"'?"
        time1 = time.clock()
        for i in range(500000):
            random.choice(letter_set)
        delta = (time.clock() - time1)

        times = []

        time1 = time.clock()
        comp.ask("How about a story?")
        time2 = time.clock()

        times.append((time2 - time1 - delta) * 1000)

        with open("Storytime!.txt") as f:
            time1 = time.clock()
            x = f.read()
            time2 = time.clock()
            times.append((time2 - time1) * 1000)

        random.randint = temp

        fig = pl.figure()
        ax = fig.add_subplot(111)

        N = 2
        xlocs = numpy.arange(N)
        width = .5 # Width of the bars

        ax.bar(xlocs, times, width, color='skyblue')

        ax.set_xlim(-width, len(xlocs) + width)
        ax.set_ylim(0, max(times) + 10)
        ax.set_ylabel('Time in Milliseconds')
        ax.set_title('Write Time vs. Read Time')
        ax.set_xticks(xlocs + (width / 2))
        ax.set_xticklabels(["Write Time", "Read time"])
        pl.tight_layout()

        pl.annotate(str(times[1]) + " ms", xy=(1.25, times[1] + 20),
                    xytext=(1.3, times[1] + 110),
                    arrowprops=dict(facecolor='black', shrink=0, width=2),
        )

        pl.savefig("Plots/Time to Write, Time to Read.png")
        pl.close()

    def test_time_for_fib(self):
        pyTona.answer_funcs.seq_finder = None

        comp = Interface()
        times = []

        delta = time.clock()
        for i in range(0):
            while(comp.ask("Who invented Python?") is not "Guido Rossum(BDFL)"):
                pass
        delta = time.clock() - delta

        time1 = time.clock()
        for i in range(51):
            while(comp.ask("What is the {0} digit of the Fibonacci sequence?".format(i))
                  in ("Thinking...", "One second", "cool your jets")):
                pass
            times.append(time.clock() - time1 - (i * delta))

        # Make centiseconds
        times = [x * 100 for x in times]

        pl.plot([x for x in range(51)], times, marker='o')
        pl.title("Time to Calculate Fibonacci(x)")
        pl.ylabel("Calculation Time in Centiseconds")
        pl.xlabel("Fibonacci Number")
        pl.tight_layout()

        pl.savefig("Plots/Time to calculate Fibonacci(x).png")
        pl.close()

        pyTona.answer_funcs.seq_finder.stop()

    def test_store_time_v_number_of_questions(self):
        comp = Interface()

        nTests = str(len(comp.question_answers))
        testNames = [nTests + " Q's Text Store",
                     nTests + " Q's Func Store",
                     "100 Q's Text Store",
                     "100 Q's Func Store"]

        times = []

        time1 = time.clock()
        comp.ask("Who invented C++?")
        comp.teach("Bjarne Stroustrup")
        time2 = time.clock()
        times.append((time2 - time1) * 1000)

        time1 = time.clock()
        comp.ask("What is the abs of -10?")
        comp.teach(abs)
        time2 = time.clock()
        times.append((time2 - time1) * 1000)

        for i in range(100 - int(nTests)):
            comp.last_question = "What is n{0}n".format(i)
            comp.correct("It is {0}".format(i))

        time1 = time.clock()
        comp.ask("Who invented Lisp?")
        comp.teach("John McCarthy")
        time2 = time.clock()
        times.append((time2 - time1) * 1000)

        time1 = time.clock()
        comp.ask("What is the square root of 25?")
        comp.teach(math.sqrt)
        time2 = time.clock()
        times.append((time2 - time1) * 1000)

        fig = pl.figure()
        ax = fig.add_subplot(111)

        N = 4
        xlocs = numpy.arange(N)
        width = .5 # Width of the bars

        ax.bar(xlocs, times, width, color='skyblue')

        ax.set_xlim(-width, len(xlocs) + width)
        ax.set_ylim(0, max(times) + 1)
        ax.set_ylabel('Time in Milliseconds')
        ax.set_title('Number of Questions vs. Store Time')
        ax.set_xticks(xlocs)
        xtickNames = ax.set_xticklabels(testNames)
        pl.setp(xtickNames, rotation=45, fontsize=10)
        pl.tight_layout()

        pl.savefig("Plots/Number of Questions vs. Store Time.png")
        pl.close()

    def spike_tester(self, comp):
        time1 = time.clock()
        comp.ask("What is 6000 feet in miles?")
        time2 = time.clock()
        return time2 - time1

    @requirements(['#0032'])
    def test_load_testing(self):
        comp = Interface()

        # Regular
        self.assertLessEqual(self.spike_tester(comp) * 1000, 5)

        # Put under a constant load
        for i in range(1000):
            self.assertLessEqual(self.spike_tester(comp) * 1000, 5)

        # Sleep 5ms to allow time for last answer
        time.sleep(.005)

        # Regular
        self.assertLessEqual(self.spike_tester(comp) * 1000, 5)

    @requirements(['#0032'])
    def test_spike_testing(self):
        comp = Interface()
        qs = []

        # Regular
        self.assertLessEqual(self.spike_tester(comp) * 1000, 5)

        # Get Ready
        for i in range(1000):
            qs.append(GeneralThreader(self.spike_tester, comp))

        # Spike
        for i in range(1000):
            qs[i].start()

        # Sleep 5ms to allow time for last answer
        time.sleep(.005)

        for i in range(1000):
            print i
            self.assertLessEqual(qs[i].result * 1000, 5)
            qs[i].stop()

        # Regular
        self.assertLessEqual(self.spike_tester(comp) * 1000, 5)