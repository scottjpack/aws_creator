
'''
AWS Account Creator

Populate these values with an gmail address and password that you control
The Alias will be appended to the email along with an incremental offset, ie email-address+EC2-12@gmail.com
Specify the password you want to use for the AWS account

I haven't gotten as far as to set up billing or spin up the EC2 boxes yet.

This can't be run on a headless box, as it requires Selenium to execute the javascript in the browser.  If there's a good way around this, please let me know.
'''

import os
from PIL import Image
from selenium import webdriver
import random
import time




EMAIL="salt_ec2_hosts"
ALIAS="EC2"
NAME="Salt Hosts"
PASSWORD="whitedragon"
OFFSET=12

locations = ["18015","Bethlehem","PA"],["55311","Osseo","MN"],["12533","Hopewell Junction","NY"],["44004","Ashtabula","OH"],["14606","Rochester","NY"],["11357","Whitestone","NY"],["33470","Loxahatchee","FL"],["32708","Winter Springs","FL"],["19454","North Wales","PA"],["32043","Green Cove Springs","FL"],["30040","Cumming","GA"],["46060","Noblesville","IN"],["78213","San Antonio","TX"],["02816","Coventry","RI"],["01089","West Springfield","MA"],["33460","Lake Worth","FL"],["29730","Rock Hill","SC"],["30721","Dalton","GA"],["14450","Fairport","NY"],["34711","Clermont","FL"]

streets = ["Orchard Lane","Railroad Street","Myrtle Avenue","Route 202","Bridge Street","Inverness Drive","Magnolia Avenue","North Street","Sycamore Lane","Madison Avenue"]

gen_email = "%s+%s-%s@gmail.com" % (EMAIL,ALIAS,OFFSET)

aws_registration_start = "http://aws.amazon.com/account/"
browser = webdriver.Firefox()
browser.get(aws_registration_start)
create_acct = browser.find_element_by_link_text("Create a Free Account")
create_acct.click()
ap_email = browser.find_element_by_name("email")
ap_email.send_keys(gen_email)
new_user = browser.find_element_by_name("create")
new_user.click()
sign_in = browser.find_element_by_id("signInSubmit-input")
sign_in.click()
username = browser.find_element_by_id("ap_customer_name")
username.send_keys(NAME)
#Prefilled
#ap_email = browser.find_element_by_id("ap_email")
#ap_email.send_keys(gen_email)
confirm_email = browser.find_element_by_id("ap_email_check")
confirm_email.send_keys(gen_email)
password = browser.find_element_by_id("ap_password")
password.send_keys(PASSWORD)
confirm_password = browser.find_element_by_id("ap_password_check")
confirm_password.send_keys(PASSWORD)
create_acct = browser.find_element_by_id("continue-input")
create_acct.click()
name = browser.find_element_by_name("fullName")
name.send_keys(NAME)

location = random.choice(locations)
street = random.choice(streets)
street_address = "%s %s" % (random.choice(range(5,50)),street)

addr = browser.find_element_by_name("addressLine1")
addr.send_keys(street_address)
city = browser.find_element_by_name("city")
city.send_keys(location[1])
state = browser.find_element_by_name("state")
state.send_keys(location[2])
pc = browser.find_element_by_name("postalCode")
pc.send_keys(location[0])
agreement = browser.find_element_by_name("agreementAccepted")
agreement.click()

phone_number = random.choice(range(2000000,8000000))
phone_prefix = random.choice(range(200,800))
phone = browser.find_element_by_name("phoneNumber")
phone.send_keys("%s%s" % (phone_prefix,phone_number))


filled = False
print "Waiting for Captcha completion"
while (not filled):
	guess = browser.find_element_by_name("guess")
	val = guess.get_attribute("value")
	print val
	if val == "":
		filled = False
	else:
		filled = True
		
print "Captcha filled, moving on"
time.sleep(10)

submit = browser.find_element_by_class_name("display-block width-450 margin-side-auto a-button a-button-primary")
submit.click()

