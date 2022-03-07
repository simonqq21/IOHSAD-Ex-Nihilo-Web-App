from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, SelectField, IntegerField, DateField, TimeField
from wtforms.fields import TelField, EmailField
from wtforms.validators import DataRequired, Email, InputRequired, Optional

PHRegions = [('R1', "Region 1 (Ilocos Region)"),
            ('R2', "Region 2 (Cagayan Valley)"),
            ('R3', "Region 3 (Central Luzon)"),
            ('R4A', "Region 4A (CALABARZON)"),
            ('R4B', "Region 4B (MIMAROPA)"),
            ('R5', "Region 5 (Bicol Region)"),
            ('R6', "Region 6 (Western Visayas)"),
            ('R7', "Region 7 (Central Visayas)"),
            ('R8', "Region 8 (Eastern Visayas)"),
            ('R9', "Region 9 (Zamboanga Peninsula)"),
            ('R10', "Region 10 (Northern Mindanao)"),
            ('R11', "Region 11 (Davao Region)"),
            ('R12', "Region 12 (SOCCSKSARGEN)"),
            ('R13', "Region 13 (Caraga Region)"),
            ('ARMM', "ARMM (Autonomous Region in Muslim Mindanao)"),
            ('CAR', "CAR (Cordillera Administrative Region)"),
            ('NCR', "NCR (National Capital Region)")]

hoursPerDayOptions = [('1-4', "1-4 oras"),
            ('4-6', "4-6 oras"),
            ('6-8', "6-8 oras"),
            ('8++', "higit sa 8 oras")]

caseCountOptions = [('1-10', "1-10 kaso"),
            ('10-50', "10-50 kaso"),
            ('50-100', "50-100 kaso"),
            ('>100', "mas marami pa sa 100 na kaso")]
'''
Accidental Injury Form
-Name of Company
-Presence of union (If yes, put down the contact details of the head of the union (contact number and email)
-Contact Details of the one who submitted the form

then finally a large textbox for the nature of the complaint
'''
class AccidentalInjuryForm(FlaskForm):
    username = StringField("Unique Username*", validators=[DataRequired(), InputRequired()])
    companyName = StringField("Company Name* (Pangalan ng kumpanya)*", validators=[DataRequired(), InputRequired()])
    unionPresence = BooleanField("Union Present* (Mayroon bang unyon ng mga manggagawa?)*")
    unionHeadContactNo = TelField("Union Head Contact No. (Telepono ng pinuno ng unyon ng mga manggagawa)", validators=[Optional()])
    unionHeadEmail = EmailField("Union Head Email Address (Email address ng pinuno ng unyon ng mga manggagawa)", validators=[Email(), Optional()])
    contactNumber = StringField("Contact No. (Telepono)*", validators=[DataRequired(), InputRequired()])
    complaint = TextAreaField("Enter your complaint here regarding the accident that resulted in an injury* \
        (I-type ang inyong reklamo dito ukol sa aksidenteng nagresulta sa pagkasugat*)", validators=[DataRequired(), InputRequired()])
    submit = SubmitField("Submit Form (Ipasa ang form)")

'''
Accidental Death Form
-Name of Company
-Presence of union (If yes, put down the contact details of the head of the union (contact number and email)
-Contact Details of the one who submitted the form

then finally a large textbox for the nature of the complaint
'''
class AccidentalDeathForm(FlaskForm):
    username = StringField("Unique Username*", validators=[DataRequired(), InputRequired()])
    companyName = StringField("Company Name* (Pangalan ng kumpanya)*", validators=[DataRequired(), InputRequired()])
    unionPresence = BooleanField("Union Present* (Mayroon bang unyon ng mga manggagawa?)*")
    unionHeadContactNo = TelField("Union Head Contact No. (Telepono ng pinuno ng unyon ng mga manggagawa)", validators=[Optional()])
    unionHeadEmail = EmailField("Union Head Email Address (Email address ng pinuno ng unyon ng mga manggagawa)", validators=[Email(), Optional()])
    contactNumber = StringField("Contact No. (Telepono)*", validators=[DataRequired(), InputRequired()])
    complaint = TextAreaField("Enter your complaint here regarding the accident that resulted in death* \
        (I-type ang inyong reklamo dito ukol sa aksidenteng nagresulta sa kamatayan*)", validators=[DataRequired(), InputRequired()])
    submit = SubmitField("Submit Form (Ipasa ang form)")

