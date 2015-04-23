from nose2.events import Plugin
from tests.ReqTracer import Requirements

class ReqTraceOutput(Plugin):
    configSection = 'ReqTraceOutput'
    alwaysOn = True

    def afterSummaryReport(self, event):
        f = open("ReqTracingOutput.csv", 'w')
        f.write("Requirement ID,Requirement Description," +
                "Requirement Method 1,Requirement Method 2," +
                "Requirement Method 3,Requirement Method 4," +
                "Requirement Method 5,Requirement Method 6\n\n")

        for item in Requirements:
            f.write(item + ",")
            f.write('"' + Requirements[item].req_text.replace('"', '""').replace("\n", "") + '",')
            for func in Requirements[item].func_name:
                f.write(func + ",")

            f.write("\n")

        f.close()
