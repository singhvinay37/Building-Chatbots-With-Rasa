from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import smtplib
import pandas as pd
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class ActionValidateLocation(Action):
	def name(self):
		return 'action_validate_location'
		
	def run(self, dispatcher, tracker, domain):
		list_loc = ["ahmedabad","bangalore","chennai","delhi","hyderabad","kolkata","mumbai","pune","agra","ajmer","aligarh","allahabad","amravati","amritsar",
					"asansol","aurangabad","bareilly","belgaum","bhavnagar","bhiwandi","bhilai","bhopal","bhubaneswar","bikaner","bokaro steel city","chandigarh","coimbatore",
					"cuttack","dehradun","dhanbad","durgapur","erode","faridabad","firozabad","ghaziabad","gorakhpur","gulbarga","guntur","gurgaon",
					"guwahati","gwalior","hubli-dharwad","indore","jabalpur","jaipur","jalandhar","jammu","jamnagar","jamshedpur","jhansi","jodhpur","kannur","kanpur","kakinada",
					"kochi","kottayam","kolhapur","kollam","kota","kozhikode","kurnool","lucknow","ludhiana","madurai","malappuram","mathura","goa","mangalore","meerut",
					"moradabad","mysore","nagpur","nanded","nashik","nellore","noida","palakkad","patna","pondicherry","raipur","rajkot","rajahmundry","ranchi","rourkela",
					"salem","sangli","siliguri","solapur","srinagar","sultanpur","surat","thiruvananthapuram","thrissur","tiruchirappalli","tirunelveli","tiruppur","ujjain",
					"vijayapura","vadodara","varanasi","vasai-virar city","vijayawada","visakhapatnam","warangal"]
		loc = tracker.get_slot('location')
		if loc is not None:
			if loc.lower() in list_loc:
				return[SlotSet('location',loc)]
			else:
				dispatcher.utter_message("Sorry, we don’t operate in this city. Can you please specify some other location")
				return[SlotSet('location',None)]
		else:
			dispatcher.utter_message("Sorry, we don’t operate in this city. Can you please specify some other location")
			return[SlotSet('location', None)]

class ActionValidateCuisine(Action):
	def name(self):
		return 'action_validate_cuisine'
		
	def run(self, dispatcher, tracker, domain):
		list_cuis = ["chinese","mexican","italian","american","south indian","north indian"]
		cuis = tracker.get_slot('cuisine')
		if cuis is not None:
			if cuis.lower() in list_cuis:
				return[SlotSet('cuisine',cuis)]
			else:
				dispatcher.utter_message("Sorry, we don’t serve this cuisine. Can you please specify some other cuisine preference")
				return[SlotSet('cuisine',None)]
		else:
			dispatcher.utter_message("Sorry, we don’t serve this cuisine. Can you please specify some other cuisine preference")
			return[SlotSet('cuisine', None)]         
            
class ActionValidateBudget(Action):
    def name(self):
        return 'action_validate_budget'

    def run(self, dispatcher, tracker, domain):
        price = tracker.get_slot('budget')
        list_budget_low = ['low','less','cheap','less than 300','Lesser than Rs 300','<300']
        list_budget_mid = ['mid','average','between 300 and 700','Rs. 300 to 700','moderate']
        list_budget_high = ['high','expensive','more than 700','costly','greater than 700','>700']
        if price is not None:
            if price.lower() in list_budget_low:
                return[SlotSet('budget','low')]
            elif price.lower() in list_budget_mid:
                return[SlotSet('budget','mid')]
            elif price.lower() in list_budget_high:
                return[SlotSet('budget','high')]
            else:
                return[SlotSet('budget', 'mid')] #default
            
            
class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config={ "user_key":"8b113977c6ea374631f4bc8318fd8536"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('budget')
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'american':1,'chinese':25,'mexican':73,'italian':55,'north indian':50,'south indian':85}
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),"rating","desc", 20)
        d=json.loads(results)
        response=""
        restaurants=d['restaurants']
        global restaurant_df
        restaurant_df=pd.DataFrame([{'zomato rating':restaurant['restaurant']["user_rating"]["aggregate_rating"],'restaurant name':restaurant['restaurant']['name'],'restaurant address': restaurant['restaurant']['location']['address'],'avg. budget for two': restaurant['restaurant']['average_cost_for_two']} 
                                    for restaurant in restaurants])
        def pricerange(row):
            if row['avg. budget for two'] < 300:
                return 'low'
            elif row['avg. budget for two'] > 700:
                return 'high'
            else:
                return 'mid'
        restaurant_df['budget']=restaurant_df.apply(lambda row: pricerange(row), axis=1)
        restaurant_df=restaurant_df[(restaurant_df['budget']== budget)]    
        restaurant_df = restaurant_df.sort_values(['zomato rating','avg. budget for two'], ascending=[False,True])
        restaurant_df = restaurant_df.head(5)
        
