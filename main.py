from ediel_parser.lib.EDIParser import EDIParser
import json


data = "UNA:+.? 'UNB+UNOC:3+91100:ZZ:PRODAT+92135:ZZ:PRODAT+230515:2100+E230515804727++23-DDQ-PRODAT++1'UNH+1+PRODAT:D:97A:UN:E2SE5B'BGM+Z04+E230515804728+9+AB'DTM+137:202305152000:203'DTM+ZZZ:1:805'NAD+FR+91100:160:SVK+++++++SE'NAD+DO+92135:160:SVK+++++++SE'LIN+1++735999888000000192:::9'DTM+92:202306100000:203'DTM+354:60:806'QTY+31:5000:KWH'CCI++Z02'CAV+:::1'CCI++Z07'CAV+Z12'CCI++Z04'CAV+Z02'CCI++Z12'CAV+:::D'CCI++Z16'CAV+:::901'CCI++Z15'CAV+Z32'CCI++Z05'CAV+:::5'CCI++Z14'CAV+:::L641'CCI++Z13'CAV+Z70'RFF+MG:M10190'RFF+Z05:TES'RFF+Z07:735999888000000147'RFF+LI:E230515804729'NAD+Z02+11400:160:SVK'NAD+UD+193001017072:SE2:260++Harald HÂrfager+ƒlvsjˆv‰gen 44+STOCKHOLM++11820+SE'NAD+IT+735999888000000192::9+++ƒlvsjˆv‰gen 44+STOCKHOLM++11820+SE'UNT+36+1'UNZ+1+E230515804727'"

parser = EDIParser(payload=data, format="edi",
                   our_ediel="92135", our_city="STOCKHOLM")

res = parser.toDict()

# print(res)

data_1 = json.dumps(res)
# print(data_1)
parser_1 = EDIParser(payload=data_1, format="json",
                     our_ediel="92135", our_city="STOCKHOLM")

res_1 = parser_1.toEdi()

print(res)
