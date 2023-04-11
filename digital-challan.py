import streamlit as st
import smtplib
import re
from PIL import Image
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("kriya.json", scope)
client = gspread.authorize(creds)
sheet = client.open("psg_bank").sheet1 
# data = sheet.get_all_records()
st.set_page_config(page_title="Digital Challan",layout="wide")
l=[]
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
page_bg="""
<style>
[data-testid="stAppViewContainer"]{
    background-image: url("https://c4.wallpaperflare.com/wallpaper/303/229/316/photo-of-man-in-motorcycle-suit-riding-on-red-and-white-sport-bike-wallpaper-preview.jpg");
    background-size: cover;
}
[data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
}
</style>
"""
# with c2:
st.markdown(page_bg,unsafe_allow_html=True)

c1,c2,c3=st.columns([0.2,1.2,1])
with c2:
    cell = sheet.cell(1,1).value
    # print(cell)
    data=sheet.get_all_values()
    for i in range(1,len(data)):
        if data[i][0]==cell:
            l=data[i]
            print(l)
            break
    st.write(f'''<h4 style="margin-left:135px"> Account number: {l[0]}</h4>''',unsafe_allow_html=True)
    st.write(f'''<h4 style="margin-left:135px"> Name: {l[2]}</h4>''',unsafe_allow_html=True)
    st.write(f'''<h4 style="margin-left:135px"> DOB: {l[3]}</h4>''',unsafe_allow_html=True)
    st.write(f'''<h4 style="margin-left:135px"> Branch: {l[4]}</h4>''',unsafe_allow_html=True)
    st.write(f'''<h4 style="margin-left:135px">Phone No.: {l[5]}</h4>''',unsafe_allow_html=True)
    st.write(f'''<h4 style="margin-left:135px"> Current Balance: {l[6]}</h4>''',unsafe_allow_html=True)
def mail(name,type_,id,to_):
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("sarvesh20123@gmail.com","agcrudcldljbnylx")
    # text=f"Hello ! \nYou now can register for upcoming Technotronz events\nYour login credentials are :\nRegistration ID: TZ23{str(int(r[4:])+1)}\nName: {name}\nContact number: {ph}\n\nNote: You can use this mail as verification if the registration pdf went missing.\n\nBest regards,\nTeam Technotronz."
    text=f"Hello {name},\nYou have requested for {type_}.\nYour Transaction ID is: {id}.\n\nNOTE: This Transaction ID is valid for 24 hours."
    message='Subject: {}\n\n{}'.format("Your request has been submitted.",text )
    server.sendmail("sarvesh20123@gmail.com",to_,message)
    server.quit()
f=0
with c3:
    event=st.selectbox("Choose the transaction type:",options=["--Choose--","Deposit","Withdrawal"],index=0)
    t=0
    if event=="Deposit":
        acc_no=st.text_input("Enter the Account Number")
        amt_d=st.text_input("Enter the amount to be deposited:")
        t=2
    if event=="Withdrawal":
        amt_w=st.text_input("Enter the amount to be withdrawn:")
        t=1
    if t==1:
        if st.button("Proceed"):
            if int(amt_w)>int(l[6]) or int(amt_w)==0 or amt_w.isalpha():
                if int(amt_w)>int(l[6]):
                    st.error("Insufficient funds!")
                else:
                    st.error("Invalid data. Please enter again.")
            else:
                st.success("Your challan has been requested successfully")
                # st.write("Your Transaction ID is "+ sheet.cell(1,2).value)
                st.write(f'''<h4 style="margin-left:135px"> Your Transaction ID is {sheet.cell(1,2).value}</h4>''',unsafe_allow_html=True)
                id=sheet.cell(1,2).value
                sheet.update_cell(1,2,int(sheet.cell(1,2).value)+1)
                
                for i in range(1,len(data)):
                    if data[i][0]==cell:
                        var=sheet.cell(i+1,7).value
                        # print(var,type(var))
                        sheet.update_cell(i+1,9,int(var)-int(amt_w))
                        sheet.update_cell(i+1,10,id)
                        sheet.update_cell(i+1,11,"WD")
                        # name,type,id,to
                        mail(data[i][2],"withdrawal",id,data[i][7])
                        st.write(f'''<h6 style="margin-left:135px"> A mail with details has been sent to you. </h6>''',unsafe_allow_html=True)
                        break                
                
    if t==2:
        if st.button("Proceed"):
            if int(amt_d)==0 or amt_d.isalpha():
                st.error("Invalid data. Please enter again.")
            for i in range(1,len(data)):
                if data[i][0]==acc_no:
                    f=1
                    break             
            else:
                st.error("Invalid bank account number")
            if f==1:
                st.success("Your challan has been requested successfully")
                st.write(f'''<h4 style="margin-left:135px"> Your Transaction ID is {sheet.cell(1,2).value}</h4>''',unsafe_allow_html=True)
                id=sheet.cell(1,2).value
                sheet.update_cell(1,2,int(sheet.cell(1,2).value)+1)
                var=sheet.cell(i+1,7).value
                sheet.update_cell(i+1,9,int(var)+int(amt_d))
                sheet.update_cell(i+1,10,id)
                sheet.update_cell(i+1,11,"DEP")
                mail(data[i][2],"deposition",id,data[i][7])
                st.write(f'''<h6 style="margin-left:135px"> A mail with details has been sent to you. </h6>''',unsafe_allow_html=True)
                # break

        # if amt<l[6]:
            
    # amt=
    # st.write(l)