# show results 
        if len(restaurant_df) != 0:
            for index, row in restaurant_df.iterrows():
                response = response + row['restaurant name']+ "\" in "+ row['restaurant address']+" has been rated "+ row['zomato rating']+"\n"
        else:
            response = 'There are no restaurants available in given price range'
        dispatcher.utter_message(response)
        return [SlotSet('budget',budget)]


class ActionValidateEmail(Action):
    def name(self):
        return 'action_validate_email'

    def run(self, dispatcher, tracker, domain):
        email_val = tracker.get_slot('email')
        print(email_val)
        if email_val is not None:
            if re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",email_val):
                return[SlotSet('email',email_val)]
            else:
                dispatcher.utter_message("Sorry this is not a valid email. please provide correct email id.")
                return[SlotSet('email',None)]
        else:
            dispatcher.utter_message("Sorry this is not a valid email. please provide correct email id.")
            return[SlotSet('email', None)]
        
        
class ActionMail(Action):
    def name(self):
        return 'action_send_email'

    def run(self,dispatcher, tracker, domain):
        config = {"user_key":"8b113977c6ea374631f4bc8318fd8536"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('budget')
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'american':1,'chinese':25,'mexican':73,'italian':55,'north indian':50,'south indian':85}
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),"rating","desc", 20)
        d=json.loads(results)
        restaurants=d['restaurants']
        global restaurant_df
        restaurant_df=pd.DataFrame([{'zomato rating':restaurant['restaurant']["user_rating"]["aggregate_rating"],'restaurant name':restaurant['restaurant']['name'],'restaurant address': restaurant['restaurant']['location']['address'],'avg. budget for two': restaurant['restaurant']['average_cost_for_two']} 
                                    for restaurant in restaurants])
        def pricerange(row):
            if row['avg. budget for two'] < 300:
                return 'low'
            elif row['avg. budget for two'] > 700:
                return 'high'
            else:
                return 'mid'
        restaurant_df['budget']=restaurant_df.apply(lambda row: pricerange(row), axis=1)
        restaurant_df=restaurant_df[(restaurant_df['budget']== budget)]   
# sort restaurants based on rating and avearge budget 
        restaurant_df = restaurant_df.sort_values(['zomato rating','avg. budget for two'], ascending=[False,True])
        email = tracker.get_slot('email')
        gmail_user = ''  #type your email id here
        gmail_password = '' #type your password here
        sent_from = gmail_user  
        to_email = str(email)
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Foodie: Requested TOP Rated Restaurant Details"
        msg['From'] = gmail_user
        msg['To'] = to_email
        if len(restaurant_df) == 0:
            html = """
            <html>
            <head>
            </head>
            <body>
            <p>Hi!</p>
            <p>Thanks for using Foodie, the restaurant chatbot.</p>
            <p>Sorry, we could not find restaurant that meet your criteria.</p>
            """
        else:
            restaurant_df10 = restaurant_df.head(10)
            s = pd.Series(range(1,len(restaurant_df10)+1))
            restaurant_df10 = restaurant_df10.set_index(s)
            restaurant_df10.drop(['budget'], axis=1, inplace=True)
            html = """
            <html>
            <head>
            </head>
            <body>
            <p>Hey there,</p>
            <p>Please find the requested list of top rated restaurants below.</p>
            <p>Thanks for contacting me.</p>
             """
            html = html+restaurant_df10.to_html() + "\n"
            html = html+" As per your interest, "+cuisine+" restaurants for dining in "+budget+" range budget at "+loc+"</body></html>"
        part2 = MIMEText(html, 'html')
        msg.attach(part2)
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to_email, msg.as_string())
        server.close()
        dispatcher.utter_message("Email Sent")
        return [SlotSet('email',email)]