'''
OSH Violation Form
-Name of Company
-Presence of union (If yes, put down the contact details of the head of the union (contact number and email)
-Contact Details of the one who submitted the form

then finally a large textbox for the nature of the complaint
'''
class OSHViolationForm(FlaskForm):
    username = StringField("Unique Username*", validators=[DataRequired(), InputRequired()])
    companyName = StringField("Company Name* (Pangalan ng kumpanya)*", validators=[DataRequired(), InputRequired()])
    unionPresence = BooleanField("Union Present* (Mayroon bang unyon ng mga manggagawa?)*")
    unionHeadContactNo = TelField("Union Head Contact No. (Telepono ng pinuno ng unyon ng mga manggagawa)", validators=[Optional()])
    unionHeadEmail = EmailField("Union Head Email Address (Email address ng pinuno ng unyon ng mga manggagawa)", validators=[Email(), Optional()])
    contactNumber = StringField("Contact No. (Telepono)*", validators=[DataRequired(), InputRequired()])
    complaint = TextAreaField("Enter your complaint here regarding the occupational safety and health violation* \
        (I-type ang inyong reklamo dito ukol sa paglabag sa mga pangkalusugang at pangkaligtasang aspeto ng trabaho*)", validators=[DataRequired(), InputRequired()])
    submit = SubmitField("Submit Form (Ipasa ang form)")

'''
Non Compensation Form
-Name of Company
-Presence of union (If yes, put down the contact details of the head of the union (contact number and email)
-Contact Details of the one who submitted the form

then finally a large textbox for the nature of the complaint
'''
class NonCompensationForm(FlaskForm):
    username = StringField("Unique Username*", validators=[DataRequired(), InputRequired()])
    companyName = StringField("Company Name* (Pangalan ng kumpanya)*", validators=[DataRequired(), InputRequired()])
    unionPresence = BooleanField("Union Present* (Mayroon bang unyon ng mga manggagawa?)*")
    unionHeadContactNo = TelField("Union Head Contact No. (Telepono ng pinuno ng unyon ng mga manggagawa)", validators=[Optional()])
    unionHeadEmail = EmailField("Union Head Email Address (Email address ng pinuno ng unyon ng mga manggagawa)", validators=[Email(), Optional()])
    contactNumber = StringField("Contact No. (Telepono)*", validators=[DataRequired(), InputRequired()])
    complaint = TextAreaField("Enter your complaint here about non-compensation* \
        (I-type ang inyong reklamo dito ukol sa hindi pag-kompensado*)", validators=[DataRequired(), InputRequired()])
    submit = SubmitField("Submit Form (Ipasa ang form)")

'''
Administrator login form
- email or username
- password
'''
class AdminLoginForm(FlaskForm):
    emailusername = StringField("Email or username:", validators=[DataRequired(), InputRequired()])
    password = PasswordField("Password:", validators=[DataRequired(), InputRequired()])
    remember_me = BooleanField("Remember Me")
    login = SubmitField("Login")

