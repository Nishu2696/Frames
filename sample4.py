from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak, Frame, Spacer
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, inch, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.doctemplate import Indenter

import os

doc = SimpleDocTemplate("simple_reportlab_rfi.pdf", pagesize=A4, rightMargin=0*mm,
                        leftMargin=0*mm,
                        topMargin=inch/4,
                        bottomMargin=inch/2,)

# reportlab_directory = os.path.dirname(Flask.__file__)
# font_folder = os.path.join(reportlab_directory, "lato")

# custom_font_folder_1 = os.path.join(font_folder, 'Lato-Black.ttf')
# custom_font_folder_2 = os.path.join(font_folder, 'Lato-Bold.ttf')

# custom_font_1 = TTFont('latoblack', custom_font_folder_1)
# custom_font_2 = TTFont('latobold', custom_font_folder_2)

pdfmetrics.registerFont(TTFont('lato_black', "../Flask/lato/Lato-Light.ttf"))
# latoblack = doc.setFont('latoblack')
pdfmetrics.registerFont(TTFont('lato_bold', "../Flask/lato/Lato-Bold.ttf"))
# latobold = doc.setFont('latobold')

data = {
    "code": "200",
    "message": "Success",
    "data": {
        "id": 24,
        "projectId": "-MIUapbi67wpiNCU6rEi",
        "createdAt": "2020-10-06T00:00:00Z",
        "priority": "Low",
        "costImpact": True,
        "scheduleImpact": True,
        "rfiTitle": "That above course green.",
        "resolvedByDate": "2020-11-04",
        "category": "missing details",
        "subCategory": "other",
        "rfiState": "completed",
        "totalQuestions": 4,
        "totalResponded": 3,
        "rfiSequence": 24,
        "conversation": False,
        "questions": [
            {
                "question": {
                    "id": 76,
                    "questionState": "draft",
                    "questionMsg": "Model free fast. Anyone want camera above.<br>Few worker care law next red piece voice. Wrong good Mr of present represent.<br>American you resource throughout. Couple skin nature hold something. Particular system at within send.<br>Thank appear window month night government win. White road budget. Imagine project play work individual imagine.<br>School news somebody almost buy. Local allow simple talk particularly. How reduce respond character.<br>Development total purpose message. Thank power role recent building group most.<br>Enter agency matter impact. Leave your want media beautiful language.<br>Project window strategy situation leader unit. Successful night job investment. Information high write couple.<br>Build receive spring pay throughout decade decade sort. Paper above represent between cost.<br>Note tree father point dream push seat partner. Effort remember listen identify debate imagine bank.<br>Maintain beyond stand possible our at. Network nor affect. He college school him station.",
                    "createdAt": "2020-10-06T00:00:00Z",
                    "rfiId": 24,
                    "attachments": []
                },
                "seqNumber": 1,
                "response": {
                    "id": 28,
                    "creatorId": "arsenicd6441",
                    "responseState": "draft",
                    "createdAt": "2020-10-19T15:59:31.038892Z",
                    "responseMsg": "Though significant sort take nice real fish. Action effect team Republican. Always whether notice mind her effort.<br>Oil need appear firm. Safe full executive thousand sometimes so.<br>Candidate possible theory section friend group picture. Various thank center safe race indeed. Question glass chance you deal experience.<br>Than practice and career across natural throw another. Become who image road spend ago set.<br>Research night economy bed simply. Mrs rather computer man. Nature the gas statement draw team every into.<br>Director practice start blue cause imagine. Outside I other write let power option. Might pay billion however sing agree.<br>Section share quality cold once available wide over.<br>Thank inside economy fish drug film majority your. Try hair approach great agreement. Word find notice point start.<br>Rich quality our page grow. Their friend leave in write. Might certain report focus care law. Indicate partner talk itself.<br>Glass act certain have if forget able. Them step character past.",
                    "rfiId": 24,
                    "questionId": 76,
                    "attachments": []
                }
            },
            {
                "question": {
                    "id": 75,
                    "questionState": "draft",
                    "questionMsg": "Son include behavior floor she. Be enjoy against.<br>Study movement find rule personal. Tend sing themselves.<br>Medical hope finish early cover those. Also network building.<br>Company civil discussion street expect than. None free response. Opportunity start father.<br>Specific country over long media. Citizen art Congress economy compare receive three.<br>When pay staff. Certain chance too run ability. Father either attorney break.<br>Media wife trip thus music top rock. Name try dinner Mrs voice view.<br>Street half stand fly final maybe. Blood even research into day build strong popular. Health international music. Mr he lay a everything foot as debate.<br>Seven heart experience let office need. Fill policy dream own probably. Community ask teach.<br>Deep condition large market. Test film top. Themselves research ready young rise teach another.<br>Address fish spend reality century shoulder cup. Rate herself generation action night party. Pull experience yeah notice per.",
                    "createdAt": "2020-10-06T00:00:00Z",
                    "rfiId": 24,
                    "attachments": []
                },
                "seqNumber": 2,
                "response": {
                    "id": 29,
                    "creatorId": "arsenicd6441",
                    "responseState": "draft",
                    "createdAt": "2020-10-19T15:59:31.076334Z",
                    "responseMsg": "Serve create writer Congress describe. Western couple check surface force hospital who what.<br>Story hot clear effort president. Clear treatment particular as clear still. Heavy try art vote.<br>Mind kind you carry war unit help. Debate indicate himself address.<br>Agency thought court. Develop police color lose him. Account it admit each deal.<br>Interest job party. Forget bar commercial.<br>Political ground live your not ask seem. Success avoid impact light money. Without another yes fall throughout those.<br>We close role Mr difficult necessary with.<br>Season where policy read true. Such else us nearly.<br>Street then require others beautiful its. Central floor parent very which drop over.<br>Yes heart fact. Remain involve issue father produce leader.<br>Manager can responsibility live. Foot get others production. Usually environment generation organization so treat.<br>Street draw agent market message Republican beautiful. All necessary top billion American experience. Really there line clearly question maybe.",
                    "rfiId": 24,
                    "questionId": 75,
                    "attachments": []
                }
            },
            {
                "question": {
                    "id": 74,
                    "questionState": "draft",
                    "questionMsg": "Red enough doctor my.<br>Road major sister science within according. Mean wrong foot maybe fast.<br>Measure attorney type most TV control scene. Play list nice. Meeting month season early prove our.<br>Hard wind development interesting. Especially job long near describe same well. Add improve think ball million air relationship.<br>Imagine again dog. Coach if serve morning true put culture. His our purpose get area bill customer.<br>Major religious enter able. Financial positive political same perform.<br>When see shake.<br>Tonight sometimes catch lose. Series stuff town. Before window miss five accept. Need present million decide military information cover.<br>Clear term raise fact. Candidate thank clear himself. Court rather sure surface college show kid final.<br>Majority occur name institution see something per employee. Apply budget woman wish morning appear back material.<br>Our Congress your. Play prove start wait item. Decade question sport car officer.",
                    "createdAt": "2020-10-06T00:00:00Z",
                    "rfiId": 24,
                    "attachments": []
                },
                "seqNumber": 3,
                "response": {
                    "id": 30,
                    "creatorId": "arsenicd6441",
                    "responseState": "draft",
                    "createdAt": "2020-10-19T15:59:31.105863Z",
                    "responseMsg": "Toward so can single box institution forget become. Society offer political make two close pick. Over surface mission second member support.<br>Participant pattern article when thought state explain lead.<br>North effort assume should could nature. Professional join have wear history natural. Statement cost meet generation himself.<br>Sea matter upon million. Bank task lot beautiful suggest too mother. Expect ten clear. Hour hard thousand age.<br>Film customer second those culture impact Mr. Car less administration reduce child certainly. Season especially size everything much two. Bit air draw base class citizen effect.<br>Carry month main project idea least. Girl per quickly.<br>Old night most look away whom.<br>Executive thus politics clear wide before direction. Growth computer figure success rock military. Stock after movie film say indeed.<br>Church discover local today doctor design. Fine enjoy three thing.<br>Democratic present life. Simply friend strategy suggest commercial word time story.",
                    "rfiId": 24,
                    "questionId": 74,
                    "attachments": []
                }
            },
            {
                "question": {
                    "id": 73,
                    "questionState": "draft",
                    "questionMsg": "Own set begin move. Follow set air board hundred.<br>Production bit keep their. Mrs organization almost.<br>Instead instead it consumer specific wait themselves three.<br>Local state try interesting sometimes economic free. Get open food pay past.<br>Agency responsibility one employee case design experience. Next spring gun matter cold walk.<br>Drug imagine mean beautiful. Both husband particularly require whose focus cultural. Card single whom care operation garden.<br>Important performance just American would phone she. Debate attorney have fact foreign no.<br>Rise wear easy education research visit mission outside.<br>Herself sign effort power. Imagine consumer large operation. Town agree skin decision huge business.<br>Until provide forward.<br>Onto east hand section quite. Run begin paper development tell response policy. Ball address their choose writer.<br>Ok executive meet language player piece. Seat me discover artist while how first. Goal choose market.",
                    "createdAt": "2020-10-06T00:00:00Z",
                    "rfiId": 24,
                    "attachments": []
                },
                "seqNumber": 4,
                "response": {
                    "id": 31,
                    "creatorId": "arsenicd6441",
                    "responseState": "draft",
                    "createdAt": "2020-10-19T15:59:31.150823Z",
                    "responseMsg": "Child partner charge east more eight risk. Billion increase avoid image pull yes our.<br>Name address movement case in example. Add reflect every.<br>Avoid future two bag evening raise behind. Investment past site least cause form attention. Crime even impact school consider.<br>Because either modern down church rock street. Allow interest page five garden.<br>Design central try mouth. Set again better product different else home cut. Strong hit start history assume reduce.<br>Explain hold admit people Mr shoulder. Own rate increase book. Enter job account bar situation.<br>Call military total between today economy. Claim concern Mrs surface continue call. Wait stand beyond understand degree personal still.<br>Language husband safe region. You catch drive performance year away.<br>Friend possible subject. Price when eye away rise cut usually hotel. General church effect more. Mean vote firm heart believe son statement.",
                    "rfiId": 24,
                    "questionId": 73,
                    "attachments": []
                }
            }
        ],
        "rfiPersona": [
            {
                "userId": "lithiumm6754",
                "companyId": "level1c8603",
                "userRole": "foreman",
                "userRfiRole": "rfiCreator"
            },
            {
                "userId": "carbonh3982",
                "companyId": "level1c8603",
                "userRole": "projectManager",
                "userRfiRole": "rfiCreator"
            },
            {
                "userId": "eriks9781",
                "companyId": "zenb9315",
                "userRole": "projectManager",
                "userRfiRole": "rfiManager"
            },
            {
                "userId": "iodinec7573",
                "companyId": "level2c4730",
                "userRole": "projectManager",
                "userRfiRole": "rfiReceiver"
            },
            {
                "userId": "arsenicd6441",
                "companyId": "level2c4730",
                "userRole": "Architect/Engineer",
                "userRfiRole": "rfiAssignee"
            }
        ],
        "userPersona": {
            "userId": "lithiumm6754",
            "companyId": "level1c8603",
            "userRole": "foreman",
            "userRfiRole": "rfiCreator"
        },
        "userRfiState": "completed"
    }
}

