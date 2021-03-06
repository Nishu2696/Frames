from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Frame, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter

fileName = '_linarcpdf1.pdf'

doc = SimpleDocTemplate(fileName, pagesize=letter)

pdf = canvas.Canvas("_linarcpdf.pdf")
# pdf.translate(cm, cm)
flow_obj = []

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

styles = getSampleStyleSheet()

# Row1
style1 = ParagraphStyle(
    name="Normal",
    alignment= TA_CENTER,
    fontSize=15,
)

text1 = Paragraph("Request For Information", style=style1)
# flow_obj1 = []
flow_obj.append(text1)
frame1 = Frame(280, 770, 250, 30, showBoundary=1)
frame1.addFromList(flow_obj, pdf)

# Row2
style2 = ParagraphStyle(
    name="Normal",
    fontSize=10,
)

project = data["data"]["projectId"].split("-")
projectId = "Project-Id: "+project[1]
print(projectId)
text2 = Paragraph(projectId, style=style2)
# flow_obj2 = []
flow_obj.append(text2)
frame2 = Frame(265, 740, 230, 30, showBoundary=0)
frame2.addFromList(flow_obj, pdf)

date = data["data"]["createdAt"].split("T")
date_no = "View Date: "+date[0]
print(date_no)
text3 = Paragraph(date_no, style=style2)
# flow_obj3 = []
flow_obj.append(text3)
frame3 = Frame(420, 740, 230, 30, showBoundary=0)
frame3.addFromList(flow_obj, pdf)

text4 = Paragraph("RFI No:", style=style2)
# flow_obj4 = []
flow_obj.append(text4)
frame4 = Frame(420, 690, 230, 30, showBoundary=0)
frame4.addFromList(flow_obj, pdf)

# left column
# flow_obj5 = []
frame5 = Frame(20, 490, 310, 150, showBoundary=1)
frame5.addFromList(flow_obj, pdf)

column1 = Paragraph("Primary Responder", style=style2)
flow_obj.append(column1)
frame5 = Frame(25, 610, 300, 30, showBoundary=0)
frame5.addFromList(flow_obj, pdf)

cc_persons = data["data"]["rfiPersona"]
cc = ["CC:"]
for x in cc_persons:
    cc.append(x["userId"])
print(cc)
separator = ' '
CC = separator.join(cc)
print(separator.join(cc))
column2 = Paragraph(CC, style=style2)
flow_obj.append(column2)
frame5 = Frame(25, 575, 300, 50, showBoundary=0)
frame5.addFromList(flow_obj, pdf)

column3 = Paragraph("From", style=style2)
flow_obj.append(column3)
frame5 = Frame(25, 560, 300, 30, showBoundary=0)
frame5.addFromList(flow_obj, pdf)

# RIGHT COLUMN
# flow_obj6 = []
frame6 = Frame(330, 490, 200, 150, showBoundary=1)
frame6.addFromList(flow_obj, pdf)

date_no_1 = "Date: "+date[0]
column1_right = Paragraph(date_no_1, style=style2)
flow_obj.append(column1_right)
frame6 = Frame(335, 610, 300, 30, showBoundary=0)
frame6.addFromList(flow_obj, pdf)

column1_right = Paragraph("Status", style=style2)
flow_obj.append(column1_right)
frame6 = Frame(335, 595, 300, 30, showBoundary=0)
frame6.addFromList(flow_obj, pdf)

column1_right = Paragraph("Resolved Date", style=style2)
flow_obj.append(column1_right)
frame6 = Frame(335, 580, 300, 30, showBoundary=0)
frame6.addFromList(flow_obj, pdf)

column1_right = Paragraph("Resolved for Request", style=style2)
flow_obj.append(column1_right)
frame6 = Frame(335, 565, 300, 30, showBoundary=0)
frame6.addFromList(flow_obj, pdf)

column1_right = Paragraph("Action Requested", style=style2)
flow_obj.append(column1_right)
frame6 = Frame(335, 550, 300, 30, showBoundary=0)
frame6.addFromList(flow_obj, pdf)

