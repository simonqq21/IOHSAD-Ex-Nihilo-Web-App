from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, IntegerField
from wtforms.fields import TelField, EmailField
from wtforms.validators import DataRequired, Email, InputRequired, Optional

'''
-Name of Company
-Presence of union (If yes, put down the contact details of the head of the union (contact number and email)
-Contact Details of the one who submitted the form

then finally a large textbox for the nature of the complaint
'''
class ComplaintForm(FlaskForm):
    username = StringField("Unique Username*", validators=[DataRequired(), InputRequired()])
    companyName = StringField("Company Name* (Pangalan ng kumpanya)*", validators=[DataRequired(), InputRequired()])
    unionPresence = BooleanField("Union Present* (Mayroon bang unyon ng mga manggagawa?)*")
    unionHeadContactNo = TelField("Union Head Contact No. (Telepono ng pinuno ng unyon ng mga manggagawa)", validators=[Optional()])
    unionHeadEmail = EmailField("Union Head Email Address (Email address ng pinuno ng unyon ng mga manggagawa)", validators=[Email(), Optional()])
    emailPhone = StringField("Contact No. / Email Address* (Telepono / Email Address)*", validators=[DataRequired(), InputRequired()])
    complaint = TextAreaField("Enter you complaint here* (I-type ang inyong reklamo dito*)", validators=[DataRequired(), InputRequired()])
    submit = SubmitField("Submit Form (Ipasa ang form)")

'''
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
class