rfihistory = {
    "code": "200",
    "data": [
        {
            "id": 47,
            "createdAt": "2020-10-19T15:56:18.572377Z",
            "userId": "lithiumm6754",
            "userRfiState": "draft",
            "userRole": "foreman",
            "userRfiRole": "rfiCreator",
            "responding": False,
            "rfiId": 24
        },
        {
            "id": 48,
            "createdAt": "2020-10-19T15:56:18.578458Z",
            "userId": "carbonh3982",
            "userRfiState": "draft",
            "userRole": "projectManager",
            "userRfiRole": "rfiCreator",
            "responding": False,
            "rfiId": 24
        },
        {
            "id": 122,
            "createdAt": "2020-10-19T15:57:13.294070Z",
            "userId": "eriks9781",
            "userRfiState": "open",
            "userRole": "projectManager",
            "userRfiRole": "rfiManager",
            "responding": False,
            "rfiId": 24
        },
        {
            "id": 156,
            "createdAt": "2020-10-19T15:58:10.405750Z",
            "userId": "iodinec7573",
            "userRfiState": "open",
            "userRole": "projectManager",
            "userRfiRole": "rfiReceiver",
            "responding": False,
            "rfiId": 24
        },
        {
            "id": 183,
            "createdAt": "2020-10-19T15:58:57.540503Z",
            "userId": "arsenicd6441",
            "userRfiState": "open",
            "userRole": "Architect/Engineer",
            "userRfiRole": "rfiAssignee",
            "responding": False,
            "rfiId": 24
        },
        {
            "id": 205,
            "createdAt": "2020-10-19T15:59:32.125841Z",
            "userId": "iodinec7573",
            "userRfiState": "open",
            "userRole": "projectManager",
            "userRfiRole": "rfiReceiver",
            "responding": True,
            "rfiId": 24
        },
        {
            "id": 225,
            "createdAt": "2020-10-19T16:00:02.005153Z",
            "userId": "eriks9781",
            "userRfiState": "open",
            "userRole": "projectManager",
            "userRfiRole": "rfiManager",
            "responding": True,
            "rfiId": 24
        },
        {
            "id": 245,
            "createdAt": "2020-10-19T16:00:35.283345Z",
            "userId": "carbonh3982",
            "userRfiState": "completed",
            "userRole": "projectManager",
            "userRfiRole": "rfiCreator",
            "responding": True,
            "rfiId": 24
        }
    ]
}