'''
COVID-19 Health Protocol Assessment Form
 Are you experiencing (Nakakaranas ka ba ng):
 fever (lagnat), cough and/or colds (ubo at/o sipon), body pains (pananakit ng katawan), sore throat (pananakit ng lalamunan/masakit lumunok)
Have you had face-to-face contact with a probable or confirmed COVID-19 case within \
    1 meter and for more than 15 minutes for the past 14 days? (May nakasalamuha ka \
    ba na probable o kumpirmadong pasyente na may COVID-19 mula sa isang metrong \
    distansya o mas malapit pa at tumagal ng mahigit 15 minuto sa nakalipas na 14 araw)?
Have you provided direct care for a patient with probable or confirmed COVID-19 \
    case without using proper personal protective equipment for the past 14 days? \
    (Nag-alaga ka ba ng probable o kumpirmadong pasyente na may COVID-19 nang hindi \
    nakasuot ng tamang personal protective equipment sa nakalipas na 14 araw?)
Have you travelled outside the Philippines in the last 14 days (Ikaw ba ay \
    nagbiyahe sa labas ng Pilipinas sa nakalipas na 14 na araw)?
Have you travelled outside the current city/municipality where you reside (Ikaw \
    ba ay nagbyahe sa labas ng iyong lungsod/munisipyo)? If yes, specify which \
    city/municipality you went to (Sabihin kung saan).

'''
class COVID19Survey(FlaskForm):
    username = StringField("Pangalan*", validators=[DataRequired(), InputRequired()])
    contactNumber = TelField("Contact Number*", validators=[DataRequired(), InputRequired()])
    fullname = StringField("Full name (Kumpletong pangngalan) (Last, Given, Middle)*", validators=[DataRequired(), InputRequired()])
    shiftdate = DateField("Shift Date (Datos ng shift):*", validators=[DataRequired(), InputRequired()])
    shifttime = TimeField("SHift Time (Oras ng Shift):*", validators=[DataRequired(), InputRequired()])
    symptoms = "Are you experiencing (Nakakaranas ka ba ng):"
    fever = BooleanField("fever (lagnat)")
    coughcolds = BooleanField("cough and/or colds (ubo at/o sipon)")
    bodypain = BooleanField("body pains (pananakit ng katawan)")
    sorethroat = BooleanField("sore throat (pananakit ng lalamunan/masakit lumunok)")
    contact = BooleanField("Have you had face-to-face contact with a probable or \
        confirmed COVID-19 case within 1 meter and for more than 15 minutes for the \
        past 14 days? (May nakasalamuha ka ba na probable o kumpirmadong pasyente na \
        may COVID-19 mula sa isang metrong distansya o mas malapit pa at tumagal ng \
        mahigit 15 minuto sa nakalipas na 14 araw)?")
    directcare = BooleanField("Have you provided direct care for a patient with probable or confirmed COVID-19 \
        case without using proper personal protective equipment for the past 14 days? \
        (Nag-alaga ka ba ng probable o kumpirmadong pasyente na may COVID-19 nang hindi \
        nakasuot ng tamang personal protective equipment sa nakalipas na 14 araw?)")
    internationalTravel = BooleanField("Have you travelled outside the Philippines in the last 14 days (Ikaw ba ay \
        nagbiyahe sa labas ng Pilipinas sa nakalipas na 14 na araw)?")
    domesticTravel = BooleanField("Have you travelled outside the current city/municipality where you reside (Ikaw \
        ba ay nagbyahe sa labas ng iyong lungsod/munisipyo)? If yes, specify which \
        city/municipality you went to (Sabihin kung saan).")
    complaint = TextAreaField("Enter your complaint here about COVID-19 protocols* \
        (I-type ang inyong reklamo dito ukol sa mga protocol ukol sa COVID-19*)", validators=[])
    submit = SubmitField("Submit Form (Ipasa ang form)")

    # username = StringField("Pangalan*", validators=[DataRequired(), InputRequired()])
    # contactNumber = TelField("Contact Number*", validators=[DataRequired(), InputRequired()])
    # email = EmailField("E-mail address*", validators=[DataRequired(), InputRequired()])
    # companyName = StringField("Pangalan ng Kumpanya*", validators=[DataRequired(), InputRequired()])
    # companyLocation = SelectField("Lokasyon ng Kumpanya*", choices=PHRegions, validators=[DataRequired(), InputRequired()])
    # freeMassTesting = BooleanField("Nagsagawa ba ng free mass testing ang kumpanya sa hanay ng mga manggagawa?*", validators=[])
    # freeMassTestingDetails = StringField("Kung oo, paano tinukoy ang mga dapat sumailalim sa test? Anong klaseng test \
    #     (rapid antibody test o rt-PCR/swab test) at saan ito isinagawa?")
    # dailyHealthMonitoring = BooleanField("Nagsasagawa ba ang kumpanya ng daily health monitoring tulad ng pag-check ng \
    #     body temperature at pagpapasagot ng daily health questionnaire sa mga manggagawa \
    #     bago pumasok sa loob ng lugar-paggawa*?", validators=[])
    # distancing = BooleanField("Naipatutupad ba ang physical at social distancing sa iba’t ibang erya ng \
    #     lugar-paggawa – production area, canteen, pantry, office, locker area, exit and \
    #     entrance, at iba pa?*", validators=[])
    # distancingHardToImplementArea = StringField("Saang erya sa lugar-paggawa pinakamahirap ipatupad ang physical at social distancing?*", validators=[DataRequired(), InputRequired()])
    # supplements = BooleanField("Nagbigay ba ng libreng mga bitamina o iba pang pagkain/suplay na makatutulong \
    #     sa pagpapalakas ng resistensya ng mga manggagawa?*", validators=[])
    # supplementList = StringField("Kung oo, anu-ano ang mga ito?")
    # mhprograms = BooleanField("May programa ba para sa mental health ng mga manggagawa ang kumpanya?*", default="Oo", false_values=(False, "Wala"), validators=[])
    # freePPE = BooleanField("Nagbibigay ba ang kumpanya ng libreng personal protective equipment (PPE) sa \
    #     mga manggagawa?*", validators=[])
    # freePPEDetails = StringField("Anu-ano ang mga PPE na ipinamimigay at gaano kadalas palitan?")
    # adequateSoapAndWater = BooleanField("May sapat bang suplay ng tubig at sabon sa lugar-paggawa para sa madalas na \
    #     paghuhugas ng mga kamay ng manggagawa?*", validators=[])
    # freeRubbingAlcohol = BooleanField("May ipanamimigay bang libreng alcohol o hand sanitizer ang kumpanya sa mga manggagawa?*", default="Oo", validators=[])
    # regularDisinfection = BooleanField("Nagsasagawa ba ng regular na disinfection ang kumpanya sa iba’t ibang erya sa \
    #     loob ng lugar-paggawa?*", default="Oo", validators=[])
    # hoursPerDay = SelectField("Ilang oras ang pasok ninyo sa trabaho ngayong panahon ng pandemya?*", choices=hoursPerDayOptions, validators=[DataRequired(), InputRequired()])
    # overtime = BooleanField("May overtime bang ipinapatupad ang kumpanya?*", validators=[])
    # covidInformationCampaign = BooleanField("Nagsasagawa ba ng information and awareness campaign ang kumpanya hinggil sa \
    #     COVID-19 at kung paano magiging ligtas sa impeksyon ang mga manggagawa at mapigilan \
    #     ang pagkalat nito sa lugar-paggawa?*", validators=[])
    # covidInformationCampaignDetails = StringField("Kung oo, ilista ang mga pamamaraan kung paano ito isinasagawa ng kumpanya.")
    # freeSafeTransportation = BooleanField("Nagbigay ba ng libre at ligtas na transportasyon ang inyong kumpanya para sa \
    #     mga manggagawa?*", validators=[])
    # freeSafeTransportationDetails = StringField("Kung oo, anu-ano ito at paano naisasapraktika ang kaligtasan at social distancing \
    #     sa byahe?")
    # freeSafeAccomodation = BooleanField("Nagbigay ba ng libre at ligtas na akomodasyon ang inyong kumpanya para sa mga \
    #     manggagawang malayo ang inuuwian o para malimita rin ang kanilang exposure sa coronavirus?*", validators=[])
    # freeSafeAccomodationDetails = StringField("Kung oo, ilarawan ang akomodasyong ibinigay para sa mga manggagawa.")
    # freeMedicalCheckup = BooleanField("Naglunsad ba ng libreng medical check-up sa hanay ng mga manggagawa?*", validators=[])
    # covidRiskAssessment = BooleanField("Naglunsad ba ng risk assessment sa iba’t ibang erya sa lugar-paggawa para i-check \
    #     ang bentilasyon, maayos na layout, espasyo at iba pa?*", validators=[])
    # isolationRoomPresent = BooleanField("May isolation room ba sa lugar paggawa para sa mga manggagawang magpapakita ng \
    #     mga sintomas ng COVID-19 sa panahon ng trabaho?*", validators=[])
    # actionTakenForCOVID = StringField("Anu-ano ang mga hakbang na ginagawa ng management kapag may suspect na COVID \
    #    case sa lugar-paggawa?*", validators=[DataRequired(), InputRequired()])
    # COVIDCaseConfirmed = BooleanField("Nagkaroon na ba ng confirmed COVID case sa lugar-paggawa?*", validators=[])
    # numberOfCOVIDCasesConfirmed = SelectField("Kung oo, ilan na ang naitalang confirmed COVID case?*", choices=caseCountOptions, validators=[DataRequired(), InputRequired()])
    # companyPaysForTreatment = BooleanField("Sagot ba ng kumpanya ang pagpapagamot sa mga confirmed COVID case?*", validators=[])
    # contactTracing = BooleanField("Nagsagawa ba ng contact tracing ang kumpanya nang magkaroon ng probable o confirmed \
    #     COVID case sa lugar-paggawa?*", validators=[])
    # quarantineProcessForContacted = BooleanField("May mga quarantine procedure ba para sa mga contact?*", validators=[])
    # sickSalary = BooleanField("Kapag na-quarantine ang manggagawa, tuloy ba ang kanyang sahod?*", validators=[])
    # sickHealthMonitoring = BooleanField("Kapag na-quarantine ba ang manggawa, tuluy-tuloy ba ang pagmonitor ng kumpanya \
    #     sa kanyang kalusugan?*", validators=[])
    # healthInsurance = BooleanField("May health insurance bang ibinigay ang kumpanya sa mga manggagawa na maaaring \
    #     magamit para sa pagpapagamot kung sakaling magkaroon sila ng COVID-19?*", validators=[])
    # hazardPay = BooleanField("May hazard pay bang natatanggap ang mga manggagawa?*", validators=[])
    # admissionOfVulnerable = BooleanField("Pinapapasok ba ang bulnerableng seksyon ng mga manggagawa (may mga comorbidity \
    #     o pre-existing illness, high risk pregnancy o 60 years old and above)?*", validators=[])
    # OSHCommittee = BooleanField("May nakatayo bang occupational safety and health (OSH) committee?*", validators=[])
    # DOLEInspection = BooleanField("Nagsagawa ba ng inspeksyon ang Department of Labor and Employment para subaybayan \
    #     ang pagpapatupad ng kumpanya ng mga prevention and control measure para sa COVID-19?*", validators=[])
    # submit = SubmitField("Submit Form (Ipasa ang form)")