column1_right = Paragraph("Probable Cost Effect", style=style2)
flow_obj.append(column1_right)
frame6 = Frame(335, 535, 300, 30, showBoundary=0)
frame6.addFromList(flow_obj, pdf)

end_date = data["data"]["resolvedByDate"]
endDate = "Probable Time Effect: "+ end_date
print(endDate)
column1_right = Paragraph(endDate, style=style2)
flow_obj.append(column1_right)
frame6 = Frame(335, 520, 300, 30, showBoundary=0)
frame6.addFromList(flow_obj, pdf)

priority = data["data"]["priority"]
priority_status = "Priority: "+ priority
print(priority_status)
column1_right = Paragraph(priority_status, style=style2)
flow_obj.append(column1_right)
frame6 = Frame(335, 505, 300, 30, showBoundary=0)
frame6.addFromList(flow_obj, pdf)

due_response = data["data"]["totalQuestions"] - data["data"]["totalResponded"]
if(due_response == 0):
    due_response = "NONE"
    dueResponse = "Response Due: "+ due_response
else:
    due_response = str(due_response)
    dueResponse = "Reponse Due: "+ due_response
print(dueResponse)
column1_right = Paragraph(dueResponse, style=style2)
flow_obj.append(column1_right)
frame6 = Frame(335, 490, 300, 30, showBoundary=0)
frame6.addFromList(flow_obj, pdf)

# text7 = Paragraph("Subject:", style=style2)
# # flow_obj7 = []
# flow_obj.append(text7)
# frame7 = Frame(15, 460, 230, 30, showBoundary=0)
# frame7.addFromList(flow_obj, pdf)

# text8 = Paragraph("Drawing No:", style=style2)
# # flow_obj8 = []
# flow_obj.append(text8)
# frame8 = Frame(15, 445, 230, 30, showBoundary=0)
# frame8.addFromList(flow_obj, pdf)

# text9 = Paragraph("Detail No:", style=style2)
# # flow_obj9 = []
# flow_obj.append(text9)
# frame9 = Frame(200, 445, 230, 30, showBoundary=0)
# frame9.addFromList(flow_obj, pdf)

# text10 = Paragraph("CSI Code:", style=style2)
# # flow_obj10 = []
# flow_obj.append(text10)
# frame10 = Frame(15, 430, 230, 30, showBoundary=0)
# frame10.addFromList(flow_obj, pdf)

# text11 = Paragraph("Other Ref No:", style=style2)
# # flow_obj11 = []
# flow_obj.append(text11)
# frame11 = Frame(200, 430, 230, 30, showBoundary=0)
# frame11.addFromList(flow_obj, pdf)

# text12 = Paragraph("Building:", style=style2)
# # flow_obj12 = []
# flow_obj.append(text12)
# frame12 = Frame(15, 415, 230, 30, showBoundary=0)
# frame12.addFromList(flow_obj, pdf)

# text13 = Paragraph("Information Requested:", style=style2)
# # flow_obj13 = []
# flow_obj.append(text13)
# frame13 = Frame(15, 385, 230, 30, showBoundary=0)
# frame13.addFromList(flow_obj, pdf)

# text14 = Paragraph("Response Information:", style=style2)
# # flow_obj14 = []
# flow_obj.append(text14)
# frame14 = Frame(15, 355, 230, 30, showBoundary=0)
# frame14.addFromList(flow_obj, pdf)

style3 = ParagraphStyle(
    name="Normal",
    fontSize=10,
    alignment= TA_CENTER,
)

text15 = Paragraph("Responder", style=style3)
# flow_obj15 = []
flow_obj.append(text15)
frame15 = Frame(20, 460, 200, 25, showBoundary=1)
frame15.addFromList(flow_obj, pdf)
    
text16 = Paragraph("Date", style=style3)
# flow_obj16 = []
flow_obj.append(text16)
frame16 = Frame(220, 460, 110, 25, showBoundary=1)
frame16.addFromList(flow_obj, pdf)

text17 = Paragraph("Response", style=style3)
# flow_obj17 = []
flow_obj.append(text17)
frame17 = Frame(330, 460, 200, 25, showBoundary=1)
frame17.addFromList(flow_obj, pdf)