elements = []

styles = getSampleStyleSheet()


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        # Change the position of this to wherever you want the page number to be
        self.drawRightString(85 * mm, 10*mm + (0.2 * inch),
                             "PDF Generated On: 27-10-2020 | 9.40 A.M")
        self.drawRightString(110 * mm, 10 * mm + (0.2 * inch),
                             "Page: %d/%d" % (self._pageNumber, page_count))
        self.drawRightString(153 * mm, 10 * mm + (0.2 * inch),
                             "Powered By")
        Linarc_logo = 'Linarc-Logo with text-blue-1-01.png'
        self.drawImage(Linarc_logo, 440, 35, width=130, height=50, mask='auto')
        # self.drawRightString(180 * mm, 10 * mm + (0.2 * inch), "Powered By <img src='Linarc-Logo with text-blue-1-01.png' width='100' height='35'/>")

style1 = ParagraphStyle(
    name="Normal",
    fontSize=15,
    alignment=TA_CENTER,
    leading=15,
    fontName= "lato_black",
)

style1a = ParagraphStyle(
    name="Normal",
    fontSize=15,
    alignment=TA_LEFT,
    fontName= "lato_black",
)

ts = [('LEFTPADDING', (0,0), (-1, -1), 15)]

text1_a = Paragraph('''<b>Project:OaK Dale</b>''', style=style1a)