'''
COVID-19 Health Protocol Assessment Form
 - Pangalan - StringField
 - Contact Number - TelField
 - E-mail address - EmailField
 - Pangalan ng Kumpanya - StringField
 - Lokasyon ng Kumpanya - SelectField
 - Nagsagawa ba ng free mass testing ang kumpanya sa hanay ng mga manggagawa? - BooleanField
 - Kung oo, paano tinukoy ang mga dapat sumailalim sa test? Anong klaseng test
    (rapid antibody test o rt-PCR/swab test) at saan ito isinagawa? - StringField
 - Nagsasagawa ba ang kumpanya ng daily health monitoring tulad ng pag-check ng
    body temperature at pagpapasagot ng daily health questionnaire sa mga manggagawa
    bago pumasok sa loob ng lugar-paggawa? - BooleanField
 - Naipatutupad ba ang physical at social distancing sa iba’t ibang erya ng
    lugar-paggawa – production area, canteen, pantry, office, locker area, exit and
    entrance, at iba pa? - BooleanField
 - Saang erya sa lugar-paggawa pinakamahirap ipatupad ang physical at social distancing? - StringField
 - Nagbigay ba ng libreng mga bitamina o iba pang pagkain/suplay na makatutulong
    sa pagpapalakas ng resistensya ng mga manggagawa? - BooleanField
 - Kung oo, anu-ano ang mga ito? - StringField
 - May programa ba para sa mental health ng mga manggagawa ang kumpanya? - BooleanField
 - Nagbibigay ba ang kumpanya ng libreng personal protective equipment (PPE) sa
    mga manggagawa? - BooleanField
 - Anu-ano ang mga PPE na ipinamimigay at gaano kadalas palitan? - StringField
 - May sapat bang suplay ng tubig at sabon sa lugar-paggawa para sa madalas na
    paghuhugas ng mga kamay ng manggagawa? - BooleanField
 - May ipanamimigay bang libreng alcohol o hand sanitizer ang kumpanya sa mga manggagawa? - BooleanField
 - Nagsasagawa ba ng regular na disinfection ang kumpanya sa iba’t ibang erya sa
    loob ng lugar-paggawa? - BooleanField
 - Ilang oras ang pasok ninyo sa trabaho ngayong panahon ng pandemya? - IntegerField
 - May overtime bang ipinapatupad ang kumpanya? - BooleanField
 - Nagsasagawa ba ng information and awareness campaign ang kumpanya hinggil sa
    COVID-19 at kung paano magiging ligtas sa impeksyon ang mga manggagawa at mapigilan
    ang pagkalat nito sa lugar-paggawa? - - BooleanField
 - Kung oo, ilista ang mga pamamaraan kung paano ito isinasagawa ng kumpanya. - StringField
 - Nagbigay ba ng libre at ligtas na transportasyon ang inyong kumpanya para sa
    mga manggagawa? - BooleanField
 - Kung oo, anu-ano ito at paano naisasapraktika ang kaligtasan at social distancing
    sa byahe? - StringField
 - Nagbigay ba ng libre at ligtas na akomodasyon ang inyong kumpanya para sa mga
    manggagawang malayo ang inuuwian o para malimita rin ang kanilang exposure sa coronavirus? - BooleanField
 - Kung oo, ilarawan ang akomodasyong ibinigay para sa mga manggagawa. - StringField
 - Naglunsad ba ng libreng medical check-up sa hanay ng mga manggagawa? - BooleanField
 - Naglunsad ba ng risk assessment sa iba’t ibang erya sa lugar-paggawa para i-check
    ang bentilasyon, maayos na layout, espasyo at iba pa? - BooleanField
 - May isolation room ba sa lugar paggawa para sa mga manggagawang magpapakita ng
    mga sintomas ng COVID-19 sa panahon ng trabaho? - BooleanField
 - Anu-ano ang mga hakbang na ginagawa ng management kapag may suspect na COVID
    case sa lugar-paggawa? - StringField
 - Nagkaroon na ba ng confirmed COVID case sa lugar-paggawa? - BooleanField
 - Kung oo, ilan na ang naitalang confirmed COVID case? - SelectField
    (1-10 kaso, 10-50 kaso, 50-100 kaso, mas marami pa sa 100 na kaso)
 - Sagot ba ng kumpanya ang pagpapagamot sa mga confirmed COVID case? - BooleanField
 - Nagsagawa ba ng contact tracing ang kumpanya nang magkaroon ng probable o confirmed
    COVID case sa lugar-paggawa? - BooleanField
 - May mga quarantine procedure ba para sa mga contact? - BooleanField
 - Kapag na-quarantine ang manggagawa, tuloy ba ang kanyang sahod? - BooleanField
 - Kapag na-quarantine ba ang manggawa, tuluy-tuloy ba ang pagmonitor ng kumpanya
    sa kanyang kalusugan? - BooleanField
 - May health insurance bang ibinigay ang kumpanya sa mga manggagawa na maaaring
    magamit para sa pagpapagamot kung sakaling magkaroon sila ng COVID-19? - BooleanField
 - May hazard pay bang natatanggap ang mga manggagawa? - BooleanField
 - Pinapapasok ba ang bulnerableng seksyon ng mga manggagawa (may mga comorbidity
    o pre-existing illness, high risk pregnancy o 60 years old and above)? - BooleanField
 - May nakatayo bang occupational safety and health (OSH) committee? - BooleanField
 - Nagsagawa ba ng inspeksyon ang Department of Labor and Employment para subaybayan
    ang pagpapatupad ng kumpanya ng mga prevention and control measure para sa COVID-19? - BooleanField
'''