text20 = Paragraph("RFI QUESTION & RESPONSE", style=style2)
# flow_obj20 = []
flow_obj.append(text20)
frame20 = Frame(15, 350, 200, 25, showBoundary=0)
frame20.addFromList(flow_obj, pdf)

style5 = ParagraphStyle(
    name="Normal",
    firstLineIndent = 10,
    leading=15,
)
style6 = ParagraphStyle(
    name="Normal",
    firstLineIndent = 10,
    spaceAfter = 6,
    leading=15,
)

elements = []
questions = data["data"]["questions"]
count = 1
for a in questions:
    # rfi = []
    # print(a)
    qu = "Question"+str(count)+":"
    text1 = Paragraph(qu, style=styles["Normal"])
    elements.append(text1)
    question_date = a["question"]["createdAt"].split("T")
    questiondate = question_date[0]
    text3 = Paragraph(questiondate, style=styles["Normal"])
    elements.append(text3)
    question_msg = a["question"]["questionMsg"]
    questionmsg = question_msg.split("<br>")
    question = ","
    question = question.join(questionmsg)
    text2 = Paragraph(question, style=style5)
    elements.append(text2)
    # rfi.append(question)
    # rfi.append(questiondate)
    an = "Answer"+str(count)+":"
    text6 = Paragraph(an, style=styles["Normal"])
    elements.append(text6)
    answer_date = a["response"]["createdAt"].split("T")
    answerdate = answer_date[0]
    text5 = Paragraph(answerdate,style=styles["Normal"])
    elements.append(text5)
    answer_reply = a["response"]["responseMsg"]
    answerreply = answer_reply.split("<br>")
    answer = ","
    answer = answer.join(answerreply)
    text4 = Paragraph(answer,style=style6)
    elements.append(text4)
    # rfi.append(answer)
    # rfi.append(answerdate)
    # rfidata.append(rfi)
    count = count+1


# questions = data["data"]["questions"]
# for a in range(1):
#     print(a)
#     question_msg = data["data"]["questions"][a]["question"]["questionMsg"]
#     questionmsg = question_msg.split("<br>")
#     question = ","
#     question = question.join(questionmsg)
#     print(question)
#     # question_date = str(a["question"]["createdAt"].split("T"))
#     answer_reply = data["data"]["questions"][a]["response"]["responseMsg"]
#     answerreply = answer_reply.split("<br>")
#     answer = ","
#     answer = answer.join(answerreply)
#     # answer_date = str(a["response"]["createdAt"].split("T"))
#     print(answer)
#     text23 = Paragraph(question, style=style2)
#     flow_obj.append(text23)
#     frame23 = Frame(15,300,520,150, showBoundary=1)
#     frame23.addFromList(flow_obj, pdf)
#     text24 = Paragraph(answer, style=style2)
#     flow_obj.append(text24)
#     frame24 = Frame(15,140,520,130, showBoundary=1)
#     frame24.addFromList(flow_obj, pdf)

text18 = Paragraph("Disclaimer", style=style2)
# flow_obj18 = []
flow_obj.append(text18)
frame18 = Frame(15, 160, 200, 0, showBoundary=0)
frame18.addFromList(flow_obj, pdf)

# disclaimer = "The above information is in no way a directive to execute work contrary to the Contract Documnets. If the Contractor feels that the above noted REPLY to the RFI is in conflict with the Drawings/Specifications or other Contract Documents or not within the scope of his or her contractual obligations, DO NOT PROCEED and notify the CO/COTR immediately."
text19 = Paragraph("The above information is in no way a directive to execute work contrary to the Contract Documnets. If the Contractor feels that the above noted REPLY to the RFI is in conflict with the Drawings/Specifications or other Contract Documents or not within the scope of his or her contractual obligations, DO NOT PROCEED and notify the CO/COTR immediately.", style=style2)
# flow_obj19 = []
flow_obj.append(text19)
frame19 = Frame(15, 105, 520, 70, showBoundary=0)
frame19.addFromList(flow_obj, pdf)

para = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# Story.append(Paragraph(ptext, styles["Normal"]))
text22=Paragraph(para, style=styles["Normal"])
flow_obj.append(text22)

# pdf.build(flow_obj)
pdf.save()
doc.build(elements)