project = data["data"]["projectId"].split("-")
projectId = "RFI Report: "+project[1]
print(projectId)
text1_b = Paragraph(projectId, style=style1)

colwidth = (215, 85, 270)
# text1_b = Paragraph('''<b>RFI Report  #CON1023</b>''', style=style1)
data1 = [[text1_a, "", text1_b]]
table1 = Table(data1, colwidth, style=ts,spaceAfter=10)
# table1 = Table(data1, spaceAfter=10)
table1.setStyle(TableStyle([('BOX', (-1, -1), (-1, -1), 1, colors.black),
                            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
                            ('TOPPADDING', (-1, -1), (-1, -1), 10),
                            ('LEFTPADDING', (-1, -1), (-1, -1), 5), ]))

elements.append(table1)

style2a = ParagraphStyle(
    name='Normal',
    fontSize=10,
    alignment=TA_LEFT,
    fontName= "lato_black",
)

style2 = ParagraphStyle(
    name="Normal",
    fontName= "lato_black",
    fontSize=10,
    alignment=TA_LEFT,
)
text2_a = Paragraph('''<b>Request By</b>''', style=style2a)
text2_b = Paragraph("Allen Construction", style=style2)

# data2 = [[text2_a, text2_b, "", ""]]

data2_a = [[text2_a, text2_b]]
table2_a = Table(data2_a)

data2 = [[table2_a, ""]]

table2 = Table(data2, style=ts,spaceAfter=10)

elements.append(table2)

category = data["data"]["category"]
subtype = data["data"]["subCategory"]
priority = data["data"]["priority"]
duedate = data["data"]["resolvedByDate"]
cost = data["data"]["costImpact"]
schedule = data["data"]["scheduleImpact"]
date = data["data"]["createdAt"].split("T")
date_no = date[0]
print(date_no)

text3_a = Paragraph('''<b>Type</b>''', style=style2a)
# text3a = text3_a + category

text3_b = Paragraph('''<b>Subtype</b>''', style=style2a)
# text3b = text3_b + subtype

text3_c = Paragraph('''<b>Priority</b>''', style=style2a)
# text3c = text3_c + priority

text3_d = Paragraph('''<b>Open date</b>''', style=style2a)
# text3d = text3_d + date_no

text3_d = Paragraph('''<b>Due date</b>''', style=style2a)
# text3d = text3_d + duedate

text3_e = Paragraph('''<b>Location</b>''', style=style2a)
# text3e = text3_e + "First Floor"

text3_f = Paragraph('''<b>Reference</b>''', style=style2a)
# text3f = text3_f + "Concrete"

text3_g = Paragraph('''<b>Cost Impact</b>''', style=style2a)
# text3g = text3_g + cost

text3_h = Paragraph('''<b>Schdule Impact</b>''', style=style2a)
# text3h = text3_h + schedule

data3_a = [[text3_a], [text3_b], [text3_c], [text3_d], [text3_e]]
table3_a = Table(data3_a,  style=ts)

data3_b = [[category], [subtype], [priority], [date_no], [duedate]]
table3_b = Table(data3_b)

data3_c = [[text3_e], [text3_f], [text3_g], [text3_h], [""]]
table3_c = Table(data3_c)

data3_d = [["First Floor"], ["Concrete"], ["-"], ["-"], [""]]
table3_d = Table(data3_d)

data3 = [[table3_a, table3_b, table3_c, table3_d]]
table3 = Table(data3)

table3.setStyle(TableStyle([
    # ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ('LINEABOVE', (0, 0), (-1, -1), 1, colors.black),
    ('LINEBELOW', (0, -1), (-1, -1), 1, colors.black),
    ('LINEBEFORE', (2, 0), (2, -1), 1, colors.black)
]))

elements.append(table3)

text4_a = Paragraph('''<b>Response by</b>''', style=style2a)
text4_b = Paragraph('''<b>Response date</b>''', style=style2a)

data4_a = [[text4_a], [text4_b]]
table4_a = Table(data4_a)

data4_b = [["Bob's Builders"], ["24-10-2020"]]
table4_b = Table(data4_b)

data4 = [[table4_a, table4_b, "", ""]]
table4 = Table(data4, style=ts)

table4.setStyle(TableStyle([('BOTTOMPADDING', (0, 0), (-1, -1), 10),
                            ('LINEBELOW', (0, -1), (-1, -1), 1, colors.black),
                            # ('BOX', (0, 0), (-1, -1), 1, colors.black)
                            ]))
elements.append(table4)

style5 = ParagraphStyle(
    name="Normal",
    fontSize=12,
    fontName= "lato_black",
    firstLineIndent=10,
    alignment=TA_JUSTIFY,
    # fontName = Helvetica,
)

style6 = ParagraphStyle(
    name="Normal",
    firstLineIndent=10,
    alignment=TA_JUSTIFY,
    fontSize=12,
    fontName= "lato_black",
    # fontName = Helvetica,
)

style5a = ParagraphStyle(
    name="Normal",
    spaceAfter=5,
    spaceBefore=5,
    fontSize=12,
    fontName= "lato_black",
)

# ts1 = [('LEFTMARGIN', (0,0), (-1, -1), 15)]

elements.append(Indenter(left=15, right=15))

questions = data["data"]["questions"]
count = 1
for a in questions:
    # rfi = []
    print(a)
    texta = Paragraph('''<b>Question{}:</b>'''.format(count), style=style5a)
    # qu = str(texta1)+str(count)+":"
    # texta = Paragraph(texta1, style=styles["Normal"])
    # elements.append(texta)
    question_date = a["question"]["createdAt"].split("T")
    questiondate = question_date[0]
    textb = Paragraph(questiondate, style=styles["Normal"])
    # elements.append(textb)
    question_msg = a["question"]["questionMsg"]
    questionmsg = question_msg.split("<br>")
    question = ","
    question = question.join(questionmsg)
    textc = Paragraph(question, style=style5)
    # elements.append(textc)

    data_a = [[[texta, textc]]]
    table_a = Table(data_a)

    # rfi.append(question)
    # rfi.append(questiondate)

    textd = Paragraph('''<b>Answer{}:</b>'''.format(count), style=style5a)
    # an = "Answer"+str(count)+":"
    # textd = Paragraph(an, style=styles["Normal"])
    # elements.append(textd)
    answer_date = a["response"]["createdAt"].split("T")
    answerdate = answer_date[0]
    texte = Paragraph(answerdate, style=styles["Normal"])
    # elements.append(texte)
    answer_reply = a["response"]["responseMsg"]
    answerreply = answer_reply.split("<br>")
    answer = ","
    answer = answer.join(answerreply)
    textf = Paragraph(answer, style=style6)
    # elements.append(textf)

    data_b = [[[textd, textf]]]
    table_b = Table(data_b, spaceAfter=5)

    data_c = [[table_a], [table_b]]
    table_c = Table(data_c,spaceBefore=10)

    table_c.setStyle(TableStyle([
        # ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('GRID', (0, 2), (-1, -1), 1, colors.black)
        # ('LINEBELOW', (0, -1), (-1, -1), 1, colors.black)
    ]))

    elements.append(table_c)

    # rfi.append(answer)
    # rfi.append(answerdate)
    # rfidata.append(rfi)

    count = count+1

elements.append(PageBreak())

text5_a = Paragraph('''<b>USER_ID</b>''', style=style2a)
text5_b = Paragraph('''<b>RECEIVED-AT</b>''', style=style2a)
text5_c = Paragraph('''<b>RESOLVED-AT</b>''', style=style2a)

data13 = [[text5_a, text5_b, text5_c]]

history = rfihistory["data"]
i = 0
for a in history:
    print(a)
    created_at = a["createdAt"].split("T")
    created_time = created_at[1].split(".")
    resolveddate = created_at[0]+" | "+created_time[0]
    text13_a = Paragraph(resolveddate, style=style2)
    # text13_h = Paragraph(created_time[0], style=style2)
    user_id = a["userId"]
    text13_b = Paragraph(user_id, style=style2)
    # user_role = a["userRole"]
    # text13_c = Paragraph(user_role, style=style2)
    # user_rfi_role = a["userRfiRole"]
    # text13_d = Paragraph(user_rfi_role, style=style2)
    # responding = str(a["responding"])
    # text13_e = Paragraph(responding, style=style2)
    if(i != len(history)-1):
        # j =i+1
        resolved_at = rfihistory["data"][i+1]["createdAt"].split("T")
        resolved_time = resolved_at[1].split(".")
        resolvedat = resolved_at[0]+" | "+resolved_time[0]
        # resolved_at = rfihistory["data"][j]
        print(resolved_at[0])
        text13_f = Paragraph(resolvedat, style=style2)
        # text13_g = Paragraph(resolved_time[0], style=style2)
        data13_a = [text13_b, text13_a, text13_f]
    else:
        resolved_at = "NILL"
        print(resolved_at)
        text13_f = Paragraph(resolved_at, style=style2)
        data13_a = [text13_b, text13_a, text13_f]

    data13.append(data13_a)

    i = i+1

colwidths = (235, 150, 150)

table13 = Table(data13, colwidths,  style=ts,spaceBefore=10)


table13.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 1, colors.black),
                             ('GRID', (0, 0), (-1, -1), 1, colors.black),
                             ('BOTTOMPADDING', (0, 0), (-1, -1), 20),
                             ('TOPPADDING', (0, 0), (-1, -1), 15)]))

elements.append(table13)

# doc.build(elements, onFirstPage=PageNumCanvas, onLaterPages=PageNumCanvas)
# doc.build(elements, onFirstPage=NumberedCanvas, onLaterPages=NumberedCanvas)
doc.build(elements, canvasmaker=NumberedCanvas)
